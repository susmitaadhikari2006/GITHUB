import cv2
import numpy

def draw_vertical_line(image):
    height, width, _ = image.shape
    # Calculate the coordinates for the middle of the screen
    middle_x = width // 2
    # Draw the vertical line
    cv2.line(image, (middle_x, 0), (middle_x, height), (0, 0, 255), 2)
    return middle_x
    
    
cam = cv2.VideoCapture(0)

while True:
    ret, frame = cam.read()
    width = int(cam.get(3))
    height = int(cam.get(4))
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Define range of orange color in HSV
    lower_orange = numpy.array([0, 102, 204])
    upper_orange = numpy.array([20, 255, 255])
    
    # Threshold the HSV image to get only orange colors
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    
    # Find contours in the mask
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    middle = draw_vertical_line(frame)
    
    
    # Draw bounding rectangles around detected orange items
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        width = w
        height = h
        area = width * height
        ratio = w/h
        height_s, width_s, _ = frame.shape
        if((width >= height*2) and (area > 3000)):
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, f'Width: {width}, Height: {height}, Area: {area}', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

            # Draw a circle at the centroid
            cv2.circle(frame, (height, width), 7, (255, 255, 255), -1)
                
             # Calculate distance between the two points (center of screen and centroid)
            distance = numpy.sqrt((height_s - width_s // 2) ** 2 + (width_s - height // 2) ** 2)

    cv2.imshow('FRC Image Processing', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
