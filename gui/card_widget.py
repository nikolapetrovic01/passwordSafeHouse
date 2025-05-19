from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class CardWidget(QWidget):
    def __init__(self, cred, on_click_callback):
        super().__init__()

        self.cred = cred
        self.setFixedSize(150, 150)  # Full square card

        # Main layout for this card
        outer_layout = QVBoxLayout(self)
        outer_layout.setContentsMargins(0, 0, 0, 0)
        outer_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Inner widget to style as the "card"
        card_box = QWidget()
        card_box.setFixedSize(130, 130)

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

        card_box.setAttribute(Qt.WidgetAttribute.WA_Hover, True)

        card_layout = QVBoxLayout(card_box)
        card_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        card_layout.setContentsMargins(10, 10, 10, 10)
        card_layout.setSpacing(5)

        # Icon
        icon_label = QLabel()
        icon_label.setFixedSize(64, 64)
        icon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        icon_label.setStyleSheet("background: none; border: none;")

        pixmap = QPixmap(cred["icon"])
        if not pixmap.isNull():
            icon_label.setPixmap(
                pixmap.scaled(48, 48, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            )

        # Label
        name_label = QLabel(cred["name"])
        name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        name_label.setStyleSheet("background: none; border: none;")

        card_layout.addWidget(icon_label)
        card_layout.addWidget(name_label)

        # Add the styled box to the full card
        outer_layout.addWidget(card_box)

        # Handle clicks
        self.mousePressEvent = lambda event: on_click_callback(self.cred)