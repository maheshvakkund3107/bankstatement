from fpdf import FPDF
import pandas as pd

pdf = FPDF()
# Add a page
pdf.add_page()
filepath = '07950100017620 SOABoB.txt'
pdf.set_font("Arial", size=12)
# open the text file in read mode
f = open(filepath, "r")
# insert the texts in pdf
for x in f:
    pdf.cell(260, 12, txt=x, ln=1, align='C')

# save the pdf with name .pdf
pdf.output("baroda.pdf")
df = pd.read_fwf('baroda.pdf')
df
