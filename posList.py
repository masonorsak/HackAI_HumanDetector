import os
import cv2 

for file in os.listdir('.'):
    print(file)
    file1 = open("MyFile.txt","a")

    img = cv2.imread(file)
    dim = img.shape

    file1.write(file + ' 1 0 0 ' + str(dim[1]) + ' ' + str(dim[0]) + '\n')
    file1.close()