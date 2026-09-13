from PyQt6.QtWidgets import QApplication, QDoubleSpinBox, QWidget
from PyQt6.QtGui import QCursor
from PyQt6.QtCore import QPoint
from krita import Krita
import random

def last_smaller_fib(n):
    if n <= 1:
        return 1

    n = round(n)
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    return a

def first_larger_fib(n):
    # n could be stupid number like 0.99999 so we need some special cases and rounding
    if n < 0.9:
        return 1

    n = round(n)
    a, b = 0, 1
    while b <= n:
        a, b = b, a + b
    return min(b, 987)

def increase_brush_size():
    activeView = Krita.instance().activeWindow().activeView()
    liquify_slider = _get_liquify_slider()
    if  liquify_slider and liquify_slider.isVisible():
        liquify_slider.setValue(first_larger_fib(liquify_slider.value()))
    else:
        activeView.setBrushSize(first_larger_fib(activeView.brushSize()))
    _nudge_mouse()

def decrease_brush_size():
    activeView = Krita.instance().activeWindow().activeView()

    liquify_slider = _get_liquify_slider()
    if liquify_slider and liquify_slider.isVisible():
        liquify_slider.setValue(last_smaller_fib(liquify_slider.value()))
    else:
        activeView.setBrushSize(last_smaller_fib(activeView.brushSize()))
    _nudge_mouse()

def _nudge_mouse():
    """
    Moves the mouse 1px down to force Krita to redraw the cursor/brush outline.
    """
    pos = QCursor.pos()
    # Move randomly 1 pixel up or down
    QCursor.setPos(pos + QPoint(0, random.choice([-1, 1])))
    # Optional: Process events to ensure the move is registered immediately
    QApplication.processEvents()

# From https://krita-artists.org/t/customize-the-steps-of-brush-size-when-increasing-decreasing-it-with-shortcuts/151604/2
def _get_liquify_slider():
    """
    Navigates the Krita UI hierarchy to find the liquify size spinner.
    Returns None if the tool or docker is not active.
    """
    try:
        # 1. Get the shared options docker
        dockers = Krita.instance().dockers()
        dock = next((d for d in dockers if d.objectName() == 'sharedtooldocker'), None)
        if not dock: return None
        
        # 2. Find the Transform Tool widget inside the docker
        # If the transform tool isn't active, this widget usually won't be found or won't be visible
        transform_widget = dock.findChild(QWidget, "KisToolTransform option widget")
        if not transform_widget: return None

        # 3. Find the specific slider for liquify size
        slider = transform_widget.findChild(QDoubleSpinBox, "liquifySizeSlider")
        return slider
    except Exception as e:
        # Fail silently to fall back to brush size
        return None