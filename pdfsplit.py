import sys, fitz
file = 'data/physicsnobel2020.pdf'
try:
    doc = fitz.open(file) 
except Exception as e:
    print(e)

for page in doc:
    
    doc2 =fitz.open()
    doc2.insert_pdf(doc,from_page=page.number,to_page=page.number)
    doc2.save("data/physicsnobel-%i.pdf"%page.number)
    
    
    
    
   



   