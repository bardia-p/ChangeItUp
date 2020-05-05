"""
Milestone 2 Final Code (P6) - All of the filters made in milestones 1 & 2

Team 64: Py Eaters
Team Leader: Bardia Parmoun
Team Members: Hao Lin
              Benjamin Richards
              Ian Holmes
              
Submitted on 02/04/2020
"""


#Libraries 
from Cimpl import (copy, create_color,set_color, Image, get_width, get_height,
                   choose_file, load_image, show, get_color)     
from simple_Cimpl_filters import grayscale 


#Functions
# Milestone 1 Filters
def red_channel (picture: Image) -> Image :
    """ Author: Benjamin Richards
    Type Annotations: Cimpl.Image -> Cimpl.Image

    This function takes a copy of a selected png image, and applies a filter to
    it, which eliminates all the blue and green aspects of the picture, leaving
    a red-only image.
    
    >>> red_image=red_channel (original_image)
    >>> show(red_image)
    (It will display the red monochrome of the image)
    """
    
    copied_image = copy(picture)   
    
    for x, y, (r,g,b) in picture:
        red = create_color(r, 0, 0)
        set_color(copied_image, x,y, red)
    return copied_image


def green_channel(image: Image) -> Image:
    """ Author: Hao Lin
    Type Annotations: Cimpl.Image -> Cimpl.Image

    This function applies the green filter to the function by making a copy of 
    the image and only keeping its green component. It will set the other values
    to zero. 
    
    >>> green_image=green_channel (original_image)
    >>> show(green_image)
    (It will display the green monochrome of the image)
    """ 
    
    copied_image = copy(image)    
    
    for pixel in image:
        x, y, (r,g,b) = pixel
        new_color = create_color(0, g, 0)
        set_color(copied_image, x,y, new_color)
    return copied_image
 

def blue_channel (image: Image) -> Image:
    """ Author: Ian Holmes 
    Type Annotations: Cimpl.Image -> Cimpl.Image
        
    Returns an image with only the blue values for each pixel 
    (Red and green rgb values are set to zero), given an initial loaded image 
    file.
    
    >>> blue_image=blue_channel (original_image)
    >>> show(blue_image)
    blue monochrome version of the image will be displayed.
    """
    
    new_image = copy(image)
    
    for x,y, (r,g,b) in image:
        new_colour = create_color(0, 0, b)
        set_color(new_image, x, y, new_colour)
    return new_image


def combine (image1: Image, image2: Image, image3: Image) -> Image: 
    """ Author: Bardia Parmoun 
    Type Annotations: Cimpl.Image, Cimpl.Image, Cimpl.Image -> Cimpl.Image
   
    This functions three filtered images (red, green, blue) and creates a new 
    image by combining the rgb's of these three images. 
   
    Note that in order for this function to work properly the three input images
    must be in .png format and should be properly filtered (for example the red
    image must only have a red component in its rgb).
   
    >>> combined_image= combine (red_image,green_image, blue_image)
    >>> show (combined_image)
    (This will display the combined image made from the three input images)
    """
    
    new_image = copy(image1)
    width = get_width(image1)
    height = get_height(image1)
    
    for x in range(width):
        for y in range(height):
            r1,g1,b1= get_color(image1, x, y)
            r2,g2,b2= get_color(image2, x, y)
            r3,g3,b3= get_color(image3, x, y)  
            
            # Combining the there pictures by adding their rgb values
            new_colour = create_color(r1+r2+r3, g1+g2+g3, b1+b2+b3)
            set_color (new_image, x,y, new_colour)   
    return new_image


