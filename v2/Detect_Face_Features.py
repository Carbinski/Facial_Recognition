import cv2
def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale( # using the classifier do the following
        gray_img, # the image
        scaleFactor, # scale image - controls how small / large of a face can be detected
        minNeighbors # how many features need to be detected to confirm face
    )
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        cv2.putText(img ,text, (x, y - 4), cv2.QT_FONT_NORMAL, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    
    return coords

def detect(img, faceCascade, eyesCascade, noseCascade, mouthCascade):
    color = {
        "blue":(255, 0, 0),
        "red":(0,0,255),
        "green":(0,255,0),
        "white":(255,255,255)
        }
    coords = draw_boundary(img, faceCascade, 1.1, 10, color['blue'], "Face")

    # if face is detected
    if len(coords) == 4:
        # crop image to only have face
        x, y, w, h = coords
        roi_img = img[y : y + h, x : x + h]
        coords = draw_boundary(roi_img, eyesCascade, 1.1, 14, color['red'], "Eyes")
        coords = draw_boundary(roi_img, noseCascade, 1.1, 20, color['green'], "Nose")
        coords = draw_boundary(roi_img, mouthCascade, 1.1, 40, color['white'], "Mouth")

    return img

def detect_face_features():
    mouthCascade = cv2.CascadeClassifier("classifier/mouth.xml")
    noseCascade = cv2.CascadeClassifier("classifier/nose.xml")
    faceCascade = cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")
    eyesCascade = cv2.CascadeClassifier("classifier/haarcascade_eye.xml")

    # 0 for default, -1 for external
    video_capture = cv2.VideoCapture(0)

    while True:
        _, img = video_capture.read()
        img = detect(img, faceCascade, eyesCascade, noseCascade, mouthCascade)
        
        cv2.imshow("face detection", img)
        
        # break loop of user preses q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_face_features()