#Imports
from cmath import e
from tkinter import *
from tkinter import ttk
import tkinter.font as font
import random
import numpy as np
from  sortingAlgorithms import bubbleSort, insertionSort, selectionSort, mergeSort, resetGlobals

#|---------------------------Functions---------------------------|
#Function that draws rectangles to the canvas 'myCanvas'.
#Takes in the randomly generated 'data' array and an array of the same length deciding the color of each bar in the 'data' array.
def draw(data,currentColor):
    #Clear 'myCanvas'
    myCanvas.delete("all")
    canvasHeight = 600
    canvasWidth = 1000
    dataSize = len(data)
    #The height of each bar is large enough so that atleast one extra bar can fit into the canvas height.
    barHeight = canvasHeight / (dataSize+1)
    offset = 11
    barSpacing = round(1/dataSize)
    
    #Scale the data so each element in the data array ranges between 0 and 1.
    #Use numpy to multiply entire 'data' array by scalar of 1/(highest value in 'data' array).
    scaledData = 1/(max(data)) * np.array(data)
    
    #Scale font size depending on however many elements are in the 'data' array.
    #Minimum font size is '5'.
    fontSize = round((1/dataSize)*150)+5
    #Set font on the the number displayed on the bar.
    barFont = font.Font(family="Fira Code", size = fontSize)
    #If there are more than 50 'data' elements, don't show the numbers on the bar as it can become messy and hard to read.
    if dataSize-1 > 50:
        showFont = False
    else: 
        showFont = True

    #Obtaining the (x,y) coordinates of the top-left and bottom-right positions of each individual bar representing each element in the 'data' array.
    #Enumerate to obtain both the index value and the current element of the 'data' array
    for i, dataVal in enumerate(scaledData):
        #(x,y) point of the top left of our bar
        #The x is always 0 on our canvas (all the way to the left).
        #The y is the the length of i bar heights (plus offset and spacing if any).
        topx = 0
        topy = (i*barHeight) + offset + barSpacing
        
        #(x,y) point of the bottom right of our bar
        #The x is going to be the distance from the canvas width to the difference of the canvas width and current 'data' array element
        #Multiply current 'data' array element (scaled element) by 900 to scale it up so its almost as large as the total canvas width (100 less than 1000)
        #The y is the height of i+1 bar heights (plus offset and spacing if any).
        botx = canvasWidth - (canvasWidth-dataVal*900)
        boty = (i+1)*barHeight + offset
        
        #Draw a rectangle based on the calculated top left (x,y) point and bottom right (x,y) point. 
        #Color based on the colorArray's color for the current element.
        myCanvas.create_rectangle(topx,topy,botx,boty,fill=currentColor[i],outline="")
        #If the 'data' array's length is greater than 50, don't show the text on the bars.
        if showFont == True:
            myCanvas.create_text(botx-2,boty - (barHeight/2),anchor=E, text=str(data[i]),font=barFont,fill='white')
    #Allows each change in the sorting algorithm to be shown.
    root.update_idletasks()        

#Function used to ensure user inputed data is valid.
def entryVerification():
    #Try & except used to make sure there is an input enter in the entry field. 
    #If there isn't default to the base case of size = 5, max = 10, min = 0 and enter these values into the entry field.
    try:
        maximum = int(maxEntry.get())
    except:
        maximum = 10
        maxEntry.delete(0,"end")
        maxEntry.insert(0,"10")
    try:
        minimum = int(minEntry.get())
    except:
        minimum = 0
        minEntry.delete(0,"end")
        minEntry.insert(0,"0")
    try:
        size = int(sizeEntry.get())
    except:
        size = 5
        sizeEntry.delete(0,"end")
        sizeEntry.insert(0,"5")        

    #Testing for other invalid cases:
    #Min is negative or greater than the maximum, Max is negative/0 and size is negative or greater than 100. If so, resort to the default case.
    if (minimum < 0 or minimum >= maximum):
        minimum = 0
        minEntry.delete(0,"end")
        minEntry.insert(0,"0")
    if(maximum <= 0 or maximum <= minimum):
        maximum = 10
        maxEntry.delete(0,"end")
        maxEntry.insert(0,"10")     
    if (size < 0 or size > 100):
        sizeEntry.delete(0,"end")
        sizeEntry.insert(0,"5")
        size = 5       
    return minimum, maximum, size

