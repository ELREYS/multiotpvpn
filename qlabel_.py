import sys
from PyQt5.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QCheckBox, QComboBox, QLineEdit,
    QLineEdit, QSpinBox, QDoubleSpinBox, QSlider
)
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My App")

        

        label  = QLabel("Hello Giuseppe")
        label.setText("Hi Peppe")
        font = label.font()
        font.setPointSize(30)
        label.setFont(font)
        label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.setCentralWidget(label)


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()