import cv2

def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    features = classifier.detectMultiScale( # using the classifier do the following
        gray_img, # the image
        scaleFactor, # scale image - controls how small / large of a face can be detected
        minNeighbors # how many features need to be detected to confirm face
    )
    coords = []
    for (x, y, w, h) in features:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2);
        id, _ = clf.predict(gray_img[y : y + h, x : x + w])
        if id == 1:
            cv2.putText(img,"Carson", (x, y - 4), cv2.QT_FONT_NORMAL, 0.8, color, 1, cv2.LINE_AA)
        if id == 2:
            cv2.putText(img,"Juliana", (x, y - 4), cv2.QT_FONT_NORMAL, 0.8, color, 1, cv2.LINE_AA)
        coords = [x, y, w, h]
    
    return coords

def recognize(img, clf, faceCascade):
    color = {
        "blue":(255, 0, 0),
        "red":(0,0,255),
        "green":(0,255,0),
        "white":(255,255,255)
        }
    coords = draw_boundary(img, faceCascade, 1.1, 10, color["white"], "Face", clf)
    return img

def detect_person():
    faceCascade = cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("v2/classifier.yml")

    # 0 for default, -1 for external
    video_capture = cv2.VideoCapture(0)

    while True:
        _, img = video_capture.read()
        img = recognize(img, clf, faceCascade)
        
        cv2.imshow("face detection", img)
        
        # break loop of user preses q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    detect_person()