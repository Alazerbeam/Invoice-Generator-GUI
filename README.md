# Automated Invoice Generator GUI

A simple, Tkinter-based tool for generating invoices from customer data stored in a CSV file. From a GUI, you may select one or multiple customers from a list and automatically generate their invoices as pdfs. 

# Features

- Load client data directly from a CSV file
- Scrollable list with live search and filter
- "Select All" and "Deselect All" buttons for batch operations
- Cross-platform scroll wheel support (Windows, macOS, Linux)
- Easily configurable directories and constants via `config.py`

# Demo

Coming soon.

# Project Structure

| Folder / File | Description |
|----------------|-------------|
| `data/sales.csv` | Example CSV file which contains 5 customers each having up to 2 purchases. |
| `data/sales2.csv` | Larger example CSV file containing 50 customers each having up to 3 purchases. |
| `images/generic_logo.png` | A generic company logo to put on the invoice pdfs. |
| `invoices/` | The output folder to contain all generated invoice pdfs. |
| `src/config.py` | Contains configuration constants such as directory paths and file templates. |
| `src/generate_example_csv.py` | Generates a new random CSV file with 50 customers, each having up to 3 purchases. |
| `src/generate_invoice.py` | Core logic for reading client data, generating PDFs, and formatting invoices. |
| `src/gui.py` | Entry point of the application. Launches the Tkinter GUI and handles user interactions. |
| `LICENSE.txt` | Licensing terms and conditions for use of this project. |
| `README.md` | Project overview, setup instructions, and usage guide. |
| `requirements.txt` | Python library requirements to successfully run this project. |

# Setup Instructions

1. Clone the repository.

```
git clone https://github.com/Alazerbeam/Invoice-Generator-GUI.git
cd Invoice-Generator-GUI
```

2. Create and activate virtual environment (optional but recommended).

```
python -m venv .venv
source .venv/bin/activate   # (for macOS/linux)
.venv\Scripts\activate      # (for Windows)
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the app

```
python gui.py
```

# Configuration

Modify `config.py` to match the directories, csv files, and images that you want to use. 

# How It Works

1. Creates the output folder `invoices` if it doesn't already exist.

2. Reads customer data from the provided csv file.

3. Creates list of unique customer names, and maps each customer name to their corresponding invoice ID.

4. Builds the GUI, including dynamic search bar, "Select All"/"Deselect All" buttons, scrollable checklist, and "Generate Invoices" button.

5. Upon selecting the desired customers and clicking the "Generate Invoices" button, a pdf of an invoice for each selected customer will be created and placed in the `invoices` folder.

# Example CSV Format

See `data/sales.csv` for a short example of the format your own CSV file should follow.

# Potential Improvements

- More advanced filtering (by city, date, etc.)
- Automatically email the invoice to the customer

# License & Usage

This repository is part of my consulting and portfolio work. 
The code is shared publicly for demonstration purposes only.
Please do not reuse or distribute without permission.


## © 2025 Adam Lizerbram / AML Software Consulting. All rights reserved.

