import os
import sys
import cv2
import numpy as np
import logging

MODEL_FILE = "model.mdl"
  
def detect(img, cascade):
  gray = to_grayscale(img)
  rects = cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=2, minSize=(15, 15), flags = cv2.CASCADE_SCALE_IMAGE)
  
  if len(rects) == 0:
    return []
  return rects
  #haarcascade_frontalface_alt.xml
  #haarcascade_fullbody.xml
def detect_faces(img):
  cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
  return detect(img, cascade)
  
def to_grayscale(img):
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  gray = cv2.equalizeHist(gray)
  return gray
  
def contains_face(img):
  return len(detect_faces(img)) > 0
  
def save(path, img):
  cv2.imwrite(path, img)
  
def crop_faces(img, faces):
  for face in faces:
    x, y, h, w = [result for result in face]
    return img[y:y+h,x:x+w]

