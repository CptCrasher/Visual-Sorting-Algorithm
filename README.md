
# Visual Sorting Algorithm

This project allows users to create or randomize an array represent by bars to be sorted step-by-step
using 4 popular sorting algoritms. This program operates as a .exe file in the form of a GUI.

## How it works
This program allows a user to generate a bar graph and to sort it using one of the four sorting
algoritms:
* Bubble Sort
* Insertion Sort 
* Selection Sort 
* Merge Sort

On the GUI, there are settings for customizing your own array to be sorted. You can 
input the minimum and maximum lengths of the entries in the array that will be sorted and also choose the
length of the array (size capped at 100). You can also choose to completly randomize the array providing a random maximum, minimum and size of the array.

Everytime you generate a new array, you will see it displayed (in it's unsorted form). You can continue to change 
the settings of this array until it meets your liking.

#### GUI Screen Shot
![Screenshot](https://i.imgur.com/zUwyRhS.png)

If certain conditions aren't met with the inputted data, for example:
* Minimum set higher than the maximum 
* Values too high 
* Nothing inputted

Error conditions have been set allowing a default value to be subsituted with the specifed value providing an error or allowing the array to not be generated at all.

The entirety of this program was coded in Python using notable packages such as:
* `Tkinter` (Creation of interactive GUI)
* `NumPy` (Array calculations)


**To download and try this program for yourself, download the folder titled "Visual Sorting Alg Build" and run the "Visual Sorting Alg.exe".**

#### Randomizing Data
![Screenshot](https://static.wixstatic.com/media/552ff3_d6cb0b4c09a74861a3cfda46f528b96d~mv2.gif)

#### Sorting Data
The following demonstration utilizes insertion sort
![Screenshot](https://static.wixstatic.com/media/552ff3_1a2c2dd610634752a2bfefa67fbd1734~mv2.gif)


