import os
import sys

from PyQt6.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox

from uic import app
from unitypackage_extractor import extractor


class UnityPackageExtractorUi(QMainWindow, app.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.files = None
        self.setupUi(self)

        self.btnExtract.setEnabled(False)
        self.filenames = None
        self.dirName = "Extracteds"

        self.inputs()

    def inputs(self):
        self.btnExtract.clicked.connect(self.extract)
        self.btnOpenDest.clicked.connect(self.getDir)
        self.btnOpenFile.clicked.connect(self.getFile)

    def getFile(self):
        self.filenames, _filter = QFileDialog.getOpenFileNames(
            self, "Choisir le fichier à extraire", filter="*.unitypackage"
        )
        if self.filenames:
            self.files = "\n".join(self.filenames)
            self.filesNames.setText(self.files)
            self.btnExtract.setEnabled(True)

    def getDir(self):
        self.dirName = QFileDialog.getExistingDirectory(
            self, "Choisir le repertoire de destination"
        )
        if self.dirName:
            self.lineDest.setText(self.dirName)

    def extract(self):
        try:
            for file in self.filenames:
                extractor.extractPackage(
                    file, self.dirName,
                )
                if self.ckSuppr:
                    os.remove(file)
        except Exception as e:
            show_invalid_files_error(self, e)


def show_invalid_files_error(self, e):
    QMessageBox.critical(
        self,
        "Erreur",
        "Les fichiers ne sont pas valides.\n\n%s" % e,
    )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    upe = UnityPackageExtractorUi()
    upe.show()
    sys.exit(app.exec())
