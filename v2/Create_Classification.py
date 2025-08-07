import os
import cv2
import numpy as np
from PIL import Image

def train_classifier(data_dir):
    # path to all data
    path = [os.path.join(data_dir, f) for f in os.listdir(data_dir)]
    faces = []
    ids = []

    for image in path:
        # skip any hidden files in folder
        if os.path.basename(image).startswith('.'):
            continue
        
        # format images correctly
        img = Image.open(image).convert('L')
        imageNp = np.array(img, 'uint8')
        # get corresopnding id from image
        id = int(os.path.split(image)[1].split(".")[1])

        faces.append(imageNp)
        ids.append(id)

    ids = np.array(ids)
    
    # train model
    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.train(faces, ids)
    clf.write("v2/classifier.yml")

if __name__ == "__main__":
    train_classifier("v2/data")