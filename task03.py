from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from datetime import datetime

def create_receipt(file_path, receipt_info):
    # Initialize the canvas with the output file path and page size 612 x 792
    c = canvas.Canvas(file_path, pagesize=letter)

    # Draw rectangle for logo
    c.setStrokeColor("blue")
    c.setFillColor("lightgrey")
    c.rect(15, 777, 150, -100, fill=True)

    # Draw rectangle 2 for company name
    c.setStrokeColor("blue")
    c.setFillColor("lightgrey")
    c.rect(170, 777, 427, -100, fill=True)

    # Draw image (assuming "example.jpg" exists)
    # c.drawImage("example.jpg", 100, 600, width=100, height=100)
    
    # Draw lines
    c.setStrokeColor("black")
    c.line(15, 667, 597, 667)  # Horizontal line

   # Title
    c.setFont("Times-Roman", 16)
    c.setFillColor(colors.black)
    c.drawString(250, 640, "Payment Receipt")

    # Date
    c.setFont("Times-Roman", 12)
    c.drawString(100, 610, f"Date: {receipt_info['date']}")

    # Payee
    c.drawString(100, 590, f"Payee: {receipt_info['payee']}")

    # Payer
    c.drawString(100, 570, f"Payer: {receipt_info['payer']}")

    # Items
    c.drawString(100, 530, "Description")
    c.drawString(400, 530, "Amount")
    y_position = 500
    total = 0

    for item in receipt_info['items']:
        c.drawString(100, y_position, item['description'])
        c.drawString(400, y_position, f"Rs. {item['amount']:.2f}")
        total += item['amount']
        y_position -= 20

    # Total
    c.drawString(300, y_position - 30, f"Total: Rs.{total:.2f}")

    # Footer
    c.setFont("Times-Roman", 10)
    c.drawString(250, 100, "Thank you for your payment.")

    c.save()

# Example usage
current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
receipt_info = {
    "date": f"{current_time}",
    "payee": "ACME Corporation",
    "payer": "John Doe",
    "items": [
        {"description": "Item 1", "amount": 29.99},
        {"description": "Item 2", "amount": 49.99},
        {"description": "Service Fee", "amount": 15.00}
    ]
}

create_receipt("payment_receipt.pdf", receipt_info)