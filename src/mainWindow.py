from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QMainWindow, QMessageBox
from ui.ui_mainwindow import Ui_MainWindow
import resources.rc_resource

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.actionExit.triggered.connect(self.exitWindow)

        self.ui.actionAbout.triggered.connect(self.openAboutWindow)

        self.add_pokemon()

        self.setFixedSize(750, 480)

        self.ui.comboBox_Pokemon_Names.setCurrentIndex(6)

        squirtle_image = QPixmap(":/pokemon_images/pokemon_images/Squirtle.png")
        self.ui.label_Pokemon_Image.setPixmap(squirtle_image)
        self.ui.label_Pokemon_Image.setScaledContents(True)

        self.ui.comboBox_Pokemon_Names.currentIndexChanged.connect(self.change_Pokemon_Image)
    
    def exitWindow(self):
        self.close()
    
    def openAboutWindow(self):
        title = "About"
        text = "Pokemon Gen 3 Starter Manip v1.0\nCreated by MKDasher and JP_Xinnam\nPorted by HunarPG"
        message = QMessageBox()
        message.information(self, title, text)
    
    def add_pokemon(self):
        with open("database/pokemon.txt", "r") as f:
            for line in f:
                line = line.strip("\n")
                self.ui.comboBox_Pokemon_Names.addItem(line)
    
    def change_Pokemon_Image(self):
        self.image = QPixmap(":/pokemon_images/pokemon_images/" + self.ui.comboBox_Pokemon_Names.currentText() + ".png")
        self.ui.label_Pokemon_Image.setPixmap(self.image)
        self.ui.label_Pokemon_Image.setScaledContents(True)
