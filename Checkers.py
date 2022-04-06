import sys
from PyQt5.QtWidgets import QWidget,QApplication, QLabel, QMainWindow, QPushButton,QVBoxLayout, QGridLayout
from PyQt5.QtCore import QCoreApplication,Qt
from PyQt5.QtGui import QPixmap,QColor, QPalette

class Color(QWidget):
  def __init__(self, color):
    super().__init__()
    self.setAutoFillBackground(True) 
    self.myPalette = self.palette() 
    self.myPalette.setColor(QPalette.Window, QColor(color))
    self.setPalette(self.myPalette) 

class Window2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Grid Layouts")
        self.layout = QGridLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0,0,0,0)
        for i in range (4):
            if i%2 == 0:
                for j in range(4):
                    if j%2 == 0:
                        self.layout.addWidget(Color('black'),i,j)
                    else:
                        self.layout.addWidget(Color('white'),i,j)

            else :
                if i%2 == 1:
                    for j in range(4):
                        if j%2 == 0:
                            self.layout.addWidget(Color('white'),i,j)
                        else:
                            self.layout.addWidget(Color('black'),i,j)
        self.widget = QWidget()
        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

                

app = QCoreApplication.instance()
if app is None:
    app = QApplication(sys.argv)
window = Window2()
window.show()
app.exec_()
