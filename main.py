import os
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog

from uic import app
from unitypackage_extractor import extractor


class UnityPackageExtractorUi(QMainWindow, app.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btnExtract.setEnabled(False)
        self.filename = None
        self.dirName = None

        self.inputs()

    def inputs(self):
        self.btnExtract.clicked.connect(self.extract)
        self.btnOpenDest.clicked.connect(self.getDir)
        self.btnOpenFile.clicked.connect(self.getFile)

    def getFile(self):
        self.filename, _filter = QFileDialog.getOpenFileName(
            self, "Choisir le fichier à extraire", filter="*.unitypackage"
        )
        if self.filename:
            self.lineFile.setText(self.filename)
            self.btnExtract.setEnabled(True)

    def getDir(self):
        self.dirName = QFileDialog.getExistingDirectory(
            self, "Choisir le repertoire de destination"
        )
        if self.dirName:
            self.lineDest.setText(self.dirName)

    def extract(self):
        extractor.extractPackage(
            self.filename, self.dirName
        )
        if self.ckSuppr:
            os.remove(self.filename)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    upe = UnityPackageExtractorUi()
    upe.show()
    sys.exit(app.exec())
