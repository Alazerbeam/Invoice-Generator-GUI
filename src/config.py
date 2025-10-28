from pathlib import Path

# define directories
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
INVOICE_DIR = BASE_DIR / "invoices"
IMAGE_DIR = BASE_DIR / "images"

SALES_CSV = DATA_DIR / "sales2.csv"
LOGO_PATH = IMAGE_DIR / "generic_logo.png"