from PySide2 import QtWidgets, QtCore, QtGui
from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

def get_mayaWindow():
    main_window_ptr = omui.MQtUtil.mainWindow()
    return wrapInstance(int(main_window_ptr), QtWidgets.QMainWindow)

class ValentineWindow(QtWidgets.QDialog):
    def __init__(self, parent=get_mayaWindow()):
        super(ValentineWindow, self).__init__(parent)

        self.setWindowTitle("Valentine Question")
        self.setWindowFlags(QtCore.Qt.Window)

        self.label = QtWidgets.QLabel("Will you be my valentine?")
        self.label.setFont(QtGui.QFont("Courier New", 24))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("""
            background-color: pink;
            color: red;
            border-style: outset;
            border-width: 5px;
            border-radius: 10px;
            border-color: red;
            padding: 30px;
        """)

        self.yes_button = QtWidgets.QPushButton("Yes")
        self.yes_button.setFont(QtGui.QFont("Courier New", 16))
        self.yes_button.setStyleSheet("background-color: red; color: white;")

        self.no_button = QtWidgets.QPushButton("No")
        self.no_button.setFont(QtGui.QFont("Comic Sans MS", 10))
        self.no_button.setStyleSheet("background-color: #bfbebe; color: #eae7e7; padding: 6px;")

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.label)
        layout.addWidget(self.yes_button)
        layout.addWidget(self.no_button)

        self.yes_button.clicked.connect(self.on_yes_clicked)
        self.no_button.clicked.connect(self.on_no_clicked)

    def on_yes_clicked(self):
        self.label.setText("I love you!")
        self.label.setStyleSheet("background-color: pink; color: red; border-style: outset; border-width: 5px; border-radius: 10px; border-color: red; padding: 30px;")
        QtCore.QTimer.singleShot(2000, self.close)

    def on_no_clicked(self):
        self.label.setText("LMAO!!")
        self.label.setStyleSheet("background-color: pink; color: black; border-style: outset; border-width: 5px; border-radius: 10px; border-color: red; padding: 30px;")
        QtCore.QTimer.singleShot(500, lambda: self.label.setText("Will you be my valentine?"))

def show_valentine_window():
    global valentine_win
    try:
        valentine_win.close()
        valentine_win.deleteLater()
    except:
        pass

    valentine_win = ValentineWindow()
    valentine_win.show()

show_valentine_window()