#Function that is issued when the 'Generate' button is pressed.
#Recieves all values from the entry fields and assigns them to size, min and max accordingly. 
#Using these values, a bar graph is drawn.
def generate():
    global data
    global dataHolder
    #entryVerficiation is used to ensure user inputed max, min and size values are all valid.
    minimum,maximum,size = entryVerification()
    data=[]
    for i in range(size):
        data.append(random.randint(minimum,maximum)) 
    #Draw function called to draw on canvas
    dataHolder = np.copy(data)    
    draw(data,colorAlternator())

#Create an array the same length as the 'data' array that contains the color of each element's bar to be drawn on the canvas
#Alternates between a darker and lighter purple
def colorAlternator():
    global data
    dataSize = len(data)
    lightenBar = True
    colorArray = []
    for i in range(dataSize):
        if lightenBar == True:
            colorArray.append('#6967a1')
            lightenBar = False
        else:
            colorArray.append('#545283')
            lightenBar = True
    return colorArray 

#Command that is issued when 'Randomize' button is pressed. Assigns a random value for the size (maximum of 50) and maximum (maximum of 999).
#Assigns a random value less than 200 of the maximum value to the minimum value  unless maximum is less than 200.      
def randomizeData():
    size = random.randint(4,50)
    maximum = random.randint(0,999)
    if(maximum > 201):
        minimum = random.randint(0,maximum-200)
    else:
        minimum = random.randint(0,maximum)
    #Clearning and entering the new size, min and max values in the entry fields    
    minEntry.delete(0,"end")
    minEntry.insert(0,str(minimum))
    maxEntry.delete(0,"end")
    maxEntry.insert(0,str(maximum))
    sizeEntry.delete(0,"end")
    sizeEntry.insert(0,str(size))
    generate()

#Command that is issued when 'Sort' button is pressed. Calls the 'sort' function.
def beginSort():
    global data
    #If generate is pressed, nothing will happen
    if not(not sizeEntry.get() or not minEntry.get() or not maxEntry.get()):
        #Dictionary that holds the sorting functions keyed to their respected names.
         algDict ={
        "Bubble Sort": bubbleSort,
        "Insertion Sort": insertionSort,
        "Selection Sort": selectionSort,
        "Merge Sort" : mergeSort
        }
        #Depending on whatever the combobox entry is, initiate the respected function.
         disableWidgets()
         if algType.get() == "Merge Sort":
             mergeSort(data,draw,0,(len(data))-1,fastMode.get())
         else:    
            algDict[algType.get()](data,draw,fastMode.get())
         enableWidgets()
         
#Re-draws the original array we had before sorting.
def resetData():
    global dataHolder
    global data
    if len(dataHolder > 0 ):
        resetGlobals()
        data = np.copy(dataHolder)
        draw(data,colorAlternator())

#Disables all widgets
def disableWidgets():
    algMenu.config(state = DISABLED)
    sizeEntry.config(state = DISABLED)
    minEntry.config(state = DISABLED)
    maxEntry.config(state = DISABLED)
    genButton.config(state = DISABLED)
    sortButton.config(state = DISABLED)
    sizeEntry.config(state = DISABLED)
    resetButton.config(state = DISABLED)
    
#Enables all widgets    
def enableWidgets():
    algMenu.config(state = NORMAL)
    sizeEntry.config(state = NORMAL)
    minEntry.config(state = NORMAL)
    maxEntry.config(state = NORMAL)
    genButton.config(state = NORMAL)
    sortButton.config(state = NORMAL)
    sizeEntry.config(state = NORMAL)
    resetButton.config(state = NORMAL)

#Setting up default Tkinter Frame
root = Tk()
root.title('Visualized Sorting Algorithms')
root.maxsize(1600,1600)
root.config(bg='#272643')

#Setting up custom fonts
myFont = font.Font(family="Open Sans",size=10)
myFontBold = font.Font(family="Open Sans",size=10,weight="bold")
titleFont = font.Font(family="Fira Code", size = 15,weight="bold")


#Initlizing Variables
algType = StringVar()
data = []
dataHolder = np.copy(data)
fastMode = IntVar()

