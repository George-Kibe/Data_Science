import cv2

# Load Image
img_file = "cars.jpg"
# load video
video = cv2.VideoCapture('Pedestrians.mp4')

# Our Pre trained car classifier
classifier_file = "pedestrians.xml"

#create a car classifier
pedestrian_tracker = cv2.CascadeClassifier(classifier_file)

# Run forever until car stops or something
while True:
    # read the current frame
    (read_successful, frame) = video.read()
    print(read_successful, frame)
    
    # Safe coding
    if read_successful: 
        # must convert to grayscale
        grayscaled_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    else:
        break
    # Detect cars
    pedestrians = pedestrian_tracker.detectMultiScale(grayscaled_frame)
    # draw rectangles in the car frames
    for pedestrian in pedestrians:
        (x,y,w,h) = pedestrian
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 255), 2)
    #Display the image with the pedestrians spotted
    # cv2.imshow("Car Test Image", black_n_white_img)
    cv2.imshow("Car Moving", frame)
    # To avoid autoclose (wait and listen for the close key)
    cv2.waitKey(1) 
