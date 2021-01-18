ChangeItUp Version 1.0 by Py Eaters!

Released on: 04/07/2020
Price: $15.99  
______________________________________________________________________________________

Contact information 
______________________________________________________________________________________
- Project leader: Bardia Parmoun
- Email Address: bardiaparmoun@pyeaters.com

Websites for additional informations and supports:
- ECOR 1051 course web address in cuLearn (https://culearn.carleton.ca/moodle/course/view.php?id=144561) 

- Carleton Engineering and Design web address (https://carleton.ca/engineering-design/)

- Carleton Systems and Computer Engineering web address (https://carleton.ca/sce/) 
______________________________________________________________________________________

DESCRIPTION
______________________________________________________________________________________
- This software is a photo editing program. Various filters
 can be applied to an image to alter it for a desired
 appearance.
- The software contains 13 different filters including:
red_channel, blue_channel, green_channel, combine, two_tone,
three_tone, extreme_contrast, posterize, tint sepia, detect_edges,
detect_edges_better, flip_horizontal, and flip_vertical

*red_channel, blue_channel, green_channel, and combine are not
included in the user interface but are accessbile through the 
main code* 

The program has multiple files:
The executable files:
- T64_batch_ui.py		--> The batch userinterface
- T64_interactive_ui.py 	--> the text-based userinterface

The supporting files:
- Cimpl.py			--> The main library for the program
- simple_Cimpl_filters.py	--> Some supporting functions for the program
- T64_image_filters.py		--> The file that contains all the filters
______________________________________________________________________________________

INSTALLING UNDER WINDOWS 10
______________________________________________________________________________________
To use this program, you must first ensure you have the 
most recent versions of Python and Pillow installed. 
This can be done through the windows command prompt.

Installing Python 3.8.1:
Make sure you download the latest version of Python from:
https://www.python.org/

Installing pip 20.0.2:
Make sure the latest version of pip is installed by typing
the following in the command prompt: 
python get-pip.py

Installing Pillow 7.0.0:
Next you need to install Pillow:
Go to: https://pypi.org/project/Pillow/
or type: python –m pip install --upgrade pillow

Finally make sure you download the Cimpl library version 1.04:
https://culearn.carleton.ca/moodle/mod/folder/view.php?id=1600897

Finally make sure you have downloaded some sort of an IDE so run the program such as
Wing 101 7.2.2
https://wingware.com/downloads/wing-pro

You are now ready to use the program just make sure Cimpl is 
located in the same folder as the program.
______________________________________________________________________________________

INSTALLING UNDER MacOS
______________________________________________________________________________________
The same process as installing under WINDOWS 10 except since 
MacOS already has a version of Python installed make sure to 
install Python3 and change the commands from Python to Python3.

Also note that the MacOS version of this program is slightly 
different in the way that the user will not be able to choose
their image by selecting it and instead they need to enter the
name of the image.
______________________________________________________________________________________
 
USAGE
______________________________________________________________________________________
There are two different ways to use this program. One is through
the interactive user interface and one is through the batch user
interface. 

1. Open your an apporpriate IDE (e.g. Wing 101)
2. Open the program files (T64_interactive_ui and T64_batch_ui)

3. Using the interactive user interface: 
By running the program the user is presented with a list of options
that they can choose from. The user will load the image by entering 
either 'L' or 'l' and then they can apply the various filters and at
the end the image will be saved by calling the save-as using 'S' or 's'. 
The filters can be called by putting the first letter of their name (the
letter before the ')'. Both the lowercase and uppercase versions of those
letters are accepted.

>>> L)oad image    S)ave_as
2)-tone    3)-tone    X)treme contrast    T)int sepia    P)osterize
E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip
Q)uit
: 'L'
(the user will choose an image)

>>> L)oad image    S)ave_as
2)-tone    3)-tone    X)treme contrast    T)int sepia    P)osterize
E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip
Q)uit
: 'X'
(The extreme contrast filter is applied)

>>> L)oad image    S)ave_as
2)-tone    3)-tone    X)treme contrast    T)int sepia    P)osterize
E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip
Q)uit
: 'S'
>>> Enter the filename (no extension needed): 'new_image'
(The image is saved as 'new_image.jpg' in the same folder as the program)

>>> L)oad image    S)ave_as
2)-tone    3)-tone    X)treme contrast    T)int sepia    P)osterize
E)dge detect    I)mproved edge detect    V)ertical flip    H)orizontal flip
Q)uit
: 'Q'
(The program finishes executing)

4. Using the batch user interface: 
This program works by reading a list of commands from a '.txt' file and applying 
the filters to the image. Every line of that text file should 3 main things:
1. The name of the image to apply the filter to
2. The name to save the new image as
3. A list of commands to apply to the image

For example: miss_sullivan.jpg test1.jpg 2 X P
*Note that the image that the filter is being applied to and the text file must 
be in the same folder as the program*

After running the program the user can simply enter the name of the txt file and the
program will do the rest:
>>> Enter your filename: 'sample_batch_file.txt'
(The program will apply the commands and save the images in the same folder)

*The 'sample_batch_file.txt' is included with the program as an example*

*Note that in order for the software to works properly the files 'Cimpl.py'
'T64_image_filters.py' 'simple_Cimpl_filters.py' 'T64_interactive_ui.py' and 
'T64_batch_ui.py' must be located in the same folder*

Using the program with the Command Prompt commands:
First go to the directory that the program is located in
For example: cd C:\Users\Username\Desktop\P8

Now you can run each program using the Python command:
For example:
python T64_interactive_ui.py --> runs the interactive user interface program
python T64_batch_ui.py --> runs the batch user interface program
______________________________________________________________________________________

CREDITS
______________________________________________________________________________________
Author: Bardia Parmoun
Coding: combine, adjust_component, posterize, flip_horizontal, _find_filter and
apply_filter for the interactive user interface 

Testing: combine, extreme_contrast, flip_vertical

Author: Hao Lin
Coding: green_channel, extreme_contrast, detect_edges, and read_file for the 
batch user interface

Testing: green_channel, posterize, detect_edges_better

Author: Benjamin Richards
Coding: red_channel, two_tone, three_tone, detect_edges_better, and apply_filter for 
the batch user interface

Testing: red_channel, sepia, detect_edges

Author: Ian Holmes
Coding: blue_channel, sepia, flip_vertical, get_command and open_image for the
interactive user interface 

Testing: blue_channel, two_tone, three_tone, flip_horizontal
______________________________________________________________________________________

LICENSE
______________________________________________________________________________________
MIT License

Copyright (c) [2020] [Py Eaters]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.