import sys
from PyQt5.QtWidgets import QWidget,QApplication, QLabel, QMainWindow, QPushButton,QVBoxLayout,QHBoxLayout, QGridLayout
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtGui import QPixmap,QColor, QPalette

class Color(QWidget):
  def __init__(self, color):
    super().__init__()
    self.setAutoFillBackground(True) 
    self.myPalette = self.palette() 
    self.myPalette.setColor(QPalette.Window, QColor(color))
    self.setPalette(self.myPalette) 

class Windowfrance(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layouts")
        self.layout = QHBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(Color('blue'))
        self.layout.addWidget(Color('white'))
        self.layout.addWidget(Color('red'))
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        
class Windowgermany(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layouts")
        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.addWidget(Color('black'))
        self.layout.addWidget(Color('red'))
        self.layout.addWidget(Color('yellow'))
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)
        
        


                

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Windowfrance()
window1 = Windowgermany()
window.show()
window1.show()
app.exec_()
