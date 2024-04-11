import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog
from src.GuiForm import Ui_MainWindow
from src.backup import BackupSystem


class PageGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.setWindowTitle('File Manager')

        self.ui.destination_button.clicked.connect(self.open_file_dialog)
        self.ui.source_button.clicked.connect(self.open_file_dialog_source)
        self.ui.copy_button.clicked.connect(self.copy_method)
        self.ui.move_button.clicked.connect(self.move_method)

    def move_method(self):
        move = BackupSystem()
        move.set_name('MoveSystem')
        move.set_source(self.ui.source_edit.text())
        move.set_destination(self.ui.destination_edit.text())
        print(move.move_exec())

    def copy_method(self):
        copy = BackupSystem()
        copy.set_name('CopySystem')
        copy.set_source(self.ui.source_edit.text())
        copy.set_destination(self.ui.destination_edit.text())
        print(copy.copy_exec())

    def open_file_dialog(self):
        options = QFileDialog.Options()
        directory_path = QFileDialog.getExistingDirectory(self, "Choisir un dossier", options=options)
        if directory_path:
            print("Chemin du dossier sélectionné:", directory_path)
            self.ui.destination_edit.setText(str(directory_path))

    def open_file_dialog_source(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Choisir un fichier", "", "All Files (*);;Python Files (*.py)",
                                                  options=options)
        if fileName:
            print("Nom du fichier sélectionné:", fileName)
            self.ui.source_edit.setText(str(fileName))
