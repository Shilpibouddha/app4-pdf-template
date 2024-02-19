from fpdf import FPDF #FPDF is a class which creates pdf instances
import pandas as pd


pdf=FPDF(orientation="P", unit="mm" , format="A4") #P stand for portrait L for landscape

df=pd.read_csv("topics.csv")

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family="Times", style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L",ln=1)#w=0 means till end of page, align =l means start from left side ,ln=1 means start from next line
    for y in range(20,298,10):

        pdf.line(10,y,200,y)



pdf.output("output.pdf")
