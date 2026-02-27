import sys
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout,
                             QPushButton, QFileDialog, QListWidget,
                             QMessageBox, QLabel)
from PyQt6.QtCore import Qt
from pypdf import PdfWriter

class PDFMergerApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Configure the main window
        self.setWindowTitle('PDF Merger Utility')
        self.resize(500, 350)

        # Create the main layout
        layout = QVBoxLayout()

        # Add a descriptive label
        info_label = QLabel("1. Select PDF files\n2. They will be automatically sorted by filename\n3. Click Merge")
        info_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(info_label)

        # Create button to select files
        self.select_btn = QPushButton('Select PDF Files')
        self.select_btn.clicked.connect(self.select_files)

        # Style the button to make it look a bit nicer
        self.select_btn.setStyleSheet("padding: 10px; font-weight: bold;")
        layout.addWidget(self.select_btn)

        # Create a list widget to display selected files
        self.file_list = QListWidget()
        layout.addWidget(self.file_list)

        # Create button to trigger the merge
        self.merge_btn = QPushButton('Merge PDFs')
        self.merge_btn.clicked.connect(self.merge_pdfs)
        self.merge_btn.setStyleSheet("padding: 10px; font-weight: bold; background-color: #4CAF50; color: white;")
        layout.addWidget(self.merge_btn)

        # Status label to show success or errors
        self.status_label = QLabel('')
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.status_label.setWordWrap(True)
        self.status_label.setStyleSheet("color: #555555;")
        layout.addWidget(self.status_label)

        # Set the main layout
        self.setLayout(layout)

    def select_files(self):
        # Open file dialog allowing multiple selection
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "Select PDFs",
            "",
            "PDF Files (*.pdf)"
        )

        if files:
            # Clear previous selections
            self.file_list.clear()
            self.status_label.setText("")

            # Add new selections to the list widget
            for file_path in files:
                self.file_list.addItem(file_path)

    def merge_pdfs(self):
        count = self.file_list.count()

        if count == 0:
            QMessageBox.warning(self, "Warning", "Please select at least one PDF file to merge.")
            return

        # Extract all file paths from the list widget
        file_paths = [self.file_list.item(i).text() for i in range(count)]

        # Sort the file paths specifically by their filename (basename), ignoring the directory path
        file_paths.sort(key=lambda x: os.path.basename(x))

        # Update the list widget to visually show the user the new sorted order
        self.file_list.clear()
        for f in file_paths:
            self.file_list.addItem(f)

        # Determine the output path: 'merged.pdf' in the same directory as the FIRST file in the sorted list
        output_dir = os.path.dirname(file_paths[0])
        output_path = os.path.join(output_dir, 'merged.pdf')

        try:
            self.status_label.setText("Merging... please wait.")
            QApplication.processEvents()  # Update GUI before heavy lifting

            # Initialize the PDF writer
            merger = PdfWriter()

            # Append all sorted PDFs to the writer
            for pdf in file_paths:
                merger.append(pdf)

            # Write out the merged PDF
            with open(output_path, "wb") as f_out:
                merger.write(f_out)

            # Notify the user of success
            success_msg = f"Success! Merged file saved to:\n{output_path}"
            self.status_label.setText(success_msg)
            QMessageBox.information(self, "Success", success_msg)

        except Exception as e:
            # Handle permissions errors, corrupted PDFs, etc.
            error_msg = f"An error occurred during merging:\n{str(e)}"
            self.status_label.setText("Merge failed.")
            QMessageBox.critical(self, "Error", error_msg)

if __name__ == '__main__':
    # Initialize the PyQt application
    app = QApplication(sys.argv)

    # Create and show the main window
    ex = PDFMergerApp()
    ex.show()

    # Start the event loop
    sys.exit(app.exec())
