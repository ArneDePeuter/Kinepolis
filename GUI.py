from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def addLabel(win, text, x, y, w, h):
    label = QtWidgets.QLabel(win)
    label.setText(text)
    label.setFixedWidth(w)
    label.setFixedHeight(h)
    label.move(x,y)
    return label
    
def addButton(win, text, x, y, w, h):
    button = QtWidgets.QPushButton(win)
    button.setText(text)
    button.move(x, y)
    button.setFixedWidth(w)
    button.setFixedHeight(h)
    return button

class GUI:
    def __init__(self, gui, xpos, ypos, width, height) -> None:
        pass

    def go_homepage(self):
        Homepage(self)

class Homepage:
    def __init__(self, gui, xpos, ypos, width, height) -> None:
        app = QApplication(sys.argv)
        win = QMainWindow()
        win.setGeometry(xpos, ypos, width, height)
        win.setWindowTitle("Kinepolis")

        title = self.addLabel("Homepage", 0, 0, 100, 100)
        loginButton = self.addButton("Log-In", self.win.width()//2, self.win.height()//2, self.win.width()//10, self.win.height()//10)
        loginButton.clicked.connect(gui.login)
        self.win.show()

        sys.exit(app.exec_())

    def homepage(self):
        pass
        
GUI(200,200,500,500)