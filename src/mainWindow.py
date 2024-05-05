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

        self.ui.pushButton_Check_All_Nature.clicked.connect(self.check_all_clicked)

        self.ui.pushButton_UnCheck_All_Nature.clicked.connect(self.uncheck_all_clicked)

        self.ui.pushButton_Clear_Constrain.clicked.connect(self.clear_constratin_clicked)

        self.ui.pushButton_Clear_TID.clicked.connect(self.clear_tid_clicked)

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
        self.image = QPixmap(":/pokemon_images/pokemon_images/"+ self.ui.comboBox_Pokemon_Names.currentText()+ ".png")
        self.ui.label_Pokemon_Image.setPixmap(self.image)
        self.ui.label_Pokemon_Image.setScaledContents(True)

    def check_all_clicked(self):
        self.ui.checkBox_Nature_Hardy.setChecked(True)
        self.ui.checkBox_Nature_Lonely.setChecked(True)
        self.ui.checkBox_Nature_Brave.setChecked(True)
        self.ui.checkBox_Nature_Adamant.setChecked(True)
        self.ui.checkBox_Nature_Naughty.setChecked(True)
        self.ui.checkBox_Nature_Bold.setChecked(True)
        self.ui.checkBox_Nature_Docile.setChecked(True)
        self.ui.checkBox_Nature_Relaxed.setChecked(True)
        self.ui.checkBox_Nature_Impish.setChecked(True)
        self.ui.checkBox_Nature_Lax.setChecked(True)
        self.ui.checkBox_Nature_Timid.setChecked(True)
        self.ui.checkBox_Nature_Hasty.setChecked(True)
        self.ui.checkBox_Nature_Serious.setChecked(True)
        self.ui.checkBox_Nature_Jolly.setChecked(True)
        self.ui.checkBox_Nature_Naive.setChecked(True)
        self.ui.checkBox_Nature_Modest.setChecked(True)
        self.ui.checkBox_Nature_Mild.setChecked(True)
        self.ui.checkBox_Nature_Quiet.setChecked(True)
        self.ui.checkBox_Nature_Bashful.setChecked(True)
        self.ui.checkBox_Nature_Rash.setChecked(True)
        self.ui.checkBox_Nature_Calm.setChecked(True)
        self.ui.checkBox_Nature_Gentle.setChecked(True)
        self.ui.checkBox_Nature_Sassy.setChecked(True)
        self.ui.checkBox_Nature_Careful.setChecked(True)
        self.ui.checkBox_Nature_Quirky.setChecked(True)

    def uncheck_all_clicked(self):
        self.ui.checkBox_Nature_Hardy.setChecked(False)
        self.ui.checkBox_Nature_Lonely.setChecked(False)
        self.ui.checkBox_Nature_Brave.setChecked(False)
        self.ui.checkBox_Nature_Adamant.setChecked(False)
        self.ui.checkBox_Nature_Naughty.setChecked(False)
        self.ui.checkBox_Nature_Bold.setChecked(False)
        self.ui.checkBox_Nature_Docile.setChecked(False)
        self.ui.checkBox_Nature_Relaxed.setChecked(False)
        self.ui.checkBox_Nature_Impish.setChecked(False)
        self.ui.checkBox_Nature_Lax.setChecked(False)
        self.ui.checkBox_Nature_Timid.setChecked(False)
        self.ui.checkBox_Nature_Hasty.setChecked(False)
        self.ui.checkBox_Nature_Serious.setChecked(False)
        self.ui.checkBox_Nature_Jolly.setChecked(False)
        self.ui.checkBox_Nature_Naive.setChecked(False)
        self.ui.checkBox_Nature_Modest.setChecked(False)
        self.ui.checkBox_Nature_Mild.setChecked(False)
        self.ui.checkBox_Nature_Quiet.setChecked(False)
        self.ui.checkBox_Nature_Bashful.setChecked(False)
        self.ui.checkBox_Nature_Rash.setChecked(False)
        self.ui.checkBox_Nature_Calm.setChecked(False)
        self.ui.checkBox_Nature_Gentle.setChecked(False)
        self.ui.checkBox_Nature_Sassy.setChecked(False)
        self.ui.checkBox_Nature_Careful.setChecked(False)
        self.ui.checkBox_Nature_Quirky.setChecked(False)
    
    def clear_constratin_clicked(self):
        self.ui.lineEdit_HP_IV.clear()
        self.ui.lineEdit_Minus_Attack_IV.clear()
        self.ui.lineEdit_Minus_Defense_IV.clear()
        self.ui.lineEdit_Minus_Special_Attack_IV.clear()
        self.ui.lineEdit_Minus_Special_Defense_IV.clear()
        self.ui.lineEdit_Minus_Speed_IV.clear()
        self.ui.lineEdit_Neutral_Attack_IV.clear()
        self.ui.lineEdit_Neutral_Defense_IV.clear()
        self.ui.lineEdit_Neutral_Special_Attack_IV.clear()
        self.ui.lineEdit_Neutral_Special_Defense_IV.clear()
        self.ui.lineEdit_Neutral_Speed_IV.clear()
        self.ui.lineEdit_Plus_Attack_IV.clear()
        self.ui.lineEdit_Plus_Defense_IV.clear()
        self.ui.lineEdit_Plus_Special_Attack_IV.clear()
        self.ui.lineEdit_Plus_Special_Defense_IV.clear()
        self.ui.lineEdit_Plus_Speed_IV.clear()
    
    def clear_tid_clicked(self):
        self.ui.lineEdit_Trainer_ID.clear()
