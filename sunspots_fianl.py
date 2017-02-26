from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics import renderPDF
from reportlab.graphics.charts.lineplots import LinePlot

URL = 'http://www.swpc.noaa.gov/ftpdir/weekly/Predict.txt'
COMMENT_CHAR = '#:'

drawing = Drawing(400,200)
data = []
for line in urlopen(URL).readline():
    if not line.isspace() and not line[0] in COMMENT_CHAR:
        data.append(float(n) for n in line.split())


"""
最精妙的就是，在[]里面直接来一个循环以加入到数组中去
"""
high = [row[3] for row in data]
pred = [row[2] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

lp = LinePlot()
lp.x=50
lp.y=50
lp.width = 300
lp.high = 125
lp.data = [zip(times, pred), zip(times, high)]
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)
drawing.add(String(250, 150, 'Sunspots', fontSize=14, fillColor=colors.red))

renderPDF.drawToFile(drawing, 'report2.pdf', 'Sunspots')

