import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget


class QuickNoteApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('QuickNote')
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.text_edit = QTextEdit(self)
        layout.addWidget(self.text_edit)

        save_button = QPushButton('Save', self)
        save_button.clicked.connect(self.save_note)
        layout.addWidget(save_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def save_note(self):
        with open('quicknote.txt', 'w') as f:
            f.write(self.text_edit.toPlainText())

        self.text_edit.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = QuickNoteApp()
    window.show()

    sys.exit(app.exec())
