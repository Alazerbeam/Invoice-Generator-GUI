import pandas as pd
from generate_invoice import create_invoice_from_id
import os
from pathlib import Path
from config import *

# load csv
df = pd.read_csv(SALES_CSV)

# create output folder
os.makedirs("invoices", exist_ok=True)

# create an invoice for each unique invoice id
for invoice_id in df["Invoice_ID"].unique():
    create_invoice_from_id(df, invoice_id, logo_path=LOGO_PATH)

print("All invoices generated successfully!")
