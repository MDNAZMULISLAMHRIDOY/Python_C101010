from pypdf import PdfWriter

merger = PdfWriter()

pdfs= ["Game Theory.pdf","Generating Function.pdf"]

for pdf in pdfs:
    merger.append(pdf)
    
    
merger.write("merged.pdf")
merger.close()
print("PDFs merged successfully into merged.pdf")       