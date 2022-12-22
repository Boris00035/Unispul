import cv2
import numpy as np

cap = cv2.VideoCapture(0)

fps = cap.get(cv2.CAP_PROP_FPS)

while(True):
    ret, frame = cap.read()
  
    # Display the resulting frame
    cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()