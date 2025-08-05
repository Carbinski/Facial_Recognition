from Create_Classification import train_classifier
from Dataset_Generation import run_dataset
from Detect_Face_Features import detect_face_features
from Detect_Person import detect_person


print("Welcome to facial detection and recognition controller")
print("Please select one of the following options")
print("0. Run Detect Facial Features\n" \
    "1. Run Facial Recognition and Classification\n" \
    "2. Create classification data\n" \
    "3. Generate classifier\n" \
    "4. Info")

selection = input()
valid_selection = False

while not valid_selection:
    selection = input()

    match selection:
        case "0":
            print("Running Facial Feature Detection")
            print("Press q to quit")
            valid_selection = True
            detect_face_features()
        case "1":
            print("Running Facial Recognition and Classification")
            print("Press q to quit")
            valid_selection = True
            detect_person()
        case "2":
            print("Running Generate Classifier")
            print("Please enter user ID")
            id = input()
            valid_selection = True
            run_dataset(id)
        case "3":
            print("Generating classifier")
            train_classifier()
            print("You should now be able to use Facial Recognition with your new data")
        case "4":
            print("I haven't made this yet!")

        case _:
            print("Invalid input! Please try again!")
