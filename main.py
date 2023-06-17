
from fpdf import FPDF

pdf = FPDF(orientation='p', unit="mm", format="A4")

pdf.add_page()
pdf.set_font(family="Arial", style="B", size=12)
pdf.cell(w=0, h=12, txt="Lanos institute of computer science", border=1, ln=1)
pdf.cell(w=0, h=12, txt="Learn and liberate your future", border=0, ln=1)

pdf.rect(50,50,100,50, 'D', )