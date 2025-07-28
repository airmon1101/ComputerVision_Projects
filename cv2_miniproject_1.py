import cv2

# Image loading
# image = cv2.imread(str(input("Enter your image Path here --> ")))
image = cv2.imread("/home/dhruv/New_cv2_project/YT_cv2/whitw_image.jpeg")

if image is not None:
    print("Error image could load!")
else:
    print("Image is loaded successfully")


# user input 
while True:
    print('\n')
    print("_______________________________________________Menu_________________________________________________")
    print('\n')
    print("1. Draw a line.")
    print("2. Draw circle.")
    print("3. Draw rectrangle ")
    print("4. Draw or Add Text")
    print("5. For exit()")
    choice = str(input("Enter your choice here: "))
    print('\n')

    match choice:
        case '1':
            # 2. Ask the user for two points as “x,y”
            pt1_input = input("Enter first point (x,y), e.g. 50,200: ")
            pt2_input = input("Enter second point (x,y), e.g. 300,400: ")

            # 3. Convert the strings into integer tuples
            #    - Remove parentheses if any, split at comma, convert to int
            pt1_parts = pt1_input.replace("(", "").replace(")", "").split(",")
            pt2_parts = pt2_input.replace("(", "").replace(")", "").split(",")

            # 4. Build the tuples
            pt_1 = (int(pt1_parts[0]), int(pt1_parts[1]))
            pt_2 = (int(pt2_parts[0]), int(pt2_parts[1]))

            print(f"Drawing line from {pt_1} to {pt_2}...")

            # 5. Draw the line (BGR color = red here, thickness = 3)
            color = (0, 0, 255)   # Red in BGR format
            thickness = 3
            lined_image = cv2.line(image, pt_1, pt_2, color, thickness)

            # Show the image
            cv2.imshow("Lined Image", lined_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

            # save or not 
            user_preferences = str(input("You want to save this output Image ? [y/n]: "))
            if user_preferences == 'y':
                cv2.imwrite("output_with_line.jpg", lined_image)
                print("Saved as output_with_line.jpg")
            else:
                print("Thak You!")


        case '2':
            center_input = input("Enter center e.g 50,50: ")
            center_parts = center_input.replace("(", "").replace(")", "").split(",")
            center = (int(center_parts[0]), int(center_parts[1]))


            circle_img = cv2.circle(image, center, 50, (255,0,0), 3)
            cv2.imshow("Circle image", circle_img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()


            # save or not 
            user_preferences = str(input("You want to save this output Image ? [y/n]: "))
            if user_preferences == 'y':
                cv2.imwrite("output_with_circle.jpg", circle_img)
                print("Saved as output_with_circle.jpg")
            else:
                print("Thak You!")

        case '3':
            # rectrangle
            # 2. Ask the user for two points as “x,y”
            pt1_input = input("Enter first point (x,y), e.g. 50,200: ")
            pt2_input = input("Enter second point (x,y), e.g. 300,400: ")

             # 3. Convert the strings into integer tuples
            #    - Remove parentheses if any, split at comma, convert to int
            pt1_parts = pt1_input.replace("(", "").replace(")", "").split(",")
            pt2_parts = pt2_input.replace("(", "").replace(")", "").split(",")

             # 4. Build the tuples
            pt_1 = (int(pt1_parts[0]), int(pt1_parts[1]))
            pt_2 = (int(pt2_parts[0]), int(pt2_parts[1]))


            color = (0,0,255)
            thickness = 3
            rectangle_image = cv2.rectangle(image, pt_1, pt_2, color, thickness )

            if rectangle_image is None:
                print("Error")
            else:
                cv2.imshow("Rectrangle Image", rectangle_image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()

                # save or not 
            user_preferences = str(input("You want to save this output Image ? [y/n]: "))
            if user_preferences == 'y':
                cv2.imwrite("output_with_circle.jpg", circle_img)
                print("Saved as output_with_circle.jpg")
            else:
                print("Thak You!")

        case '4':
            # Adding text to the image

            if image is None:
                print("Error")
            else: 
                text = str(input("Enter your message here: "))
                color = (255,0,0)
                thickness = 4
    
                # Input the org 
                org_input = input("Enter first point (x,y), e.g. 50,200: ")
                org_parts = org_input.replace("(", "").replace(")", "").split(",")
                org = (int(org_parts[0]), int(org_parts[1]))
    
                add_text = cv2.putText(image, text, org, cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, thickness )

                if add_text is None:
                    print("Error")

                else:
                    cv2.imshow("Adding Text Image", add_text)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

             # save or not 
            user_preferences = str(input("You want to save this output Image ? [y/n]: "))
            if user_preferences == 'y':
                cv2.imwrite("output_with_circle.jpg", circle_img)
                print("Saved as output_with_circle.jpg")
            else:
                print("Thak You!")
                
        case '5':
            exit() 
        case _ :
            print("Invalid Choice Try Agin ! \n")


