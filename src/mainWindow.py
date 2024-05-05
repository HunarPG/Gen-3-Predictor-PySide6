from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionExit.triggered.connect(self.exitWindow)

        self.ui.actionAbout.triggered.connect(self.openAboutWindow)

        self.add_pokemon()

        self.setFixedSize(750, 480)
    
    def exitWindow(self):
        self.close()
    
    def openAboutWindow(self):
        title = "About"
        text = "Pokemon Gen 3 Starter Manip v1.0\nCreated by MKDasher and JP_Xinnam\nPorted by HunarPG"
        dialog = QMessageBox.information(self, title, text)
    
    def add_pokemon(self):
        with open("database/pokemon.txt", "r") as f:
            for line in f:
                line = line.strip("\n")
                self.ui.comboBox_Pokemon_Names.addItem(line)
