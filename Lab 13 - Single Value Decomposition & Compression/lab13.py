# -*- coding: utf-8 -*-
"""lab13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OXRdL7cCLIXn9-3FYK5n30Ni-dYETf3n

#**Lab 13 - Singular value decompositions and image compression**

Enter your code in the spaces provided. Do not change any of the variable names or function names that are already provided for you. In places where we specify the name of the return value, make sure that your code produces the a value with the correct name.
"""

# Do not edit this cell.

LabID="Lab13"

try:
  from graderHelp import ISGRADEPLOT
except ImportError:
  ISGRADEPLOT = True

"""**Enter your name, section number, and BYU NetID**"""

# Enter your first and last names in between the quotation marks.

first_name="Brigham"

last_name="Andersen"

# Enter your Math 215 section number in between the quotation marks. 

section_number="001"  

# Enter your BYU NetID in between the quotation marks.  NOT YOUR BYU ID NUMBER! 

BYUNetID="abrigham"

"""**Import the required packages**"""

import numpy as np
import matplotlib.pyplot as plt

"""**Problem 1**"""

# This function accepts integers m and n, and an array of singular values s and returns the Sigma matrix.

def sigma(m,n,s):
  mat = np.zeros((m,n))
  for i in range(len(s)):
    mat[i,i] = s[i]
  return mat

"""**Problem 2**"""

# This function accepts arrays u,s, and v_t, and returns the corresponing array A.

def reconstructed_array(u,s,v_t):
  sig = sigma(len(u[0]), len(v_t), s)
  A = np.matmul(np.matmul(u,sig), v_t)
  return A

"""**Problem 3**"""

# This function accepts an array A and an integer k, and returns a rank k approximation of A as computed by an SVD.

def lower_rank(A,k):
  u, s, v_t = np.linalg.svd(A)
  s = s[:k]
  v_t = v_t[:k]
  return reconstructed_array(u, s, v_t)

"""**Downloading image data**

The simplest way to load the image into Colab is to first download it as a .png file to your local computer by clicking the link

https://drive.google.com/uc?export=download&id=1hlAEhTsqfvYX3aGFgRgFJF_gO-U5c0gH

This will allow you to download the image as a .png file.  In the top left corner of this screen you should see a little file folder icon.   Selecting it opens a new window to the left of the notebook with three tabs: "Upload", "Refresh", and "Mount Drive". Select "Upload".  This should bring up a window that allows you to select the file "Lab13Image.png" from your local machine, which will upload the file to your notebook.  You will need to do this again if you decide to close your notebook and reopen it at a later time.

**Import the image and convert it to an array**

The following cell imports the png image and creates two arrays.  The first array is a 3-dimensional array, which you can think of as three matrices, each of which describes one of three colors for the image (red, green, and blue).  The second line of the cell converts the image to grayscale, which can be represented by a single matrix, whose entries range between 0 and 1 and represent how dark or bright the corresponding pixel should be.
"""

import skimage 
from skimage import io

RGB_array = io.imread('Lab13Image.png')            
gray_array=skimage.color.rgb2gray(RGB_array)

"""The following functions can be used to display the color image and grayscale image respectively.

IMPORTANT NOTE: The auto-grading website will give you an error message if the file you submit contains calls to either of these functions. You can leave the function definitions for show_color and show_gray here, but make sure to delete any calls to these functions before you submit your lab for grading. (You can also copy them to your practice notebook to use them there.)
"""

def show_color(array):
  plt.figure(figsize=(10,10))
  plt.grid(None)
  plt.imshow(array)
  return None

def show_gray(array):
  plt.figure(figsize=(10,10))
  plt.grid(None)
  plt.imshow(array,cmap='gray',vmin=0,vmax=1)
  return None

""" **Problem 4**"""

# Save the value you obtain in Problem 4 as the variable original_size.

original_size=gray_array.size

"""**Problem 5**"""

# Place your plot for Problem 5 here.

u, s, v_t = np.linalg.svd(gray_array)

plt.plot(s)
show_gray(reconstructed_array(u, s, v_t))

"""**Problem 6**"""

# Save the value you obtain in Problem 6 as the variable min_rank.

min_rank=show_gray(lower_rank(gray_array, 100))
min_rank

"""**Problem 7**"""

# Save the values you obtain in Problem 7 as the variables rank_100_size and relative_size.
size_u = 100 * len(u)
size_s = 100
size_v_t = 100 * len(v_t[0])
total_size = size_u + size_s + size_v_t

rank_100_size=total_size

relative_size=total_size/original_size

"""**STOP!  BEFORE YOU SUBMIT THIS LAB:**  Go to the "Runtime" menu at the top of this page, and select "Restart and run all".  If any of the cells produce error messages, you will either need to fix the error(s) or delete the code that is causing the error(s).  Then use "Restart and run all" again to see if there are any new errors.  Repeat this until no new error messages show up.

**You are not ready to submit until you are able to select "Restart and run all" without any new error messages showing up.  Your code will not be able to be graded if there are any error messages.**

To submit your lab for grading you must first download it to your compute as .py file.  In the "File" menu select "Download .py".  The resulting file can then be uploaded to http://www.math.byu.edu:30000 for grading.
"""