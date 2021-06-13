import sys, fitz
file = 'data/physicsnobel2020.pdf'
try:
    doc = fitz.open(file) 
except Exception as e:
    print(e)
#page_count  = doc.pageCount
for page in doc:   
    doc2 =fitz.open()
    doc2.insert_pdf(doc)
    doc2.save("data/physicsnobel-%i.pdf"%page.number)
    
    
    
    
   



   