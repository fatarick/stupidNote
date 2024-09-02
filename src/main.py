from PyQt6.QtWidgets import QApplication, QPushButton, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt6.QtCore import Qt

class Window(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Stupid Note")
        self.resize(1280, 720)
        
        # Create widgets
        self.line_edit = QLineEdit(parent=self)  # Renamed to avoid conflict with built-in function 'input'
        save_button = QPushButton("Save", parent=self)
        exit_button = QPushButton("Exit", parent=self)
        
        # Connect the save button to the save function
        save_button.clicked.connect(self.save_file)

        # Create layouts
        main_layout = QVBoxLayout()
        button_layout = QHBoxLayout()

        # Add widgets to layouts
        main_layout.addWidget(self.line_edit, alignment=Qt.AlignmentFlag.AlignTop)
        self.line_edit.setFixedSize(1280, 600)
        
        # Add buttons to the horizontal layout
        button_layout.addWidget(save_button)
        button_layout.addWidget(exit_button)
        
        # Add the horizontal layout to the main vertical layout
        main_layout.addLayout(button_layout)

        # Set the main layout for the window
        self.setLayout(main_layout)

        # Set fixed size for buttons
        save_button.setFixedSize(640, 150)
        exit_button.setFixedSize(640, 150)

        # Connect the exit button to close the application
        exit_button.clicked.connect(self.close)

    def save_file(self):
        # Open a dialog to get the save file name from the user
        file_name, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Text Files (*.txt);;All Files (*)")
        
        if file_name:  # Check if the user provided a file name
            try:
                # Open the file in write mode and save the content of QLineEdit to the file
                with open(file_name, 'w') as file:
                    text_to_save = self.line_edit.text()  # Access the text from the QLineEdit widget
                    file.write(text_to_save)
                    print(f"File saved: {file_name}")
            except Exception as e:
                print(f"Error saving file: {e}")

app = QApplication([])
window = Window()
window.show()
app.exec()
