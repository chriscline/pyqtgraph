# -*- coding: utf-8 -*-
"""
graphicsWindows.py -  Convenience classes which create a new window with PlotWidget or ImageView.
Copyright 2010  Luke Campagnola
Distributed under MIT/X11 license. See license.txt for more information.
"""

from .Qt import QtCore, QtGui, mkQApp
from .widgets.PlotWidget import *
from .imageview import *
from .widgets.GraphicsLayoutWidget import GraphicsLayoutWidget
from .widgets.GraphicsView import GraphicsView


class GraphicsWindow(GraphicsLayoutWidget):
    """
    (deprecated; use :class:`~pyqtgraph.GraphicsLayoutWidget` instead)
    
    Convenience subclass of :class:`~pyqtgraph.GraphicsLayoutWidget`. This class
    is intended for use from the interactive python prompt.
    """
    def __init__(self, title=None, size=(800,600), **kargs):
        mkQApp()
        GraphicsLayoutWidget.__init__(self, **kargs)
        self.resize(*size)
        if title is not None:
            self.setWindowTitle(title)
        self.show()
        

class TabWindow(QtGui.QMainWindow):
    """
    (deprecated)
    """
    def __init__(self, title=None, size=(800,600)):
        mkQApp()
        QtGui.QMainWindow.__init__(self)
        self.resize(*size)
        self.cw = QtGui.QTabWidget()
        self.setCentralWidget(self.cw)
        if title is not None:
            self.setWindowTitle(title)
        self.show()
        
    def __getattr__(self, attr):
        return getattr(self.cw, attr)
    

class PlotWindow(PlotWidget):
    sigClosed = QtCore.Signal(object)

    """
    (deprecated; use :class:`~pyqtgraph.PlotWidget` instead)
    """
    def __init__(self, title=None, **kargs):
        mkQApp()
        self.win = QtGui.QMainWindow()
        PlotWidget.__init__(self, **kargs)
        self.win.setCentralWidget(self)
        for m in ['resize']:
            setattr(self, m, getattr(self.win, m))
        if title is not None:
            self.win.setWindowTitle(title)
        self.win.show()

    def closeEvent(self, event):
        PlotWidget.closeEvent(self, event)
        self.sigClosed.emit(self)


class ImageWindow(ImageView):
    sigClosed = QtCore.Signal(object)

    """
    (deprecated; use :class:`~pyqtgraph.ImageView` instead)
    """
    def __init__(self, *args, **kargs):
        mkQApp()
        self.win = QtGui.QMainWindow()
        self.win.resize(800,600)
        if 'title' in kargs:
            self.win.setWindowTitle(kargs['title'])
            del kargs['title']
        ImageView.__init__(self, self.win)
        if len(args) > 0 or len(kargs) > 0:
            self.setImage(*args, **kargs)
        
        self.win.setCentralWidget(self)
        for m in ['resize']:
            setattr(self, m, getattr(self.win, m))
        self.win.show()
    
    def closeEvent(self, event):
        ImageView.closeEvent(self, event)
        self.sigClosed.emit(self)
