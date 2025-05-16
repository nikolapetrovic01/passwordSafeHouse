# gui/main_window.py
from PyQt6.QtWidgets import (
    QWidget, QLabel, QVBoxLayout, QGridLayout, 
    QDialog, QDialogButtonBox, QVBoxLayout, QLineEdit, QDialogButtonBox
)
from PyQt6.QtCore import Qt
from gui.CardWidget import CardWidget
from PyQt6.QtGui import QIcon
from gui.add_card_widget import AddCardWidget
from core.storage import load_credentials, save_credentials
from core.models import Credential

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

        # Load credentials from JSON file
        self.credentials: list[Credential] = load_credentials()

        # 🔹 If empty, add some dummy entries (optional)
        # TODO: REMOVE
        if not self.credentials:
            self.credentials = [
                Credential(name="Gmail", icon="gui/icons/gmail.png", username="you@gmail.com", password="abc123"),
                Credential(name="Steam", icon="gui/icons/steam.png", username="gamer123", password="g4m3r"),
                Credential(name="Facebook", icon="gui/icons/facebook.png", username="you.fb", password="fb_pass"),
                Credential(name="GitHub", icon="gui/icons/github.png", username="yougit", password="gh_token")
            ]
        save_credentials(self.credentials)

        # Add regular cards to the grid
        for i, cred in enumerate(self.credentials):
            row = i // 3 # 3 Cards per row
            col = i % 3

            card = CardWidget(cred.__dict__, self.open_card_dialog)
            grid_layout.addWidget(card,row,col)

        # Add the "Add New" card always last
        add_row = len(self.credentials) // 3
        add_col = len(self.credentials) % 3
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
        name_input = QLineEdit()
        name_input.setPlaceholderText("Name")
        layout.addWidget(QLabel("Name"))
        layout.addWidget(name_input)

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
            new_cred = Credential(
                name=name_input.text(),
                username=username_input.text(),
                password=password_input.text(),
                icon=""
            )
            self.credentials.append(new_cred)
            save_credentials(self.credentials)

            grid_layout: QGridLayout = self.layout().itemAt(0).layout()

            # Remove the "+" card from the grid
            add_card_item = grid_layout.itemAtPosition(len(self.credentials) // 3, len(self.credentials) % 3)

            if add_card_item:
                widget = add_card_item.widget()
                if widget:
                    widget.setParent(None)

            # Add the new card
            row = (len(self.credentials) - 1) // 3
            col = (len(self.credentials) - 1) % 3
            new_card = CardWidget(new_cred.__dict__, self.open_card_dialog)
            grid_layout.addWidget(new_card, row, col)

            # Add the "+" card again at the end
            add_row = len(self.credentials) // 3
            add_col = len(self.credentials) % 3
            add_card = AddCardWidget(self.open_add_dialog)
            grid_layout.addWidget(add_card, add_row, add_col)

            dialog.accept()

        buttons.accepted.connect(on_save)
        dialog.setLayout(layout)
        dialog.exec()