#Creating two sections on the Tkinter Frame - one side will be for a UI (Frame), the other for graphical display (Canvas).
myFrame = Frame(root, width=300,height=650,bg='#272643',bd=0)
myFrame.grid(row=0,column=0, padx=0,pady=0)
myCanvas = Canvas(root,width=1000,height=600, bg='#e2fbfa',relief=GROOVE,bd=4)
myCanvas.grid(row=0,column=2,padx=20,pady=20)


#|---------------------------myFrame(Column[0]) - User Interface---------------------------|
#Column[0] will contain the widgets for the visualizer.
#All user interface is stored in the 'myFrame' frame.

#Creating a box for to outline the application name.
titlebox = Canvas(myFrame,width=270,height=150, bg='#272643',relief=GROOVE,bd=4,highlightbackground='#7674b6').grid(row=0,column=0,columnspan=2,padx=5,pady=5,sticky=E)

#Application Title
Label(myFrame,text="Ajay's Sorting\nVisualizer",bg='#272643',fg='white',font=titleFont,width=19).grid(row=0,column=0,columnspan=2,padx=5,pady=70,sticky=N)

#Label to create spacing.
Label(myFrame,text="",bg='#272643').grid(row=1,column=0,padx=5,pady=5)

#Dropdown menu to select the sorting algorithm.
Label(myFrame, text="Selected Algorithm: ", bg ='#272643', fg='white',font=myFont).grid(row=2,column=0,padx=5,pady=0,sticky=W)
algMenu = ttk.Combobox(myFrame, textvariable=algType, font=myFont, values =['Bubble Sort', 'Merge Sort', 'Selection Sort', 'Insertion Sort'])
algMenu.grid(row=2, column=1,padx=0,pady=0)
algMenu.current(0)

#Space between 'Generation' button and text fields.
Label(myFrame, text="",bg='#272643').grid(row=3,column=0,padx=2,pady=3)

#Text field to enter amount of data entries.
Label(myFrame, text="Data Size: ", bg='#272643', fg='white',font=myFont,width=10).grid(row=4,column=0,padx=5,pady=10,sticky=E)
sizeEntry = Entry(myFrame)
sizeEntry.grid(row=4,column=0,columnspan=2,padx=10,pady=10,sticky=E)

#Text field to enter amount of data entries.
Label(myFrame, text="  Minimum: ", bg='#272643', fg='white',font=myFont,width=10).grid(row=5,column=0,padx=5,pady=10,sticky=E)
minEntry = Entry(myFrame)
minEntry.grid(row=5,column=0,columnspan=2,padx=10,pady=10,sticky=E)

#Text Field to enter amount of data entries.
Label(myFrame, text="  Maximum: ", bg='#272643', fg='white',font=myFont,width=10).grid(row=6,column=0,padx=5,pady=10,sticky=E)
maxEntry = Entry(myFrame)
maxEntry.grid(row=6,column=0,columnspan=2,padx=10,pady=10,sticky=E)

#'Generation Button' that calls createData function.
genButton = Button(myFrame,text="Generate Data", command = generate, bg = '#bae8e8',font=myFont,bd=0)
genButton.grid(row=7,column=0,columnspan=2,padx=20,pady=10)

#'Randomize Button' that randomizes max,min and size.
#Reading the image from directory.
diceImg = PhotoImage(file = r"dice2.png")
ranButton = Button(myFrame, text = "",image=diceImg,bg="#272643",bd=0,font=myFont,command = randomizeData).grid(row=7,column=1,padx=10,pady=5,sticky=E)

#Space between randomize + generation buttons and sort button.
Label(myFrame,text="",bg='#272643').grid(row=8,column=0,padx=20,pady=20)

#Button that beings sorting visualizer.
sortButton = Button(myFrame,text="Sort", command = beginSort, bg ='#93f1b7', font = myFontBold,bd=0)
sortButton.grid(row=9,column=0,columnspan = 2, padx=5,pady=5)

#Check box that allows sorting algorithm to run faster.
fastBox = Checkbutton(myFrame,text="Fast Mode", variable = fastMode,font = myFont,bg='#adbcfb',onvalue=1,offvalue=0,bd=0).grid(row=10,column=0,padx=10,pady=10,sticky=W)

#Reset button that undos the applied sorting algorithm
resetButton = Button(myFrame,text="Reset", command = resetData, bg='#adbcfb', font = myFont,bd=0)
resetButton.grid(row=10,column=1,padx=5,pady=10,sticky=E)
root.mainloop()
