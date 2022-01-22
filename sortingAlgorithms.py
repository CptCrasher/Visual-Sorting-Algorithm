#Imports
import time
import numpy as np
from turtle import color

speed = 0.2
originalColorArray = []

#Whenever the reset button is pressed, all global values are also reset
def resetGlobals():
    global speed
    global originalColorArray
    speed = 0.2
    print('ok')
    originalColorArray = np.array([])
    print(originalColorArray)
    
#Creates a list of alternating dark and light colors the same length as a passed array.
def colorAlternator(data):
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
#Applies the bubble sort algorithm to a passed array.
def bubbleSort(data,draw,fastMode):
    dataLength = len(data)-1
    #Used to set color array back to its inital color.
    originalColorArray = np.array(colorAlternator(data))
    #Used to update the color of selected elements during sort.
    updatedColor = np.copy(originalColorArray)
    #Loop through the block of code i times for each element in the data array
    for i in range(dataLength):
        #For each loop, loop i amount of times for each element in the data array
        for j in range(dataLength):
            #If the current element is greater than the next element swap both of these elements
            if data[j] > data[j+1]:
                data[j+1],data[j] = data[j],data[j+1]
                #Draw the swapping of 'data's' elements everytime elements swap.
                #Set the swapped partition to green in the color array. Everything else is set back to the original color.
                for k in range(len(data)):
                    if (k==j or k==j+1):
                       updatedColor[k] = '#93f1b7'
                    else:
                        updatedColor[k] = originalColorArray[k]
                draw(data,updatedColor)           
                
                #Delay between each swap in the bubble sort. If checkbox is checked, delay is reduced.
                if(fastMode == 1):
                    time.sleep(0.0001)
                else:
                    time.sleep(0.2)
    draw(data,originalColorArray)
#Applies the insertion sort algorithm to a passed array.
def insertionSort(data,draw,fastMode):
    #Used to set color array back to its inital color.
    originalColorArray = np.array(colorAlternator(data))
    #Used to update the color of selected elements during sort.
    updatedColor = np.copy(originalColorArray)
    dataLength = len(data)
    #Cycle through the first element to the last element of the 'data' array
    for i in range (1,dataLength):
        #Create a key that holds the current 'data' array's element
        dataVal = data[i]
        #While the current element is less than the previous element, swap the previous element with the current element of the 'data' array (and the index i hasn't reached 0):
        while data[i-1] > dataVal and i>0:
            data[i], data[i-1] = data[i-1],data[i]
            #Decrement the index.
            i-=1
            #If two elements were swapped, change the same index in the updatedColoar array to green else set them back to their original colors.
            for j in range(dataLength):
                if (j == i or j ==i-1):
                    updatedColor[j] = '#93f1b7'
                    updatedColor[j] ='#93f1b7'
                else:
                    updatedColor[j] = originalColorArray[j]
            #Draw the bars using the updatedColor array and the new 'data' array.         
            draw(data,updatedColor)  
            #Delay between each swap in the bubble sort. If checkbox is checked, delay is reduced.
            if(fastMode == 1):
                    time.sleep(0.0001)
            else:
                    time.sleep(0.2)   
    #When sorting is complete, reset color to the orginal                 
    draw(data,originalColorArray)
#Applies the selection sort algorithm to a passed array.
def selectionSort(data,draw,fastMode):
    #Used to set color array back to its inital color.
    originalColorArray = np.array(colorAlternator(data))
    #Used to update the color of selected elements during sort.
    updatedColor = np.copy(originalColorArray)
    dataLength = len(data)
    for i in range(dataLength):
        #Current index is the intially the lowest value
        minVal = i
        
        #If there exists an element in 'data' that is lower than 'data' at the current minVal, set this element as the new minVal.
        for j in range(i+1, dataLength):        
            if data[j] < data[minVal]:
                minVal = j
                
        #If there is an element in 'data that is lower than our inital 'data' value, swap the inital element with the lower element.        
        if minVal != i:
            data[minVal],data[i] = data[i], data[minVal]
            #If two elements were swapped, change the same index in the updatedColoar array to green else set them back to their original colors.
            for k in range(dataLength):
                if (k == minVal or k ==i):
                    updatedColor[k] = '#93f1b7'
                    updatedColor[k] ='#93f1b7'
                else:
                    updatedColor[k] = originalColorArray[k]
            #Draw the bars using the updatedColor array and the new 'data' array.         
            draw(data,updatedColor)  
            #Delay between each swap in the bubble sort. If checkbox is checked, delay is reduced.
            if(fastMode == 1):
                    time.sleep(0.0001)
            else:
                    time.sleep(0.2) 
    draw(data,originalColorArray)                      
