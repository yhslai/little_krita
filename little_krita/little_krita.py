from krita import *
from PyQt6 import QtCore
from .create_tracing_paper import create_tracing_paper
from .remove_tracing_papers import remove_tracing_papers
from .merge_down_unnamed import merge_down_unnamed
from .flip_brush import flip_brush
from .change_brush_size import increase_brush_size, decrease_brush_size
from .toggle_sibling_layers import toggle_sibling_layers

class LittleKrita(Extension):

    def __init__(self, parent):
        # This is initialising the parent, always important when subclassing.
        super().__init__(parent)

    def setup(self):
        pass

    def createTracingPaper(self):
        create_tracing_paper()

    def removeTracingPapers(self):
        remove_tracing_papers()

    def mergeDownUnnamed(self):
        merge_down_unnamed()

    def flipBrush(self):
        flip_brush()

    def increaseBrushSize(self):
        increase_brush_size()

    def decreaseBrushSize(self):
        decrease_brush_size()

    def createActions(self, window):
        act1 = window.createAction("createTracingPaper", "Create Tracing Paper", "tools/little_krita/scripts")
        act1.triggered.connect(self.createTracingPaper)
        act1.setVisible(False)

        act2 = window.createAction("removeTracingPapers", "Remove Tracing Papers", "tools/little_krita/scripts")
        act2.triggered.connect(self.removeTracingPapers)
        act2.setVisible(False)

        act3 = window.createAction("mergeDownUnnamed", "Merge Down Unnamed", "tools/little_krita/scripts")
        act3.triggered.connect(self.mergeDownUnnamed)
        act3.setVisible(False)

        act4 = window.createAction("flipBrush", "Flip Brush", "tools/little_krita/scripts")
        act4.triggered.connect(self.flipBrush)
        act4.setVisible(False)

        act5 = window.createAction("increaseBrushSizeFib", "Increase Brush Size Fib", "tools/little_krita/scripts")
        act5.triggered.connect(self.increaseBrushSize)
        # act5.setVisible(False)

        act6 = window.createAction("decreaseBrushSizeFib", "Decrease Brush Size Fib", "tools/little_krita/scripts")
        act6.triggered.connect(self.decreaseBrushSize)
        # act6.setVisible(False)

        act7 = window.createAction("toggleSiblingLayers", "Toggle Sibling Layers", "tools/little_krita/scripts")
        act7.triggered.connect(toggle_sibling_layers)
        # act7.setVisible(False)
        pass

# And add the extension to Krita's list of extensions:
Krita.instance().addExtension(LittleKrita(Krita.instance()))
QtCore.qDebug("little_krita extension loaded")