# Milestone 2 Filters
def two_tone(image: Image, colour1: str, colour2: str) -> Image:
    """Author: Benjamin Richards 
    Type Annotations: Cimpl.Image, str, str -> Cimpl.Image
    
    Takes an image and 2 colours and returns a copy of the image which is made
    up of only those two colours. If the pixel's brightness is between 0 and 127 
    it uses the first colour and if it's more than that it uses the second color
    
    >>> new = two_tone (original_image, 'blue', 'red')
    >>> show(new)
    (shows the image only made up of blue and red)."""
    
    #Constants
    COLOUR_LIST = ["black","white","red","lime","blue","yellow","cyan","magenta"
                   ,"gray"]
    COLOUR_CODES = [(0,0,0),(255,255,255),(255,0,0),(0, 255, 0),(0, 0, 255),
                    (255, 255, 0),(0, 255, 255),(255, 0, 255),(128, 128, 128)]
    
    BRIGHTNESS_LIMIT = 128 # Below this value colour1 is applied and above this
                           # Value colour2 is applied
    
    # Replacing the colour texts by the respective colour codes
    for i in range(len(COLOUR_LIST)): 
        if colour1 == COLOUR_LIST[i]:
            colour1 = COLOUR_CODES[i]
        if colour2 == COLOUR_LIST[i]:
            colour2 = COLOUR_CODES[i]           
    
    altered_image = copy(image)
    
    
    for x,y, (r,g,b) in image:
        brightness = (r+g+b)/3
        # Checks the brighness value with the limit to decide which color to use
        if brightness >= BRIGHTNESS_LIMIT:
            new_colour = create_color(colour2[0], colour2[1], colour2[2])
        else:
            new_colour = create_color(colour1[0], colour1[1], colour1[2])       
        set_color(altered_image, x, y, new_colour)
    return altered_image


def three_tone (image: Image, colour1: str, colour2: str, colour3: str) -> Image:
    """Author: Benjamin Richards 
    Type Annotations: Cimpl.Image, str, str, str -> Cimpl.Image
    
    This function takes an image and three colours and creates a copy of the
    image using only those three colours. If the brightness is between 0 and 84
    the filter applies colour1, if it's between 85 and 170 it applies colour2 
    and above that it applies colour3
    
    >>> new = three_tone (original_image, 'black', 'white', 'lime')
    >>> show(new)
    (shows the image only made up only black, white, and lime)"""
    
    # Constants
    COLOUR_LIST = ["black","white","red","lime","blue","yellow","cyan","magenta"
                   ,"gray"]
    COLOUR_CODES = [(0,0,0),(255,255,255),(255,0,0),(0, 255, 0),(0, 0, 255),
                    (255, 255, 0),(0, 255, 255),(255, 0, 255),(128, 128, 128)]
    
    TOP_BRIGHTNESS_LIMIT = 171 # Above this value colour3 is applied
    MID_BRIGHTNESS_LIMIT = 85 # Between this value and TOP_BRIGHTNESS_LIMIT,
    # Colour2 is applied and below this value colour1 is applied
    
    # Replacing the colour texts by the respective colour codes    
    for i in range(len(COLOUR_LIST)):
        if colour1 == COLOUR_LIST[i]:
            colour1 = COLOUR_CODES[i]
        if colour2 == COLOUR_LIST[i]:
            colour2 = COLOUR_CODES[i]
        if colour3 == COLOUR_LIST[i]:
            colour3 = COLOUR_CODES[i]            
    
    altered_image = copy(image)
    
    
    for x,y, (r,g,b) in image:
        brightness = (r+g+b)/3
        # Checks the brighness value with the limit to decide which color to use        
        if brightness >= TOP_BRIGHTNESS_LIMIT:
            new_colour = create_color(colour3[0],colour3[1],colour3[2])
        elif brightness >= MID_BRIGHTNESS_LIMIT:
            new_colour = create_color(colour2[0],colour2[1],colour2[2])
        else:
            new_colour = create_color(colour1[0],colour1[1],colour1[2])       
        set_color(altered_image, x, y, new_colour)
    return altered_image


