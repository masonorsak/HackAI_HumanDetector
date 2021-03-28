# HackAI Human Detector
Using a Haar cascade trained using thousands of images and OpenCV, this project can detect humans from a live video feed. See the project demo [here](https://www.youtube.com/watch?v=LOR-_iQCrAc).

## How To Run
Note: while almost all (see note below) files and folders needed for the creation of this project were included here, only HumanDetector.py and HumanHaar.xml are needed for the program to run.

Ensure you have [Python 3](https://www.python.org/download/releases/3.0/) and [OpenCV](https://opencv.org/) installed on your windows system. Download or clone the source code and navigate to the source code location in your terminal. Then simply run the program by envoking the HumanDetector.py file like so:
```
cd C:\Users\Mason\Desktop\UTD Spring 2021\HackAI
python HumanDetector.py
```
Note: a video camera connected to your computer is required for this to work.

## Sources
This Haar cascade was built using [this fantastic paper](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Creating_a_Cascade_of_Haar-Like_Classifiers_Step_by_Step.pdf) from the University of Auckland. Some of the tools seen on this repo like createsamples.exe and haartraining.exe is written by them. For a full list of tools used in this project created by the University of Auckland visit [this link](https://www.cs.auckland.ac.nz/~m.rezaei/Tutorials/Haar-Training.zip).

The positive images used to create this Haar cascade weere taken from the Chinese University of Hong Kong CUHK01 manually cropped images which can be found [here](https://www.ee.cuhk.edu.hk/~xgwang/CUHK_identification.html).

The negative images that contain no humans were borrowed from [this github repo](https://github.com/handaga/tutorial-haartraining/tree/master/data/negatives).

For more information about the theory behind cascade classifier training please see the OpenCV website [here](https://docs.opencv.org/master/db/d28/tutorial_cascade_classifier.html)

Note: positive and negative image folders and the Haar cascade tools from the University of Auckland were excluded from this repo because they were simply too large of folders to upload. Please see the above links for where the original source material can be found.
