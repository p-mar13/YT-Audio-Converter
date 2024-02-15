from PyQt5.QtWidgets import (QWidget, QInputDialog, QLineEdit, 
                             QLabel, QVBoxLayout, QPushButton)
from get_audio import Download


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title  = 'YouTube->MP3 converter'
        self.left   = 50
        self.top    = 50
        self.width  = 640
        self.height = 480

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.label = QLabel()
        self.label.setStyleSheet("color: green; font: 16px;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(QPushButton("Convert YT video through link", clicked=self.getText))
        self.setLayout(layout)        
        self.show()   

    def getText(self):  

        userInput, okPressed = QInputDialog.getText(
                self, 
                "Convert your YT video to MP3", 
                "Link:", 
                QLineEdit.Normal, "")
        if okPressed:                      
            if userInput.strip():
                result, file_name = Download(str(userInput))
                if result==True:
                    self.label.setText("File "+str(file_name)+".mp3 is ready for using.")
                else:
                    self.label.setText("An error has occured")
            else:
                self.label.setStyleSheet("color: red; font: 24px;")
                self.label.setText("Input line is empty, enter valid YT link")
        else:
            self.label.setText("")