def sepia(image: Image) -> Image:
    """Author: Ian Holmes 
    Type Annotations: Cimpl.Image -> Cimpl.Image

    Return a new image with the sepia filter applied. The image is first 
    converted to gray using grayscale and then a yellow tint is added (The 
    grayscale is taken from the Cimple library)
    
    >>> new = sepia(image)
    >>> show(new)
    """
    
    #turning image to grayscale
    new_image = grayscale(image)
    
    #setting limits for which pixels are considered dark, medium, or light.
    DARK_GRAY_LIMIT = 63
    MEDIUM_GRAY_LIMIT = 191
    
    # Red value is multiplied is multiply by one of these factors depending on
    # The range in which it is located
    RED_FACTOR_LOW = 1.1 
    RED_FACTOR_MID = 1.15
    RED_FACTOR_HIGH = 1.08

    # Blue value is multiplied is multiply by one of these factors depending on
    # The range the red value is located at
    BLUE_FACTOR_LOW = 0.9
    BLUE_FACTOR_MID = 0.85
    BLUE_FACTOR_HIGH = 0.93   
    
    #tinting pixels yellow
    for x,y, (r,g,b) in new_image:
        # Depending on the red value the red value and the blue are multiplied
        # By a constant 
        if r < DARK_GRAY_LIMIT:
            r1,b1 = r * RED_FACTOR_LOW, b * BLUE_FACTOR_LOW
        elif r >= DARK_GRAY_LIMIT and r <= MEDIUM_GRAY_LIMIT:
            r1,b1 = r * RED_FACTOR_MID, b * BLUE_FACTOR_MID
        elif r > MEDIUM_GRAY_LIMIT:
            r1,b1 = r * RED_FACTOR_HIGH, b * BLUE_FACTOR_HIGH
            
        sepia = create_color(r1,g,b1)
        set_color(new_image, x, y, sepia)  
        
    return new_image


def _adjust_component (n: int) -> int:
    """ Author: Bardia Parmoun
    Type Annotations: int -> int

    This function takes the integer values of r, g, and b and determines the 
    range in which these values are located and returns the midpoint of that 
    range. This function is used for the posterize filter. The possible ranges 
    and their midpoints are: (The functions argument MUST be in range of 
    0<=x<=255).
    
    0 to 63 -> 31 
    64 to 127 -> 95
    128 to 191 -> 159
    192 to 255 -> 223
    
    >>> _adjust_component (12)
    31
    >>> _adjust_component (156)
    159
    """
    
    #Constants
    RANGE1_LOW = 0
    RANGE1_MID = 31
    RANGE2_LOW = 64
    RANGE2_MID = 95
    RANGE3_LOW = 128
    RANGE3_MID = 159
    RANGE4_LOW = 192
    RANGE4_MID = 223
    
    # Checks to see what range is n located in and returns the midpoint of that
    # Range. 
    if n >= RANGE4_LOW:
        return RANGE4_MID
    elif n >= RANGE3_LOW:
        return RANGE3_MID
    elif n >= RANGE2_LOW:
        return RANGE2_MID
    else:
        return RANGE1_MID


def posterize (image: Image) -> Image:
    """ Author: Bardia Parmoun 
    Type Annotations: Cimpl.Image -> Cimpl.Image

    This function takes a copy of an image and applies the posterize filter to 
    it. In other words, it will replace its rgb values with the midpoint value 
    of their range. This function uses the internal _adjust_component function
    to calculate the new rgb values
    
    >>> new=posterize (original_image)
    >>> show(new)
    (It will display the posterized version of the image)
    """
    
    new_image = copy(image)

    for x, y, (r,g,b) in image:
        # Every colour value is replaced with the midpoint of the range in which
        # It is located and uses _adjust_component to replace it with the 
        # Midpoint of that range
        new_colour = create_color(_adjust_component(r), _adjust_component(g),
                                  _adjust_component(b))
        set_color(new_image, x, y, new_colour)
    return new_image


def extreme_contrast(original_image: Image) -> Image:
    """ Author: Hao Lin 
    Type Annotations: Cimpl.Image -> Cimpl.Image

    This function applies the extreme contrast filter to the image. It converts
    the rgb values of every pixel to either 255 or 0 depending on their range.
    
    >>> new_image= extreme_contrast(original_image,10)
    >>> show(new_image)
    (Shows a version of the image after extreme contrast filter is applied)
    """
    # Constants
    RANGE_LOW =0
    RANGE_MID =127
    RANGE_HIGH =255
    
    HIGH_RED, LOW_RED = 255,0
    HIGH_BLUE, LOW_BLUE = 255,0
    HIGH_GREEN, LOW_GREEN = 255,0
    
    h = get_height(original_image)
    w = get_width(original_image)
    new_image = copy(original_image)
    
    for x in range(w):
        for y in range(h):
            r,g,b = get_color(original_image,x,y)
            
            # Based on the value of rgb they are either replaced with 0 or 255
            if r >= RANGE_LOW and r <= RANGE_MID:
                r = LOW_RED
            elif r > RANGE_MID and r <= RANGE_HIGH:
                r = HIGH_RED
                
            if g >= RANGE_LOW and g <= RANGE_MID:
                g=LOW_GREEN
            elif g>RANGE_MID and g <= RANGE_HIGH:
                g=HIGH_GREEN
                
            if b >= RANGE_LOW and b <= RANGE_MID:
                b = LOW_BLUE
            elif b > RANGE_MID and b <= RANGE_HIGH:
                b = HIGH_BLUE
                
            new_color = create_color(r,g,b)
            set_color(new_image, x,y, new_color)
    return new_image


