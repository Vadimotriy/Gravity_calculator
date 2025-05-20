import sys

from PyQt6.QtWidgets import QApplication
from menu import TheLawOfUniversalGravitation

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = TheLawOfUniversalGravitation()
    MainWindow.show()
    sys.exit(app.exec())