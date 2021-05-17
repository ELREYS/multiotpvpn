import sys

from PyQt5.QtCore import QSize,Qt
from PyQt5.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QPushButton, QStyle, QVBoxLayout, QVBoxLayout, QWidget,QDialog,QMessageBox
#Need for command line argument
from main import generateBC,unlockVPN,connect_and_execute,connect_and_login,execute_command




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setFixedWidth(400)
        self.setWindowTitle("VPN Tools")
        

        layout = QVBoxLayout()
        logindata = QVBoxLayout()


        #Username input
        lblusername = QLabel("Username")
        lblusername.setAlignment(Qt.AlignBottom)
        self.username = QLineEdit()
        self.username.setPlaceholderText("use LDAP Username")
        self.username.echoMode = QLineEdit.EchoMode.Normal
        logindata.addWidget(lblusername)
        logindata.addWidget(self.username)

        #password input
        lblpw = QLabel("Password")
        lblpw.setAlignment(Qt.AlignBottom)
        
        self.password = QLineEdit()
        self.password.setPlaceholderText("use LDAP Password")
        self.password.setEchoMode(QLineEdit.EchoMode.Password)
        logindata.addWidget(lblpw)
        logindata.addWidget(self.password)

        #Buttons
        loginbtn = QPushButton("Login")
        loginbtn.setFixedSize(QSize(400,40))
        loginbtn.setContentsMargins(20,20,20,20)
        loginbtn.setIconSize(QSize(25,25))
        loginbtn.clicked.connect(self.the_button_was_clicked)
        
        logindata.addWidget(loginbtn)

        widget = QWidget()

        layout.addLayout(logindata)
        widget.setLayout(layout)
        

        self.setCentralWidget(widget)



        # Set the central widget of the Window.
        

    


    def the_button_was_clicked(self,s):
        
        sessions = connect_and_login(self.username.text(),self.password.text())
        print(sessions._transport.authenticated)
        
        if sessions._transport.authenticated == False:

            button = QMessageBox.critical(
                self,"Authentication",
                "Authentication error",
                buttons=QMessageBox.Discard | QMessageBox.NoToAll | QMessageBox.Ignore,
                defaultButton=QMessageBox.Discard,
            )

            if button == QMessageBox.Discard:
                print("Discard!")
                sessions.close()
            elif button == QMessageBox.NoToAll:
                print("No to all!")
            else:
                print("Ignore!")
        else:
            print("Login successfull")
            print(sessions)
            execute_command(sessions,"ls -la")
            



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()



