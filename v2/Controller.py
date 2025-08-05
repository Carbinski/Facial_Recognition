from Create_Classification import train_classifier
from Dataset_Generation import run_dataset
from Detect_Face_Features import detect_face_features
from Detect_Person import detect_person

def print_menu():
    print("\n" + "="*50)
    print("Welcome to the Facial Detection & Recognition Controller")
    print("="*50)
    print("Please select one of the following options:\n")
    print("  0. Run Detect Facial Features")
    print("  1. Run Facial Recognition and Classification")
    print("  2. Create Classification Data")
    print("  3. Generate Classifier")
    print("="*50)

print_menu()
valid_selection = False

while not valid_selection:
    selection = input("Enter your selection (0–4): ").strip()

    match selection:
        case "0":
            print("\n[INFO] Running Facial Feature Detection...")
            print("      → Press 'q' to quit.\n")
            valid_selection = True
            detect_face_features()

        case "1":
            print("\n[INFO] Running Facial Recognition and Classification...")
            print("      → Press 'q' to quit.\n")
            valid_selection = True
            detect_person()

        case "2":
            print("\n[INFO] Creating Classification Data")
            id = input("Enter User ID: ").strip()
            name = input("Enter USer Name: ").strip()
            valid_selection = True
            run_dataset(id, name)

        case "3":
            print("\n[INFO] Generating Classifier...")
            train_classifier()
            print("Classifier generated successfully.")
            print("You can now run Facial Recognition with your new data.\n")

        case _:
            print("\nInvalid input! Please enter a number between 0 and 4.\n")