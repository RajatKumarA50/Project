from PyPDF2 import PdfFileReader
# Opening the pdf in a read binary mode
file=open('C:/Users/Rajat/Desktop/CHAPTER 1 Textbook.pdf','rb')
# instantiating the object
reader=PdfFileReader(file)
print("Printing the document info: ",(reader.getDocumentInfo()))
print('**************************************************')
print()
print("Number of pages: ",reader.getNumPages())
print("PDF File Created by: ",reader.getDocumentInfo().creator)
print("**************************************************")
pages=reader.getNumPages()
for i in range(0, pages):
    print("Page number: ",i+1)
    print("-----------------------------------------------------------")
    pageObj = reader.getPage(i)
    print(pageObj.extractText())
    print("-----------------------------------------------------------")
# close the PDF file object
file.close()