import random
from krita import Krita, InfoObject, Selection


def get_next_suffix(prefix=None):
    app = Krita.instance()
    doc = app.activeDocument()
    top_layers = doc.topLevelNodes()
    all_layers = []
    # collect all layers with DFS
    def collect_layers(node):
        all_layers.append(node)
        for child in node.childNodes():
            collect_layers(child)
    for layer in top_layers:
        collect_layers(layer)

    # get all suffixes. Suffixes are the last part of the layer name with a space before it and is a number
    suffixes = []
    for layer in all_layers:
        name = layer.name()
        if ' ' in name:
            suffix = name.split(' ')[-1]
            # prefix is the rest of the name
            if suffix.isdigit():
                if prefix:
                    p = ' '.join(name.split(' ')[:-1])
                    if p != prefix:
                        continue
                suffixes.append(int(suffix))
    
    # get the max suffix
    max_suffix = 0
    if suffixes:
        max_suffix = max(suffixes)
    
    return max_suffix + 1



def create_tracing_paper():
    app = Krita.instance()
    doc = app.activeDocument()
    if not doc:
        return  # no doc
    node = doc.activeNode()
    if not node:
        return  # no node
        
    info = InfoObject()
    info.setProperty(
            'color', (
                '<!DOCTYPE color>'
                '<color channeldepth="U16">'
                '<RGB space="sRGB-elle-V2-g10.icc" r="0.514259576797485" b="0.514259576797485" g="0.514259576797485"/>'
                '</color>'
            ))

    selection = Selection()
    selection.select(0, 0, doc.width(), doc.height(), 255)
    
    fill_layer = doc.createFillLayer(f'Tracing Paper {get_next_suffix("Tracing Paper")}', 'color', info, selection)
    fill_layer.setOpacity(190)

    paint_layer = doc.createNode(f'Paint Layer {get_next_suffix("Paint Layer")}', 'paintlayer')
    
    parent_node = node.parentNode() or doc.rootNode()

    parent_node.addChildNode(fill_layer, node)
    parent_node.addChildNode(paint_layer, fill_layer)

    # fill_layer.setLocked(True)

    doc.refreshProjection()

    return fill_layer, paint_layer

