import cv2
import os

def get_image_path():
    """Get and validate image file path from user"""
    while True:
        image_path = input("Enter the path to your image file: ").strip()
        
        if os.path.exists(image_path):
            # Check if it's a valid image file extension
            valid_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.tif']
            if any(image_path.lower().endswith(ext) for ext in valid_extensions):
                return image_path
            else:
                print("Error: Please provide a valid image file (jpg, jpeg, png, bmp, tiff)")
        else:
            print("Error: File not found. Please check the path and try again.")

def load_classifiers():
    """Load Haar cascade classifiers"""
    try:
        # Use OpenCV's built-in cascade files
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        if face_cascade.empty() or eye_cascade.empty():
            print("Error: Could not load cascade classifiers")
            return None, None
        
        print("Face detection models loaded successfully")
        return face_cascade, eye_cascade
    
    except Exception as e:
        print(f"Error loading classifiers: {e}")
        return None, None

def detect_faces(image, face_cascade, eye_cascade):
    """Detect faces and eyes in the image"""
    # Convert to grayscale for detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    print(f"Found {len(faces)} face(s) in the image")
    
    # Draw rectangles around faces and detect eyes
    for (x, y, w, h) in faces:
        # Draw yellow rectangle around face
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 0), 2)
        
        # Create regions of interest for eye detection
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = image[y:y+h, x:x+w]
        
        # Detect eyes within the face region
        eyes = eye_cascade.detectMultiScale(roi_gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20))
        
        # Draw blue-green rectangles around eyes
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 127, 255), 2)
    
    return image

def display_image(image, window_title="Face Detection Result"):
    """Display image and wait for user to close window"""
    cv2.imshow(window_title, image)
    print("Image displayed. Close the window to continue...")
    cv2.waitKey(0)  # Wait indefinitely for any key press
    cv2.destroyAllWindows()

def get_save_choice():
    """Get user's choice to save the image"""
    while True:
        choice = input("Do you want to save the processed image? (y/n): ").strip().lower()
        
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no")

def save_image(image, original_path):
    """Save the processed image"""
    try:
        # Generate default output filename
        base_name = os.path.splitext(os.path.basename(original_path))[0]
        extension = os.path.splitext(original_path)[1]
        default_name = f"{base_name}_face_detected{extension}"
        
        # Ask user for output filename
        save_path = input(f"Enter filename to save (press Enter for '{default_name}'): ").strip()
        
        if not save_path:
            save_path = default_name
        
        # Add extension if not provided
        if not os.path.splitext(save_path)[1]:
            save_path += extension
        
        # Save the image
        success = cv2.imwrite(save_path, image)
        
        if success:
            print(f"Image saved successfully as: {save_path}")
        else:
            print("Error: Failed to save the image")
            
    except Exception as e:
        print(f"Error saving image: {e}")

def main():
    """Main function to run the face detection program"""
    print("=== Face Detection Program ===")
    print("This program detects faces in an image and allows you to save the result.\n")
    
    try:
        # Step 1: Get image path from user
        image_path = get_image_path()
        
        # Step 2: Load the image
        print("Loading image...")
        image = cv2.imread(image_path)
        
        if image is None:
            print("Error: Could not load the image. Please check the file format.")
            return
        
        print("Image loaded successfully")
        
        # Step 3: Load classifiers
        face_cascade, eye_cascade = load_classifiers()
        
        if face_cascade is None or eye_cascade is None:
            print("Cannot proceed without face detection models")
            return
        
        # Step 4: Detect faces and eyes
        print("Processing image for face detection...")
        processed_image = detect_faces(image.copy(), face_cascade, eye_cascade)
        
        # Step 5: Display the result
        display_image(processed_image)
        
        # Step 6: Ask user if they want to save
        if get_save_choice():
            save_image(processed_image, image_path)
        else:
            print("Image not saved.")
        
        print("Program completed successfully!")
        
    except KeyboardInterrupt:
        print("\nProgram interrupted by user")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
