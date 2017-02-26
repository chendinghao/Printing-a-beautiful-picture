from reportlab.graphics.shapes import Drawing,String
from reportlab.graphics import renderPDF

d=Drawing(100,100)
s=String(50,50, 'hello,world!', textAnchor='middle')

d.add(s)

#对renderPDF.drawToFile的调用会把你的ＰＤＦ文件存储到当前目录下一个名字为 'hello.pdf'的文件中
renderPDF.drawToFile(d, 'hello.pdf', 'A simple PDF file')
