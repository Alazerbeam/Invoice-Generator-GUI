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

Under the `data` folder, there are example csv files. `sales.csv` contains only a few entries (5 customers with up to 2 purchases each) for testing and simplicity. `sales2.csv` contains much more data (50 customers with up to 3 purchases each).

Under the `images` folder, there is an example logo to put on the invoices.

The `invoices` folder is the output folder from running the program. All generated invoices are placed in this folder.

The `src` folder contains all source code files.

[insert table here explaining each script]

# Setup Instructions

1. Clone the repository.

git clone [repo link]
cd [repo name]

2. Create and activate virtual environment (optional but recommended).

python -m venv .venv
source .venv/bin/activate   (for macOS/linux)
.venv\Scripts\activate      (for Windows)

3. Install dependencies

pip install -r requirements.txt

4. Run the app

python gui.py

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