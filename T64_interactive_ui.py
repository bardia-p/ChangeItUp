"""
Milestone 3 Code (P7 & P8) - Interactive User Interface

Team 64: Py Eaters
Team Leader: Bardia Parmoun
Team Members: Hao Lin 
              Benjamin Richards 
              Ian Holmes 
              
Authors: Bardia Parmoun and Ian Holmes

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
def get_command () -> str:
    """ Author: Ian Holmes 
    Type annotation: (None) -> str
    
    This functions asks prompts the user to enter their command by printing the
    user interface. It also makes sure that the command that they choose is 
    among the list of the accepted inputs
    
    >>> get_command()
    L)oad image    S)ave_as
    2)-tone    3)-tone    X)treme contrast    T)int sepia    P)osterize
    E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip
    Q)uit
    : x
    "X"
    
    >>> get_command()
    L)oad image    S)ave_as
    2)-tone    3)-tone    X)treme contrast    T)int sepia    P)osterize
    E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip
    Q)uit
    : j
    "No such command"
    """
        
    # Making the user interface text
    LINE1 = "L)oad image    S)ave_as\n"
    LINE2 = ("2)-tone    3)-tone    X)treme contrast    T)int sepia" + 
             "    P)osterize\n")
    LINE3 = ("E)dge detect    I)mproved edge detect    V)ertical flip" + 
             "    H)orizontal flip\n")
    LINE4 = "Q)uit"
    
    # Asks the user to input a command
    print(LINE1 + LINE2 + LINE3 + LINE4)
    command = input(": ").upper()
    
    # If the user inputs a wrong command it keeps asking them until they enter 
    # The correct command
    while command not in ACCEPTED_INPUTS:
        print("No such command")
        print(LINE1 + LINE2 + LINE3 + LINE4)
        command = input(": ").upper() # Makes sure the input is uppercase
    
    return command
        
        
def open_image() -> Image:
    """ Author: Ian Holmes 
    Type annotation: (None) -> Cimple.Image
    
    This functions asks prompts the user to select an image that they want to 
    apply the filter to.
    
    >>> open_image()
    (asks the user to select their image)
    (shows the image to the user)
    """
    
    FILENAME = choose_file()
    if FILENAME != "":
        original_image = load_image(FILENAME)
        show(original_image)
        return original_image
    else:
        print("No image loaded")


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
    """ Author: Bardia Parmoun 
    Type annotation: Cimple.Image, str -> Cimpl.Image
    
    This functions takes the image and the command and applies the specific 
    filter on the image. 
    
    >>> apply_filter(original_image, "X")
    (applies the extreme contrast filter to the original image)
    """    
    
    # Finds out which filter was selected
    selected_filter = FILTERS[_find_filter(command)]
    
    # For the detect_edges and detect_edges_better filters it asks the user for
    # A threshold value
    if selected_filter == detect_edges:
        threshold = int(input("Threshold?: "))
        image = detect_edges(image, threshold)
    elif selected_filter == detect_edges_better:
        threshold = int(input("Threshold?: "))
        image = detect_edges_better(image, threshold)  
        
    # For two_tone and three_tone filters there are preset values for colours
    elif selected_filter == two_tone:      
        image = two_tone(image, COLOUR1, COLOUR3)
    elif selected_filter == three_tone:     
        image = three_tone(image, COLOUR1, COLOUR2, COLOUR3)
        
    else:
        image = selected_filter(image)
    return image
        
    
# Main Code
# Assumptions: Cimpl.py, T64_image_filters.py, and simple_Cimpl_filters.py are
# In the same folder as this program 
original_image = None 
command = ""

# Constants
COLOUR1 = "yellow"
COLOUR2 = "magenta"
COLOUR3 = "cyan"

# A list of all the possible commands
ACCEPTED_INPUTS = ["L","S","2","3","X","T","P","E","I","V","H","Q"]

# A list of all the filters.
FILTERS = [two_tone, three_tone, extreme_contrast, sepia, posterize, 
           detect_edges, detect_edges_better, flip_vertical,flip_horizontal]


while command != "Q": # Stops the program when the user enters 'Q'
    command = get_command()
    
    if command != "Q":
        if command == "L":
            original_image = open_image ()
            
        # Makes sure there is an image already selected before letting the user
        # Choose any filters
        elif original_image == None:
            print ("No image loaded")
            
        # If the user the wants to save the image it prompts them for the name    
        elif command == "S":
            save_as (original_image)
            
        else:
            original_image = apply_filter (original_image, command)
            show(original_image)

