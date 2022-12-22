import cv2
import numpy as np

# Deze functie neemt als argument een cv2 frame, en minimaal een hue en een delta hue en berekend het massamiddelpunt.
def calculate_cm(frame, hue0, delta_hue, smin=30, smax = 255, vmin = 100, vmax = 255):

    frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    hue_fac = 180/255 
    hmin = hue_fac*(hue0 - delta_hue)
    hmax = hue_fac*(hue0 + delta_hue)
    lower = np.array([np.maximum(0,hmin),smin,vmin])
    upper = np.array([np.minimum(180,hmax),smax,vmax])

    if hmin<0:
        mask=cv2.inRange(frame_hsv,lower,upper)+\
        cv2.inRange(frame_hsv,
                    np.array([np.mod(hmin,180.),smin,vmin]),
                    np.array([180.,smax,vmax]))
    elif hmax>180:
        mask=cv2.inRange(frame_hsv,lower,upper)+\
        cv2.inRange(frame_hsv,
                    np.array([0.,smin,vmin]),
                    np.array([np.mod(hmax,180.),smax,vmax]))
    else:
        mask=cv2.inRange(frame_hsv,lower,upper)
    
    res=cv2.bitwise_and(frame,frame,mask=mask)

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[-2]

    # Test for presence of contours
    if len(cnts) == 0:
        # If not present (object has left image plane or is otherwise not found),
        # set position to [-1,-1]
        pos=[[-1,-1]]
    else:
        # Otherwise pick the contour with largest enclosed area and 
        # determine 'center of mass' (CM)
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        center = ((M["m10"] / M["m00"]), M["m01"] / M["m00"])
        pos=np.array([center])

    return(pos)


