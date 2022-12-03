import PyPDF2
data = PyPDF2.PdfFileReader("Working with pdf/sample1.pdf")
print(data.documentInfo)
print(data.getNumPages())
str = ''
for i in range(1,11):
    str+= data.getPage(i).extractText()

with open('text.txt',"w",encoding='utf-8') as f:
    f.write(str)

