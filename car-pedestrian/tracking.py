import cv2

# Load Image
img_file = "cars.jpg"
# load video
video = cv2.VideoCapture('Tesla.mp4')

# Our Pre trained car classifier
classifier_file = "car_detector.xml"
# classifier_file = cv2.cv.Load("car_detection.xml")

#create a car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

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
    cars = car_tracker.detectMultiScale(grayscaled_frame)
    # draw rectangles in the car frames
    for car in cars:
        (x,y,w,h) = car
        cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 0, 255), 2)
    #Display the image with the cars spotted
    # cv2.imshow("Car Test Image", black_n_white_img)
    cv2.imshow("Car Moving", frame)
    # To avoid autoclose (wait and listen for the close key)
    cv2.waitKey(1) 

"""
# create opencv image
img = cv2.imread(img_file)

# convert to grayscale (needed for haar cascade)
black_n_white_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect cars
cars = car_tracker.detectMultiScale(black_n_white_img)
# print(cars)
# a list of all detected objects, x, y, width, height

# Draw rectangles around the detected cars
# car = cars[0]
# (x,y,w,h) = car
# cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

for car in cars:
    (x,y,w,h) = car
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0, 255), 2)

#Display the image with the cars spotted
# cv2.imshow("Car Test Image", black_n_white_img)
cv2.imshow("Car Test Image", img)
# To avoid autoclose (wait and listen for the close key)
cv2.waitKey(10) 

"""
print("Code processing completed!")