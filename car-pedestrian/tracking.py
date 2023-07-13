import cv2

# Load Image
img_file = "cars.jpg"

# Our Pre trained car classifier
classifier_file = "car_detector.xml"
# classifier_file = cv2.cv.Load("car_detection.xml")

# create opencv image
img = cv2.imread(img_file)

# convert to grayscale (needed for haar cascade)
black_n_white_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#create a car classifier
car_tracker = cv2.CascadeClassifier(classifier_file)

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

#Display the image with the faces spotted
# cv2.imshow("Car Test Image", black_n_white_img)
cv2.imshow("Car Test Image", img)
# To avoid autoclose (wait and listen for the close key)
cv2.waitKey() 

print("Code processing completed!")