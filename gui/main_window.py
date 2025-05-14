# gui/main_window.py
from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QGridLayout,
    QPushButton, QDialog, QDialogButtonBox, QVBoxLayout
)
from PyQt6.QtCore import Qt
from gui.CardWidget import CardWidget
from PyQt6.QtGui import QIcon

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Safe House")
        self.setWindowIcon(QIcon("gui/icons/safeAppIcon.png"))  # <-- Custom icon
        self.resize(800,600)

        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(main_layout)
        
        grid_layout = QGridLayout()
        main_layout.addLayout(grid_layout)

        # Dummy credentials for now
        credentials = [
            {"name": "Gmail", "icon": "gui/icons/gmail.png", "username": "you@gmail.com", "password": "abc123"},
            {"name": "Steam", "icon": "gui/icons/steam.png", "username": "gamer123", "password": "g4m3r"},
            {"name": "Facebook", "icon": "gui/icons/facebook.png", "username": "you.fb", "password": "fb_pass"},
            {"name": "GitHub", "icon": "gui/icons/github.png", "username": "yougit", "password": "gh_token"}
        ]

        # Add cards to the grid
        for i, cred in enumerate(credentials):
            row = i // 3 # 3 Cards per row
            col = i % 3

            card = CardWidget(cred, self.open_card_dialog)
            grid_layout.addWidget(card,row,col)
    
    def open_card_dialog(self, cred):
        dialog = QDialog(self)
        dialog.setWindowTitle(cred["name"])
        dialog.resize(300,200)

        layout = QVBoxLayout()
        layout.addWidget(QLabel(f"Username: {cred['username']}"))
        layout.addWidget(QLabel(f"Password: {cred['password']}"))
        
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok)
        buttons.accepted.connect(dialog.accept)
        layout.addWidget(buttons)

        dialog.setLayout(layout)
        dialog.exec()