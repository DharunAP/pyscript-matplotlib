from pyscript import display,document
from pyweb import pydom
import matplotlib.pyplot as plt
from js import document

xVal = pydom['input#x'][0]
yVal = pydom['input#y'][0]
xLable = pydom['span#xlab'][0]
yLable = pydom['span#ylab'][0]
res,lt = plt.subplots()
pltType = ''
# res,t = plt.subplots()
def disp():
    val = pydom['div#inp-container'][0]
    val.add_class('hidden')
    val.html=""
    bo = pydom['div#field'][0]
    bo.remove_class('hidden')
    lt.clear()
    x=pydom['input#x'][0].value = ""
    y=pydom['input#y'][0].value = ""
    pydom['span#err'].html = ""
    pydom['div.ydiv'][0].remove_class('hidden')
    pydom['span.ydiv'][0].remove_class('hidden')

def line(event):
    pydom['span#hidden'][0].html = event.target.value
    disp()
    xLable.html = '*numbers separated by spaces'
    if pydom['span#hidden'][0].html=='hist':
        pydom['div.ydiv'][0].add_class('hidden')
        pydom['span.ydiv'][0].add_class('hidden')
        return 
    yLable.html = '*numbers separated by spaces'
def box(event):
    pydom['span#hidden'][0].html = event.target.value
    disp()
    xLable.html = "*Labels should be space-separated with no spaces in each label"
    yLable.html = '*numbers separated by spaces'
    if event.target.value=='pie':
        pydom['label.grid'][0].add_class('hidden')
    return None
def click(x):
    try:
        pydom['span#err'].html=""
        pydom['div#disp'].html=""
        x=pydom['input#x'][0].value.split(' ')
        y=pydom['input#y'][0].value.split(' ')
        key = pydom['span#hidden'].html[0]
        print('--key--',key)
        if(key=='line'):
            lt.set_title(key+' plot')
            lt.plot(x,y)
        elif(key=='scatter'):
            lt.set_title(key+' plot')
            lt.scatter(x,y)
        elif(key=='box'):
            lt.set_title(key+' plot')
            lt.bar(x,y)
        elif(key=='pie'):
            lt.set_title(key+' plot')
            lt.pie(y,labels=x,autopct='%1.0f%%')
        else:
            lt.set_title(key+' plot')
            lt.hist(x)
        print(x,y)
        if(pydom['input#grid']):
            lt.grid()
        display(res,target='#disp')
    except Exception as e:
        print('err',str(e))

        pydom['span#err'].html=str(e)
        # disp()
# x = [1,2,3,4,5,6,7]
# y = [1,2,3,4,5,6,7]
# t.set_title("plot-1")
# t.plot(x,y)
# display(res,target='#disp')


print("Hello terminal") # this goes to the terminal