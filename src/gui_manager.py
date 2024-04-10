import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from src.GuiForm import Ui_MainWindow


class PageGUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = PageGUI()
    widget.show()
    sys.exit(app.exec())


