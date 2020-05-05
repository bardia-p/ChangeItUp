"""
Milestone 3 Code (P7 & P8) - Batch User Interface

Team 64: Py Eaters
Team Leader: Bardia Parmoun
Team Members: Hao Lin 
              Benjamin Richards 
              Ian Holmes 
              
Authors: Benjamin Richards and Hao Lin
Submitted on 02/04/2020
"""


# Libraries 
from Cimpl import (copy, create_color, set_color, Image, get_width, get_height,
                   choose_file, load_image, show, get_color, create_image,
                   save_as)

from T64_image_filters import (red_channel, green_channel, blue_channel, 
                               combine,two_tone, three_tone, sepia, posterize, 
                               extreme_contrast, detect_edges, 
                               detect_edges_better, flip_horizontal, 
                               flip_vertical)


# Functions        
def _find_filter(command: str) -> int:
    """ Author: Bardia Parmoun 
    Type annotation: str -> function
    
    This functions finds the specific filter that is associated with the one 
    letter command and it will return the function for that filter. It returns
    the index of the array of the filters were the function is located at. 
    
    >>> _find_filter("X")
    2
    """
    
    # In the arrays of ACCEPTED_INPUTS and FILTERS the index for each filter in
    # The FILTERS array is less than the index of the same filter from the other
    # Array by 2. 
    for i in range (2, len(ACCEPTED_INPUTS) - 1): 
        if ACCEPTED_INPUTS [i] == command:
            return i - 2


def apply_filter(image: Image, command: str) -> Image:
    """ Author: Benjamin Richards 
    Type annotation: Cimpl.Image, str -> Cimpl.Image
    
    This functions takes the image and the command and applies the specific 
    filter on the image. 
    
    >>> apply_filter(original_image, "X")
    (applies the extreme contrast filter to the original image)
    """  
    
    # Finds the filter using the _find_filter function 
    selected_filter = FILTERS[_find_filter(command)]
    
    # For detect_edges and detect_edges_better the threshold value is 10
    if selected_filter == detect_edges:
        image = detect_edges(image, THRESHOLD)
    elif selected_filter == detect_edges_better:
        image = detect_edges_better(image, THRESHOLD)  
        
    # For two_tone and three_tone there are preset colour values    
    elif selected_filter == two_tone:
        image = two_tone(image, COLOUR1, COLOUR3)
    elif selected_filter == three_tone:
        image = three_tone(image, COLOUR1, COLOUR2, COLOUR3)
        
    else:
        image = selected_filter(image)
    return image
        

def read_file() -> list:
    """ Author: Hao Lin 
    Type annotation: (None) -> List of strings
    
    This functions reads the list of commands from a text file and puts them in 
    an array. 
    
    The format of the text file
    (name of the original image) (name of the final image) (the commands)
    
    Possible commands: '2','3','X','T','P','E','I','V','H'
    
    >>> read_file()
    [['miss_sullivan.jpg', 'test1.jpg', '2', 'X', 'P'], 
    ['miss_sullivan.jpg', 'test2.jpg', 'V', 'H']]
    """  
    
    filename = input("Enter your filename (with the .txt extension): ")
    file = open(filename, "r")
    
    # A list of commands each a element is an array with all the elements of the
    # Text file
    
    commands =[]
    for line in file: 
        # Splits every line based on the spaces and adds them to a 2D array
        commands += [line.split()] 
    
    file.close()
    return commands


# Main Code
# Assumptions: Cimpl.py, T64_image_filters.py, and simple_Cimpl_filters.py are
# In the same folder as this program 
commands = read_file()

# Constants
THRESHOLD = 10
COLOUR1 = "yellow"
COLOUR2 = "magenta"
COLOUR3 = "cyan"

# A list of all the possible commands
ACCEPTED_INPUTS = ["L","S","2","3","X","T","P","E","I","V","H","Q"]

# A list of all the filters.
FILTERS = [two_tone, three_tone, extreme_contrast, sepia, posterize, 
           detect_edges, detect_edges_better, flip_vertical,flip_horizontal]


for l in commands:
    # Loads the original image (first element of the line)
    original_image = load_image (l[0])
    
    for i in range (2, len(l)):
        # Goes through the commands and applies them to the image
        original_image = apply_filter(original_image, l[i])
    
    # Saves the final image (second element of the line)
    save_as(original_image, l[1])
