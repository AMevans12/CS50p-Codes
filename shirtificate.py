from fpdf import FPDF

WHITE = (255, 255, 255)

class PDF:
    def __init__(self, name):
        self._pdf = FPDF()
        self._pdf.set_font("helvetica", 'B', 50)
        self._pdf.add_page()
        self._pdf.set_page_background(WHITE)
        self._pdf.cell(0, 60, 'CS50 Shirtificate', align='C')
        self._pdf.image("shirtificate.png", w=self._pdf.epw)
        self._pdf.set_text_color(*WHITE)
        self._pdf.set_xy(47.5, 140)
        self._pdf.cell(0, 10, f'{name} took CS50', align='C')

    def save(self, filename):
         self._pdf.output(filename)

name = input('Name: ')
pdf = PDF(name)
pdf.save('shirtificate.pdf')
