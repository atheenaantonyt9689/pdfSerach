import sys, fitz
file = 'data/physicsnobel2020.pdf'
try:
    doc = fitz.open(file) 
except Exception as e:
    print(e)
page_count  = doc.pageCount
for page in doc:
    print(page)
    #doc2 = fitz.open() 
    #doc2.insert_pdf(doc,to_page =1)
    

    
    
   



    #doc2 = fitz.open()                 # new empty PDF
    #x.insert_pdf(doc, to_page =1)  # first 10 pages
    #doc2.insert_pdf(doc, from_page = len(doc) - 10) # last 10 pages
    #doc2.save("k.pdf")
