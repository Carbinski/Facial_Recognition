import cv2
import json
import time
from collections import defaultdict
import ResponseController 
import tts

counts = defaultdict(int)

def loadIDs() -> dict:
    filepath = "v2/users.json"

    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            return data
    except json.JSONDecodeError:
        print("No data in JSON file!")
        return {}

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

        counts[id] += 1

        all_users = loadIDs()
        for userID, name in all_users.items():
            if str(id) == userID:
                cv2.putText(img, name, (x, y - 4), cv2.QT_FONT_NORMAL, 0.8, color, 1, cv2.LINE_AA)
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

    start_time = time.time()

    is_canceled = False

    # wait for face to appear in frame
    while True and not is_canceled:
        _, img = video_capture.read()
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = faceCascade.detectMultiScale(
            gray_img,
            1.1,
            10
        )
        
        cv2.imshow("waiting for face", gray_img)

        if cv2.waitKey(1) & len(features) > 0:
            break
        
        # break loop of user preses q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            is_canceled = True
            break

    while True and not is_canceled:
        _, img = video_capture.read()
        img = recognize(img, clf, faceCascade)

        cv2.imshow("face detection", img)
        
        # breaks loop after 5 seconds
        if time.time() - start_time > 5:
            break

        # break loop of user preses q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            is_canceled = True
            break

    video_capture.release()
    cv2.destroyAllWindows()

    faceCascade = cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

    clf = cv2.face.LBPHFaceRecognizer_create()
    clf.read("v2/classifier.yml")

    # 0 for default, -1 for external
    video_capture = cv2.VideoCapture(0)

    video_capture.release()
    cv2.destroyAllWindows()



def determine_action(id: int):
    people = loadIDs()

    greeting = "Welcome, " + people[str(id)] + "!"
    tts.run_tts(greeting)
    # match id :
    #     case 1:
    #         ResponseController.report_weather()
    #     case 2:
    #         ResponseController.report_news("space", 3)
    #     case 3:
    #         ResponseController.report_news("top", 3)

def respond_person():
    detect_person()

    curr_id = 0
    max_count = 0
    for id, count in counts.items():
        if count > max_count:
            curr_id = id 
            max_count = count

    determine_action(curr_id)

def respond_person_infinite():
    respond_person()
    time.sleep(10)
    respond_person()


if __name__ == "__main__":
    respond_person_infinite()