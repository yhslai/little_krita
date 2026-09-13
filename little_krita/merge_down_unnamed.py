from krita import Krita, InfoObject, Selection
from PyQt6 import QtCore
from PyQt6.QtCore import QTimer


def check_if_next_paint_layer(node):
    app = Krita.instance()
    doc = app.activeDocument()

    queue = []
    top_layers = doc.topLevelNodes()
    # Traverse the tree with BFS to find node's next sibling
    for layer in reversed(top_layers):
        queue.append((layer, 0))

    while queue:
        current, depth = queue.pop(0)
        if current == node:
            # check if the next sibling is a paint layer
            if len(queue) > 0:
                next_sibling, d = queue[0]
                if next_sibling.type() == 'paintlayer' and d == depth:
                    return True
                else:
                    return False
            else:
                return False
        for child in reversed(current.childNodes()):
            queue.append((child, depth + 1))

    return False



def merge_down_unnamed():
    timer = QTimer()
    app = Krita.instance()
    doc = app.activeDocument()

    def try_merge_down_unnamed():
        node = doc.activeNode()
        stop = True

        if node.name().startswith('Paint Layer ') and node.type() == 'paintlayer':
            if check_if_next_paint_layer(node):
                QtCore.qDebug(f'Merging down {node.name()}')
                node.mergeDown()
                stop = False

        if stop:
            timer.stop()


    timer.setInterval(10) 
    timer.timeout.connect(try_merge_down_unnamed)
    timer.start()
    QtCore.qDebug("Merging down unnamed layers")
    QtCore.qDebug(f"{timer}")