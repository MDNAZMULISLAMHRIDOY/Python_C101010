from pypdf import PdfReader, PdfWriter

reader = PdfReader("Software_Engineering_A_Practitioner's_Approach_9th_Ed_R_Pressman.pdf")

writer = PdfWriter()

for i in range(540,570):
 writer.add_page(reader.pages[i])
 
 with open("output.pdf","wb") as f:
     writer.write(f)
     
     
     
print("Create Your Pdf Successfully....")

