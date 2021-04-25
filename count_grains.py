
import cv2
import numpy as np
import argparse

#Constructing the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image_path", required=True, help="path to input image")
args = vars(ap.parse_args())

def main():

  #Reading image
  image = cv2.imread(args['image_path'],0) #Reading it in a gray scale
  image = cv2.resize(image,(512,512)) #Resizing it

  #Adaptive Thresholding with ADAPTIVE_THRESH_MEAN_C
  output_adapthresh = cv2.adaptiveThreshold (image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 51, -20.0)

  #Finding contours from outpur adapthreshold image and that contours will be rice grains
  contours, _ = cv2.findContours(output_adapthresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

  n_rice_grain = len(contours)
  print('Total number of rice grains:',n_rice_grain)

  #Finding percentage of broken rice grains
  broken_grain_theshold = 48
  n_broken_rice_grain = 0
  for cnt in contours:
    temp = cv2.contourArea(cnt)
    if temp < broken_grain_theshold:
      n_broken_rice_grain += 1

  per = n_broken_rice_grain*100/n_rice_grain
  print('Total percentage of broken rice grains:','%.2f' % per,'%')

if __name__=="__main__":
    main()