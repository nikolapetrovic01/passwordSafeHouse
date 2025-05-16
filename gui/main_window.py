# gui/main_window.py
from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QGridLayout, 
    QDialog, QDialogButtonBox, QVBoxLayout, QLineEdit, QDialogButtonBox
)
from PyQt6.QtCore import Qt
from gui.CardWidget import CardWidget
from PyQt6.QtGui import QIcon
from gui.add_card_widget import AddCardWidget

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

        # Add regular cards to the grid
        for i, cred in enumerate(credentials):
            row = i // 3 # 3 Cards per row
            col = i % 3

            card = CardWidget(cred, self.open_card_dialog)
            grid_layout.addWidget(card,row,col)

        # Add the "Add New" card always last
        add_row = len(credentials) // 3
        add_col = len(credentials) % 3
        add_card = AddCardWidget(self.open_add_dialog)
        grid_layout.addWidget(add_card, add_row, add_col)

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

    def open_add_dialog(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("Dodaj novu karticu")
        dialog.resize(300,200)

        layout = QVBoxLayout()
        # Input fields
        username_input = QLineEdit()
        username_input.setPlaceholderText("Username")
        layout.addWidget(QLabel("Username"))
        layout.addWidget(username_input)

        password_input = QLineEdit()
        password_input.setPlaceholderText("Password")
        password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(QLabel("Password"))
        layout.addWidget(password_input)

        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Save)
        layout.addWidget(buttons)

        # When Save is pressed
        def on_save():
            print("Username:", username_input.text())
            print("Password:", password_input.text())
            dialog.accept()
        
        buttons.accepted.connect(on_save)
        dialog.setLayout(layout)
        dialog.exec()