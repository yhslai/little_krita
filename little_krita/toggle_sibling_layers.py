# If only one layer is selected, toggle it and its last previous sibling (the layer it is behind it and at the same level).
# If it doesn't have a previous sibling, toggle itself.
# If multiple layers are selected, toggle them all.

# Layer group that named "t${number}" is special. If we called this in such a group, toggle "t${number}" and "t${number}-1".

from krita import Krita, InfoObject, Selection

def toggle(node):
    node.setVisible(not node.visible())

def is_root_node(node):
    return node.parentNode() is None

def is_top_level(node):
    return is_root_node(node.parentNode())

def parse_t_group_name(name):
    if not name.startswith('t'):
        return None
    try:
        return int(name[1:])
    except Exception as e:
        return None
    
    

def find_previous_t_group(node):
    cur = node
    t_group = None
    while cur:
        if cur.type() == 'grouplayer':
            t_number = parse_t_group_name(cur.name())
            if t_number is not None:
                t_group = cur
                break
        cur = cur.parentNode()

    if t_group:
        return t_group, find_previous_sibling(t_group)

    return None, None

def find_previous_sibling(node):
    parent = node.parentNode()
    if parent:
        found = False
        for child in reversed(parent.childNodes()):
            if child == node:
                found = True
            elif found:
                return child 
    return None

def toggle_sibling_layers():
    app = Krita.instance()
    doc = app.activeDocument()
    window = app.activeWindow()
    view = window.activeView()
    selected_layers = view.selectedNodes()

    if len(selected_layers) == 1:
        layer = selected_layers[0]
        t_group, prev_sibling = find_previous_t_group(layer)
        if t_group:
            toggle(t_group)
            toggle(prev_sibling)
        else:
            prev_sibling = find_previous_sibling(layer)
            if prev_sibling:
                toggle(layer)
                toggle(prev_sibling)
            else:
                toggle(layer)
    else:
        for layer in selected_layers:
            toggle(layer)

    # Hack: Force Overview Docker to update
    app.action('toggle_layer_visibility').trigger()
    app.action('toggle_layer_visibility').trigger()

    doc.refreshProjection()
