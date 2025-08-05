Setup:

Install the following in the root folder
'''
pip install cv2
pip install numpy
pip install pillow
'''
If you are having issues ask chatGPT
Current I am working out of v2, you can ignore v1.

Also sometimes the code just doesn't work so try running it twice!

Usage:
Go into Dataset_Generation.py and set the id to a unique number. Then have the person you want to add to the dataset step into frame and run the code for some time. This will detect their face and take pictures of it and save it into v2/data/ with an according name. Do this with a unique id number for all the people you want in the data set. Also go back in and clean up the data if it is not working well (the face detection may have false positives)

Following this, use Create_Classification.py. This will create a new classifier.yml that should be able to detect the people you have added during the dataset generation step. Naturally the more data in dataset generation the better the performance should be in theory. I think around ~15 - 30 seconds works well enough

Finally use Detect_Person.py. The box around your face should have your respective name above it. Currently the id system is hard coded so you will have to go into the draw_boundary function and add more if id == x: statements.

I've made a controller.py to let you use the code but its buggy rn so best of luck! Also Detect_Face_Features.py is just there for fun and proof of the face detection working.
