from krita import Krita, InfoObject, Selection


def remove_tracing_papers():
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

    tracing_papers = [node for node in all_layers if node.name().startswith('Tracing Paper ')]
    if tracing_papers:
        for node in tracing_papers:
            node.remove()