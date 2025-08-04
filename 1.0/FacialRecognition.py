import cv2

# Detect faces from test-image picture and store them under the stored-faces folder

# loading the haar case algorithm file into alg variable
alg = "content/haarcascade_frontalface_default.xml"

# passing algorithm to OpenCV
haar_cascade = cv2.CascadeClassifier(alg)

# loading image path into file_name variable
file_name = "content/proxy-image.png"

# reading the image
img = cv2.imread(file_name)

# creating a black and white image
img_bw = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)

# detecting faces
faces = haar_cascade.detectMultiScale(
    img_bw, # the image
    scaleFactor = 1.1, # compression amount
    minNeighbors=10, # how many neighboring faces to find when it finds one
    minSize=(100, 100) # minimum size in pixels of a face
)


for i, (x, y, w, h) in enumerate(faces):
    # cropping the face
    face_img = img[y:y+h, x:x+w]
        # loading the target image path into target_file_name variable
    cv2.imwrite(f'stored-faces/{i}.jpg', face_img,)
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Detected Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()