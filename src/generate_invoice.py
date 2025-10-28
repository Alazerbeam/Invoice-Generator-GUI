from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from datetime import datetime, timedelta
import os

def create_invoice_from_id(
    df, invoice_id, invoice_file_path=None, logo_path=None, 
    tax_rate=0.08, discount=0.0, due_days=14
):
    # extract all sales data for given invoice_id
    invoice_data = df[df["Invoice_ID"] == invoice_id].copy()

    # extract customer info (from 1st row)
    customer_name = invoice_data.iloc[0]["Customer_Name"]
    customer_email = invoice_data.iloc[0]["Email"]
    customer_address = invoice_data.iloc[0]["Address"]
    customer_citystate = invoice_data.iloc[0]["City_State"]
    customer_zipcode = str(invoice_data.iloc[0]["Zip"])
    
    invoice_date = datetime.strptime(invoice_data.iloc[0]["Date"], "%Y-%m-%d")
    due_date = invoice_date + timedelta(days=due_days)
    
    invoice_date = invoice_date.strftime("%Y-%m-%d")    # format the datetimes to include date only
    due_date = due_date.strftime("%Y-%m-%d")
    
    # calculate totals
    invoice_data["Total_Price"] = invoice_data["Quantity"] * invoice_data["Unit_Price"]
    subtotal = invoice_data["Total_Price"].sum()
    discount_amount = subtotal * discount
    taxed_amount = (subtotal - discount_amount) * tax_rate
    grand_total = subtotal - discount_amount + taxed_amount

    # create PDF
    if invoice_file_path:
        file_name = invoice_file_path
    else:
        file_name = f"invoices/{invoice_id}.pdf"
    
    pdf = SimpleDocTemplate(file_name, pagesize=LETTER)
    styles = getSampleStyleSheet()
    elements = []
    
    # custom paragraph styles
    bold = ParagraphStyle("bold", parent=styles["Normal"], fontName="Helvetica-Bold")
    left_align = ParagraphStyle("left", parent=styles["Normal"], alignment=0)
    right_align = ParagraphStyle("right", parent=styles["Normal"], alignment=2)
    
    # top: company info (left) + logo (right)
    company_info = [
        Paragraph("<b>Company Name</b>", bold),
        Paragraph("12 Example Avenue", styles["Normal"]),
        Paragraph("San Diego, CA, 92128", styles["Normal"]),
        Paragraph("hello@example.com", styles["Normal"]),
        Paragraph("(xxx) xxx-xxxx", styles["Normal"])
    ]
    
    logo_img = None
    if logo_path and os.path.exists(logo_path):
        logo_img = Image(logo_path, width=100, height=50)
    
    top_table = Table([[company_info, logo_img]], colWidths=[350,150])
    top_table.setStyle(TableStyle([
        ("VALIGN", (0,0), (-1,-1), "TOP"),
        ("ALIGN", (1,0), (1,0), "RIGHT")
    ]))
    elements.append(top_table)
    elements.append(Spacer(1,20))
    
    # bill to + invoice info
    bill_to = [
        Paragraph("<b>BILL TO</b>", bold),
        Paragraph(customer_name, styles["Normal"]),
        Paragraph(customer_email, styles["Normal"]),
        Paragraph(customer_address, styles["Normal"]),
        Paragraph(customer_citystate, styles["Normal"]),
        Paragraph(customer_zipcode, styles["Normal"]),
    ]
    
    invoice_info = [
        Paragraph("<b>INVOICE</b>", bold),
        Paragraph(f"Invoice No: {invoice_id}", styles["Normal"]),
        Paragraph(f"Issue Date: {invoice_date}", styles["Normal"]),
        Paragraph(f"Due Date: {due_date}", styles["Normal"]),
    ]
    
    bill_and_invoice_table = Table([[bill_to, invoice_info]], colWidths=[350,150])
    bill_and_invoice_table.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ]))
    elements.append(bill_and_invoice_table)
    elements.append(Spacer(1,20))

    # items table
    items_data = [["Item", "Quantity", "Unit Price", "Total"]]
    for _, row in invoice_data.iterrows():
        items_data.append([
            row["Item"],
            int(row["Quantity"]),
            f"${row['Unit_Price']:.2f}",
            f"${row['Total_Price']:.2f}"
        ])

    items_table = Table(items_data, colWidths=[200, 100, 100, 100])
    items_table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("ALIGN", (1,1), (-1,-1), "CENTER"),
        ("FONTNAME", (0,0), (-1,0), "Helvetica-Bold"),
    ]))
    elements.append(items_table)
    elements.append(Spacer(1,12))

    # summary table
    summary_data = [
        ["Subtotal:", f"${subtotal:.2f}"],
        ["Discount:", f"-${discount_amount:.2f}"],
        [f"Tax ({int(tax_rate*100)}%):", f"${taxed_amount:.2f}"],
        ["Grand Total:", f"${grand_total:.2f}"]
    ]
    summary_table = Table(summary_data, colWidths=[50,75], hAlign="RIGHT")
    summary_table.setStyle(TableStyle([
        ("ALIGN", (1, 0), (-1, -1), "RIGHT"),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -2), "Helvetica"),
        ("LINEABOVE", (0, -1), (-1, -1), 1, colors.black),
        ("LINEBELOW", (0, -1), (-1, -1), 1, colors.black),
        ("TOPPADDING", (0, 0), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
    ]))
    elements.append(summary_table)
    elements.append(Spacer(1,20))
    
    # Payment info
    elements.append(Paragraph("<b>PAY BY BANK TRANSFER</b>", bold))
    elements.append(Paragraph("Bank/Sort Code: 12-34-56", styles["Normal"]))
    elements.append(Paragraph("Account Number: 12345678", styles["Normal"]))
    elements.append(Paragraph("Payment Reference: Customer 001", styles["Normal"]))
    elements.append(Paragraph("Bank Name: Example Bank", styles["Normal"]))
    elements.append(Spacer(1, 20))
    
    # Terms
    elements.append(Paragraph("<b>TERMS</b>", bold))
    elements.append(Paragraph("<i>Add payment instructions here</i>", styles["Normal"]))
    elements.append(Paragraph("<i>Add terms here, e.g. warranty, returns policy...</i>", styles["Normal"]))

    # build pdf
    pdf.build(elements)
    print(f"Invoice '{file_name}' generated successfully!")