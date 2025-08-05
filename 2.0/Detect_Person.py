import cv2

def generate_dataset(img, id, img_id):
    # save detected image
    cv2.imwrite("2.0/data/user." + str(id) + "." + str(img_id) + ".jpg", img)


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

def detect(img, faceCascade, eyesCascade, noseCascade, mouthCascade, img_id):
    coords = draw_boundary(img, faceCascade, 1.1, 10, (255, 0, 0), "Face")

    # if face is detected
    if len(coords) == 4:
        # crop image to only have face
        x, y, w, h = coords
        roi_img = img[y : y + h, x : x + h]

        user_id = 1

        # save every 4 images
        if img_id % 4 == 0:
            generate_dataset(roi_img, user_id, img_id)

    return img

mouthCascade = cv2.CascadeClassifier("classifier/mouth.xml")
noseCascade = cv2.CascadeClassifier("classifier/nose.xml")
faceCascade = cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")
eyesCascade = cv2.CascadeClassifier("classifier/haarcascade_eye.xml")

clf = cv2.face.LBPHFaceRecognizer_create()
clf.read("2.0/classifier.yml")

# 0 for default, -1 for external
video_capture = cv2.VideoCapture(0)

img_id = 0

while True:
    _, img = video_capture.read()
    img = recognize(img, clf, faceCascade)
    
    cv2.imshow("face detection", img)
    img_id += 1
    
    # break loop of user preses q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()