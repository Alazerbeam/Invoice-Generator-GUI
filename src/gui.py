import pandas as pd
import os
import tkinter as tk
from tkinter import messagebox
from config import *
from generate_invoice import create_invoice_from_id

os.makedirs("invoices", exist_ok=True)

df = pd.read_csv(SALES_CSV)
clients = df['Customer_Name'].unique()

customer_to_invoice_id = {}
for customer, group in df.groupby('Customer_Name'):
    customer_to_invoice_id[customer] = group.iloc[0]['Invoice_ID']

def generate_selected_invoices():
    selected_clients = [name for name, (_, var) in client_data.items() if var.get()]
    if not selected_clients:
        messagebox.showwarning("No selection", "Please select at least one client.")
        return

    for client in selected_clients:
        create_invoice_from_id(df, customer_to_invoice_id[client], logo_path=LOGO_PATH)
    
    messagebox.showinfo("Done", f"Invoices generated for: {', '.join(selected_clients)}")

def select_all():
    for chk, var in client_data.values():
        if chk.winfo_viewable():
            var.set(True)

def deselect_all():
    for chk, var in client_data.values():
        if chk.winfo_viewable():
            var.set(False)
        
def filter_clients(*args):
    query = search_var.get().lower()
    for name, (chk, var) in client_data.items():
        if query in name.lower():
            chk.pack(anchor="w")
        else:
            chk.pack_forget()

# GUI window
root = tk.Tk()
root.title("Invoice Generator")
root.geometry("420x600")

# --- Search bar ---
search_frame = tk.Frame(root)
search_frame.pack(pady=5)

search_label = tk.Label(search_frame, text="Search:")
search_label.pack(side="left", padx=3)

search_var = tk.StringVar()
search_entry = tk.Entry(search_frame, textvariable=search_var, width=30)
search_entry.pack(side="left", padx=3)
search_var.trace_add("write", filter_clients)  # live filtering as you type

# frame for buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

select_all_btn = tk.Button(btn_frame, text="Select All", command=select_all)
select_all_btn.pack(side="left", padx=5)

deselect_all_btn = tk.Button(btn_frame, text="Deselect All", command=deselect_all)
deselect_all_btn.pack(side="left", padx=5)

# scrollable checkbox components
container = tk.Frame(root, height=300)
container.pack(padx=10, pady=10, fill="both")

canvas = tk.Canvas(container)
canvas.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(container, orient="vertical", command=canvas.yview)
scrollbar.pack(side="right", fill="y")

canvas.configure(yscrollcommand=scrollbar.set)

# frame inside canvas for checkboxes
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0,0), window=scrollable_frame, anchor="nw")

# scroll behavior
def on_frame_configure(event):
    canvas.configure(scrollregion=canvas.bbox("all"))

scrollable_frame.bind("<Configure>", on_frame_configure)

# mouse wheel scrolling
def _on_mousewheel(event):          # windows/macOS
    canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

def _on_mousewheel_linux(event):    # linux
    """Linux"""
    if event.num == 4:
        canvas.yview_scroll(-1, "units")
    elif event.num == 5:
        canvas.yview_scroll(1, "units")

def _bind_mousewheel(event):
    canvas.bind_all("<MouseWheel>", _on_mousewheel)
    canvas.bind_all("<Button-4>", _on_mousewheel_linux)
    canvas.bind_all("<Button-5>", _on_mousewheel_linux)

def _unbind_mousewheel(event):
    canvas.unbind_all("<MouseWheel>")
    canvas.unbind_all("<Button-4>")
    canvas.unbind_all("<Button-5>")
    
canvas.bind("<Enter>", _bind_mousewheel)
canvas.bind("<Leave>", _unbind_mousewheel)

# map check boxes to client names
client_data = {}
for client_name in clients:
    var = tk.BooleanVar()
    chk = tk.Checkbutton(scrollable_frame, text=client_name, variable=var)
    chk.pack(anchor='w')
    client_data[client_name] = (chk, var)

# generate invoices button
btn = tk.Button(root, text="Generate Invoices", command=generate_selected_invoices)
btn.pack(pady=10)

root.mainloop()

