import cv2

def generate_dataset(img, id, img_id):
    # save detected image
    cv2.imwrite("v2/data/user." + str(id) + "." + str(img_id) + ".jpg", img)

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

def detect(img, faceCascade, img_id, id):
    coords = draw_boundary(img, faceCascade, 1.1, 10, (0,255,0), "Face")

    # if face is detected
    if len(coords) == 4:
        # crop image to only have face
        x, y, w, h = coords
        roi_img = img[y : y + h, x : x + h]

        # TODO: Manually update user_id when adding new people
        user_id = 2

        # save every 4 images
        if img_id % 4 == 0:
            generate_dataset(roi_img, user_id, img_id)

    return img

def run_dataset(id):
    faceCascade = cv2.CascadeClassifier("classifier/haarcascade_frontalface_default.xml")

    # 0 for default, -1 for external
    video_capture = cv2.VideoCapture(0)

    img_id = 0

    while True:
        _, img = video_capture.read()
        img = detect(img, faceCascade, img_id, id)
        
        cv2.imshow("face detection", img)
        img_id += 1
        
        # break loop of user preses q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    video_capture.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # set user ID
    id = 1
    run_dataset(id)