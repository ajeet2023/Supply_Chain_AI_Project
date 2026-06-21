from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_report():
    c = canvas.Canvas("Executive_report.pdf", pagesize=letter)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 750, "Supply Chain Execuitive Summary")

    c.setFont("Helvetica", 12)
    c.drawString(100, 700, "Date: June 2026")
    c.drawString(100, 680, "Summary: Analysis shows critical path for delivery optimization.")

    #Adding the chart we generated in phase 6
    c.drawImage("delivery_cost_analysis.png", 100, 350, width=400, height=300)

    c.drawString(100, 300, "Action Item: Please review the attached freight cost analysis.")
    c.save()
    print("PDF  'Executive_Report.pdf'  created successfully!")

if __name__ == "__main__":
    create_report()
