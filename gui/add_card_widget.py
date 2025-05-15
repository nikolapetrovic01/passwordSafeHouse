from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt


class AddCardWidget(QWidget):
    def __init__(self, on_click_callback):
        super().__init__()
        self.setFixedSize(150,150)
        
        #Outer layout
        outer_layout = QVBoxLayout(self)
        outer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        outer_layout.setContentsMargins(0,0,0,0)
        
        # Inner card box
        card_box = QWidget()
        card_box.setFixedSize(130,130)
        card_box.setStyleSheet("""
            QWidget {                   
            background-color: #f5f5f5;
            border: 1px solid #ccc;
            border-radius: 10px;
            }
            QWidget:hover {
                background-color: #e0e0e0;
                border: 1px solid #999;
            }
        """)

        card_layout = QVBoxLayout(card_box)
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.setContentsMargins(10, 10, 10, 10)
        card_layout.setSpacing(5)

        # Plus icon
        plus_label = QLabel("+")
        plus_label.setStyleSheet("font-size: 32px; color: #555; background: none; border: none;")
        plus_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Text label
        text_label = QLabel("Dodaj Novi")
        text_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        text_label.setStyleSheet("font-size: 12px; color: #333; background: none; border: none;")

        # Add into card box
        card_layout.addWidget(plus_label)
        card_layout.addWidget(text_label)

        # Add full card box into the full tile
        outer_layout.addWidget(card_box)

        self.mousePressEvent = lambda event: on_click_callback()