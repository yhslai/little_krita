def flip_brush():
    inst = Krita.instance()
    win = inst.activeWindow()
    view = win.activeView()

    rot = view.brushRotation()

    angle = 180
    rot += angle
    rot %= 360
    
    view.setBrushRotation(rot)
