from ..Qt import QtGui, QtCore, QT_LIB
import matplotlib

if QT_LIB != 'PyQt5':
    if QT_LIB == 'PySide':
        matplotlib.rcParams['backend.qt4']='PySide'

    from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
    try:
        from matplotlib.backends.backend_qt4agg import NavigationToolbar2QTAgg as NavigationToolbar
    except ImportError:
        from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
else:
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from matplotlib.figure import Figure

class MatplotlibWidget(QtGui.QWidget):
    """
    Implements a Matplotlib figure inside a QWidget.
    Use getFigure() and redraw() to interact with matplotlib.
    
    Example::
    
        mw = MatplotlibWidget()
        subplot = mw.getFigure().add_subplot(111)
        subplot.plot(x,y)
        mw.draw()
    """
    
    def __init__(self, size=(5.0, 4.0), dpi=100, doShowToolbar=True, tight_layout=None):
        QtGui.QWidget.__init__(self)
        self.fig = Figure(size, dpi=dpi, tight_layout=tight_layout)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.setParent(self)
        
        self.vbox = QtGui.QVBoxLayout()

        if doShowToolbar:
            self.toolbar = NavigationToolbar(self.canvas, self)
            self.vbox.addWidget(self.toolbar)

        # for some reason this causes child to be invisible if set to (0,0,0,0)...
        self.vbox.setContentsMargins(1, 1, 1, 1)

        self.vbox.addWidget(self.canvas)

        self.setLayout(self.vbox)

    def getFigure(self):
        return self.fig
        
    def draw(self):
        self.canvas.draw()
