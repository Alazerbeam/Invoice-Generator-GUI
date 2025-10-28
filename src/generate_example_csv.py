import pandas as pd
import random
from datetime import datetime, timedelta

# Base customer data
first_names = ["Alice","Bob","Carol","David","Eva","Frank","Grace","Hannah","Ian","Jane",
               "Kevin","Laura","Mike","Nina","Oscar","Paula","Quinn","Rachel","Steve","Tina",
               "Uma","Victor","Wendy","Xander","Yara","Zane","Aaron","Bella","Cody","Diana",
               "Ethan","Fiona","George","Holly","Ivan","Julia","Kyle","Lily","Matt","Nora",
               "Owen","Paige","Quentin","Rose","Sam","Tracy","Ulysses","Vera","Will","Yvonne"]
last_names = ["Smith","Johnson","Lee","Miller","Brown","Davis","Wilson","Moore","Taylor","Anderson",
              "Thomas","Jackson","White","Harris","Martin","Thompson","Garcia","Martinez","Robinson","Clark",
              "Lewis","Walker","Hall","Allen","Young","King","Wright","Scott","Torres","Nguyen",
              "Hill","Flores","Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell",
              "Carter","Roberts","Gomez","Phillips","Evans","Turner","Diaz","Parker","Cruz","Edwards"]

# Fixed unit prices per item
item_prices = {
    "Widget A": 25.0,
    "Widget B": 40.0,
    "Widget C": 15.0,
    "Widget D": 30.0,
    "Widget E": 35.0
}
items = list(item_prices.keys())

# Generate 50 customers
customers = []
emails = []
addresses = []
cities = []
zips = []
for i in range(50):
    first = first_names[i % len(first_names)]
    last = last_names[i % len(last_names)]
    name = f"{first} {last}"
    customers.append(name)
    emails.append(f"{first.lower()}.{last.lower()}@example.com")
    addresses.append(f"{random.randint(100,999)} {random.choice(['Maple','Oak','Pine','Birch','Cedar','Elm'])} Street")
    cities.append(f"{random.choice(['Springfield, IL','Madison, WI','Austin, TX','Denver, CO','Portland, OR','Seattle, WA','Miami, FL'])}")
    zips.append(str(random.randint(10000,99999)))

# Generate invoices
rows = []
invoice_counter = 1
for i in range(50):
    num_items = random.randint(1,3)
    invoice_id = f"INV-{invoice_counter:03d}"
    invoice_counter += 1
    
    customer_data = {
        "Invoice_ID": invoice_id,
        "Customer_Name": customers[i],
        "Email": emails[i],
        "Address": addresses[i],
        "City_State": cities[i],
        "Zip": zips[i]
    }
    
    chosen_items = random.sample(items, num_items)  # pick unique items per invoice
    for item in chosen_items:
        quantity = random.randint(1,5)
        date = (datetime(2025,10,20) + timedelta(days=random.randint(0,10))).strftime("%Y-%m-%d")
        row = {
            **customer_data,
            "Item": item,
            "Quantity": quantity,
            "Unit_Price": item_prices[item],  # fixed per item
            "Date": date
        }
        rows.append(row)

# Save to CSV
df = pd.DataFrame(rows)
df.to_csv("sales2.csv", index=False)
print("Generated sales2.csv with 50 customers; fixed item prices.")
