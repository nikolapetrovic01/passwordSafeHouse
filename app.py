# app.py
import sys
from PyQt6.QtWidgets import QApplication
from gui.main_window import MainWindow

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.move(100, 100)
    window.show()
    sys.exit(app.exec())
