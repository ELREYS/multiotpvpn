import sys
from PyQt5.QtWidgets import QApplication, QHBoxLayout, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtGui import QPalette, QColor



class Color(QWidget):
    def __init__(self, color):
        super().__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setWindowTitle("Title App")

        layoutV = QVBoxLayout()
        layoutV.addWidget(Color("Red"))
        layoutV.addWidget(Color("Green"))
        layoutV.addWidget(Color("Orange"))
        layoutV.addWidget(Color("Blue"))

        layoutH = QHBoxLayout()
        layoutH.addWidget(Color("Red"))
        layoutH.addWidget(Color("Green"))
        layoutH.addWidget(Color("Orange"))
        layoutH.addWidget(Color("Blue"))
        layoutH.setContentsMargins(0,0,-5,0)
        layoutH.setSpacing(20)

        layoutV.addLayout(layoutH)


        widget = QWidget()
        widget.setLayout(layoutV)
        self.setCentralWidget(widget)

app = QApplication(sys.argv)



window = MainWindow()
window.show()

app.exec_()