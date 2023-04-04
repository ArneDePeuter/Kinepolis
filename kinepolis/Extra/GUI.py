from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


def addLabel(win, text, x, y, w, h):
    label = QtWidgets.QLabel(win)
    label.move(x, y)
    label.setFixedWidth(w)
    label.setFixedHeight(h)
    label.setText(text)
    return label


def addButton(win, text, x, y, w, h):
    button = QtWidgets.QPushButton(win)
    button.move(x, y)
    button.setFixedWidth(w)
    button.setFixedHeight(h)
    button.setText(text)
    return button


class Screen:
    def __init__(self, gui) -> None:
        self.gui = gui
        self.win = gui.win
        self.width, self.height = self.gui.width, self.gui.height
        self.objects = []

    def show(self):
        for ob in self.objects:
            ob.show()

    def hide(self):
        for ob in self.objects:
            ob.hide()


class AboutScreen(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.initObjects()
        self.show()

    def initObjects(self):
        pass


class ScreeningsScreen(Screen):
    def __init__(self, gui) -> None:
        super().__init__(gui)
        self.initObjects()
        self.show()

    def initObjects(self):
        pass


class LoginScreen(Screen):
    def __init__(self, gui) -> None:
        super().__init__(gui)
        self.initObjects()
        self.show()

    def initObjects(self):
        newbutton = addButton(self.win, "Hey", 500, 500, 100, 100)
        newbutton.show()

        self.objects.append(newbutton)


class Homepage(Screen):
    def __init__(self, gui) -> None:
        super().__init__(gui)
        self.initObjects()
        self.show()

    def loginScreen(self):
        self.hide()
        self = LoginScreen(self.gui)

    def screeningScreen(self):
        self.hide()
        self = ScreeningsScreen(self.gui)

    def aboutScreen(self):
        self.hide()
        self = AboutScreen(self.gui)

    def initObjects(self):
        title = addLabel(self.win, "Homepage", 100, 0, 100, 100)
        welcome = addLabel(
            self.win,
            "WELCOME",
            self.width // 4,
            self.height // 3,
            self.width // 2,
            self.height // 20,
        )

        loginButton = addButton(
            self.win,
            "Reserveer",
            self.width // 4,
            self.height // 2,
            self.width // 2,
            self.height // 20,
        )
        loginButton.clicked.connect(self.loginScreen)

        screeningsButton = addButton(
            self.win,
            "Screenings",
            self.width // 4,
            self.height // 2 + self.height // 20,
            self.width // 2,
            self.height // 20,
        )
        screeningsButton.clicked.connect(self.screeningScreen)

        aboutButton = addButton(
            self.win,
            "About",
            self.width // 4,
            self.height // 2 + self.height // 10,
            self.width // 2,
            self.height // 20,
        )
        aboutButton.clicked.connect(self.aboutScreen)

        self.objects.append(title)
        self.objects.append(welcome)
        self.objects.append(loginButton)
        self.objects.append(screeningsButton)
        self.objects.append(aboutButton)


class GUI:
    def __init__(self, xpos, ypos, width, height) -> None:
        app = QApplication(sys.argv)
        self.width, self.height = width, height
        self.win = QMainWindow()
        self.win.setGeometry(xpos, ypos, width, height)
        self.win.setWindowTitle("Kinepolis")
        self.win.show()
        self.screen = Homepage(self)
        sys.exit(app.exec_())


GUI(460, 40, 1000, 1000)