def detect_edges (image: Image, threshold: float) -> Image:  
    """ Author: Hao Lin  
    Type Annotations: Cimpl.Image, float -> Cimpl.Image

    This function tries to find the edges of a given image by going through 
    every pixel and checking its brightness with the one below it. That 
    difference is compared with a given threshold value. In other words the 
    function will produce a black and white version of the image where the 
    background is white and the main parts of the image is black. 
    
    >>> new_image= detect_edge(original_image,10)
    >>> show(new_image)
    (Shows the new black and white image generated by detecting edges)
    """
    
    new_image = copy(image)
    
    #Constants
    WIDTH = new_image.get_width()
    HEIGHT = new_image.get_height()
    
    BACK = (255,255,255)
    EDGE = (0,0,0)
    
    for x in range (WIDTH):
        for y in range (HEIGHT-1):
            r,g,b = get_color(new_image,x,y)
            r_bottom,g_bottom,b_bottom=get_color(new_image,x,y+1)
            
            # Finds the brightness of the pixel and the one below it by taking
            # An average of their rgb values
            brightness = (r+g+b)/3
            brightness_bottom = (r_bottom+g_bottom+b_bottom)/3
            
            # If the difference between the brightness values is more than the
            # The threshold then it is replaced by the EDGE colour (black) and
            # Otherwise it is replaced with the BACK colour (white)
            if abs(brightness-brightness_bottom) > threshold:
                new_colour = create_color (EDGE[0],EDGE[1],EDGE[2])
            else:
                new_colour = create_color(BACK[0],BACK[1],BACK[2])
            set_color(new_image, x,y, new_colour)
            
        # The last row can't be compared with anything so it's set to BACK 
        # Automatically
        new_colour = create_color(BACK[0],BACK[1],BACK[2])
        set_color(new_image, x, HEIGHT-1, new_colour)        
    return new_image  


def detect_edges_better (image:Image, threshold: float) -> Image:  
    """ Author: Benjamin Richards 
    Type Annotations: Cimpl.Image, float -> Cimpl.Image

    This function tries to find the edges of a given image by going through 
    every pixel and checking its brightness with the one below and to the right
    of it. That difference is compared with a given threshold value. In other 
    words the function will produce a black and white version of the image where
    the background is white and the main parts of the image is black. 
    
    >>> new_image= detect_edge_better(copied_image,10)
    >>> show(new_image)
    (Shows the new black and white image generated by detecting edges)
    """
    
    new_image = copy(image)  
    
    # Constants
    WIDTH = new_image.get_width()
    HEIGHT = new_image.get_height()
    
    BACK = (255,255,255)
    EDGE = (0,0,0)
    
    for x in range (WIDTH):
        for y in range (HEIGHT):
            r,g,b = get_color(new_image,x,y)
            brightness = (r+g+b)/3
            
            # The default colour value is set to BACK (white). This value later
            # Can change to EDGE (black) if the difference exceeds the threshold
            new_colour = create_color(BACK[0],BACK[1],BACK[2])
            
            if y != HEIGHT-1 and x != WIDTH -1:  
                # Makes sure the range doesn't exceed the height and the width
                # Calculates the brightness of the pixel below it
                r_down,g_down,b_down = get_color(new_image,x,y+1)
                brightness_down = (r_down+g_down+b_down)/3
                
                r_right,g_right,b_right=get_color(new_image,x+1,y)
                brightness_right = (r_right+g_right+b_right)/3                 
                
                # Checks to see if the difference between the brightness values
                # Exceeds the threshold and if so converts it to black
                if (abs(brightness-brightness_down) > threshold or 
                    abs(brightness-brightness_right) > threshold):
                    new_colour= create_color (EDGE[0],EDGE[1],EDGE[2])
                    
            set_color(new_image, x, y, new_colour)
       
    return new_image 