#Applies the merge sort algorithm to a passed array.
def mergeSort(data,draw,left,right,fastMode):
     global originalColorArray
     global speed

     #When the function is initally run, set the originalColorArray to a array of alternating dark and light bar colors the same length as the 'data' array.
     #Since 'data''s size will change throughout this function (as a result of recursion), we must only make the originalColorArray's length the same as the inital data array. 
     if not originalColorArray:
         originalColorArray = colorAlternator(data)
     #If the checkbox is ticked set the speed to go fast, otherwise keep the speed at 0.2.    
     if fastMode == 1:
       speed = 0.0001
     else:
         speed = 0.2   
     
     #The base is that aslong as the length of the smaller partitioned arrays are 1, they have been storted.          
     if left < right:
        #Find the middle index of the data array and floor division it.
        middle = (left + right) // 2
        #Use recursion to keep calling the left and right arrays made from data until the array consists of 2 elements
        mergeSort(data,draw,left,middle,fastMode)
        mergeSort(data,draw,middle+1,right,fastMode)
        #Draw bars onto the canvas based on any changes made to the data array.
        draw(data,changeColor(len(data),left,middle,right))
        time.sleep(speed)
        #Everything from the 0 index to the middle index is the left array, everything else is the right array.
        leftArray = data[left:middle+1]
        rightArray = data[middle+1:right+1]
        i=0 #Left array index
        j=0 #Right array index
        k=left #Data array index
        leftLength = len(leftArray)
        rightLength = len(rightArray)
        #As long as the index of our data array doesn't exceed the length of the data array:
        while k <=right:
            #If we haven't sorted everything in our sub left and right arrays then:
            if i < leftLength and j < rightLength:
                #Enter in the lower value of the left and right sub arrays. Increment the left or right array index along with the index of our data array.
                if leftArray[i] <= rightArray[j]:
                    data[k] = leftArray[i]
                    i+=1
                    k+=1
                else:
                    data[k] = rightArray[j]
                    j+=1
                    k+=1
            #If everything in either our left or right subarrays have been sorted and entered into our data array, place the remaining of the other array into the 
            # data array afterwards. (The subarray that hasn't been added to our final data array is sorted from the inital recursion process of making left and right arrays of length 1
            # meaning, we can simply add them to our final data array as they are already sorted).
            elif i < leftLength:
                data[k] = leftArray[i]
                i+=1
                k+=1

            else:
                data[k] = rightArray[j]
                j+=1
                k+=1
        #Once everything is done, draw our data array one last time and set it back to its original color.        
        draw(data,originalColorArray)
        time.sleep(speed)                  
# def mergeSort2(data,draw,left,right,fastMode):
    # global data1
    # data1 = np.copy(data)
    # mergeSort(data1,draw,left,right,fastMode)

#Function that allows us to change the color of the elements in the array that we are currently working on.
def changeColor(length,left,middle,right):
    
    colorArray = []
    global originalColorArray
    for i in range(length):
        if i >= left and i <= right:
            if i >= left and i <= middle:
                colorArray.append("#b8f7bb")
            else:
                colorArray.append("#b8f7eb")
        else:
            #Fills the rest of the colorArray with our original color.
            colorArray.append(originalColorArray[i])

    return colorArray   








