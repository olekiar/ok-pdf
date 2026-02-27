# ok-pdf

A simple PDF merger tool with a graphical user interface (GUI), written in Python using PyQt6 and pypdf. It lets you pick multiple PDF files, automatically sorts them alphabetically by filename, and merges them into a single output file called `merged.pdf`.

---

## Features

- GUI built with **PyQt6** – no command-line knowledge required
- Automatically **sorts** selected PDFs by filename before merging
- Saves the merged result as **`merged.pdf`** in the same directory as the first sorted file
- Displays a clear status message and dialog on success or failure

---

## Prerequisites

- **Python 3.8+**
- **pip** (comes bundled with most Python installations)

---

## Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/olekiar/ok-pdf.git
   cd ok-pdf
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   This installs:
   | Package | Version |
   |---------|---------|
   | PyQt6   | ≥ 6.4.0 |
   | pypdf   | ≥ 3.0.0 |

---

## Usage

Run the application with:

```bash
python pdf_merger.py
```

A window will open with the following workflow:

1. **Select PDF Files** – Click the *Select PDF Files* button to open a file dialog. You can select one or more PDF files at once.
2. **Review the list** – The selected files are displayed in the list area. After clicking *Merge PDFs* they will be sorted alphabetically by filename.
3. **Merge** – Click the *Merge PDFs* button. The tool will:
   - Sort all selected files by their filename.
   - Merge them in that order into a single PDF.
   - Save the result as `merged.pdf` in the same folder as the first file in the sorted list.
4. **Confirmation** – A success dialog will show the full path of the merged file. If anything goes wrong (e.g. a corrupted PDF or a permissions error), an error dialog will describe the problem.

---

## License

This project is licensed under the terms of the [LICENSE](LICENSE) file included in this repository.