def flip_horizontal (image: Image) -> Image:
    """ Author: Bardia Parmoun 
    Type Annotations: Cimpl.Image -> Cimpl.Image

    This function takes an image, makes a copy of it and then it flips it along
    the horizontal axis. It does that by swapping the colours of the pixels that
    are the same distance from the top and bottom of the image. 
    
    >>> new=flip_horizontal (original_image)
    >>> show(new)
    (It will display a version of the image that has been flipped along the 
    horizontal axis)
    """    
    
    new_image = copy(image)
    WIDTH = new_image.get_width()
    HEIGHT = new_image.get_height()
    
    for x in range (WIDTH):
        for y in range (HEIGHT//2): # Only half of the height is needed
            # Replaces the colour of the pixel with a pixel that is equally
            # Distant from the bottom of the image (Same x value but the y value
            # Becomes HEIGHT - y -1
            col1 = get_color(new_image,x,y)
            col2 = get_color(new_image,x,HEIGHT-y-1)
            set_color(new_image, x,y, col2)
            set_color(new_image, x,HEIGHT-y-1, col1)
    return new_image


def flip_vertical(image: Image) -> Image:
    """Author: Ian Holmes 
    Type Annotations: Cimpl.Image -> Cimpl.Image

    Return a copy of the inputted image, with the pixels flipped along the
    y axis. 
    
    >>> new = flip_horizontal(image)
    >>> show(new)
    """
    
    new_image = copy(image)
    
    width = get_width(image)
    height = get_height(image)
    
    for y in range(height):
        for x in range(width//2):
            # Replaces the colour of the pixel with a pixel that is equally
            # Distant from the right of the image (Same y value but the x value
            # Becomes WIDTH - x -1            
            col1 = get_color(new_image, x, y)
            col2 = get_color(new_image, width-x-1, y)
            set_color(new_image, x, y, col2)
            set_color(new_image, width-x-1,y, col1)
            
    return new_image


#Main Code      
# Assumption: There is a image stored in the same folder as this script
# with the given name

if __name__ == "__main__":      
    #Loading images 
    FILENAME_ORIGINAL = choose_file()
    original_image = load_image(FILENAME_ORIGINAL)
        
    print("Showing the original image")
    show(original_image)
    
    #Red Filter
    print("Applying the red filter")
    red_image=red_channel (original_image)
    show(red_image)
    
    #Green Filter
    print("Applying the green filter")
    green_image=green_channel (original_image)
    show(green_image)
    
    #Blue Filter
    print("Applying the blue filter")
    blue_image=blue_channel (original_image)
    show(blue_image)
    
    #Combining the Filters
    print("Applying the combined filter")
    combined_image=combine(red_image,green_image,blue_image)
    show(combined_image)
    
    # Two tone Filter    
    print("Applying the two tone filter")    
    two_tone_image=two_tone(original_image,"blue","red")
    show(two_tone_image)

    # Three tone Filter    
    print("Applying the three tone filter")    
    three_tone_image=three_tone(original_image,"black","white","lime")
    show(three_tone_image)
    
    # Sepia Filter    
    print("Applying the sepia filter")    
    sepia_image=sepia(original_image)
    show(sepia_image)
        
    # Posterize Filter
    print("Applying the posterize filter")
    posterized_image = posterize(original_image)
    show(posterized_image)
    
    # Extreme Contrast Filter
    print("Applying the extreme contrast filter")
    extreme_contrast_image = extreme_contrast(original_image)
    show(extreme_contrast_image)
    
    # Detect Edges Filter
    print("Applying the detect edges filter")
    detect_edges_image = detect_edges(original_image, 10)
    show(detect_edges_image)    
    
    # Detect Edges Better Filter
    print("Applying the detect edges better filter")
    detect_edges_better_image = detect_edges_better(original_image, 10)
    show(detect_edges_better_image)      
    
    # Flip Horizontal Filter
    print("Applying the flip horizontal filter")
    h_flipped_image=flip_horizontal (original_image)
    show(h_flipped_image)
    
    # Flip Vertical Filter
    print("Applying the flip vertical filter")
    v_flipped_image=flip_vertical (original_image)
    show(v_flipped_image)    
