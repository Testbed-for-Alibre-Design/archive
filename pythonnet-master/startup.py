import pythonnet
import sys
import os
current_directory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(current_directory)
import clr
clr.AddReference('LibraryVb')
import System
clr.AddReference("System.Runtime.InteropServices")
from LibraryVb import *

def CodeTest():
    Init.CodeTest()
    print("CodeTest worked!")
    
def CodeTest2(x,y,z):
       """
    Calls the printpoint method from the Init class within the LibraryVb namespace with the given parameters.

    Parameters:
        x (float): The x coordinate.
        y (float): The y coordinate.
        z (float): The z coordinate.

    No return value.
    """
       Init.printpoint(x,y,z)