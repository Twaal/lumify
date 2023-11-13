import cv2

def main():
    # Open the default camera (usually camera index 0)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Couldn't open the webcam.")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()

        if not ret:
            print("Error: Couldn't read frame from the webcam.")
            break

        # Process frame
        #--- TODO 
        edges = cv2.Canny(frame,100,200)
        # Display the frame
        cv2.imshow('Webcam', edges)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close the window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()