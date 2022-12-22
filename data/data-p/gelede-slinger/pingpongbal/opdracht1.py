import cv2
import numpy as np

# Deze functie neemt als argument een cv2 frame, en minimaal een hue en een delta hue en berekend het massamiddelpunt, en laat eventueel ook de plaatjes zien.
def calculate_cm(frame, hue0, delta_hue, smin=30, smax = 255, vmin = 100, vmax = 255, write_image = False, write_mask = False, write_contour = False, show_image = False, show_mask = False, show_contour = False):

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
        pos=np.array(center)

    if write_image == True:  
        cv2.imwrite('images/image.png',frame)

    contour = frame
    cv2.drawContours(contour, c, -1, (0,255,255), 3)
    cv2.circle(contour, (np.int_(center[0]),np.int_(center[1])), 5, (255, 255, 255), -1)

    if write_mask == True:
        cv2.imwrite('images/mask.png',mask)

    if write_contour == True:  
        cv2.imwrite('images/contour.png',contour)

    if show_image == True:
        cv2.imshow('frame', frame)
        cv2.waitKey(0)

    if show_mask == True:
        cv2.imshow('mask', mask)
        cv2.imwrite('test-mask.png',mask)
        cv2.waitKey(0)

    if show_contour == True:
        cv2.imshow('countour',contour)
        cv2.waitKey(0)

    cv2.destroyAllWindows()
    return(pos)

photo = 'CIMG1549.jpg'
frame0 = cv2.imread(photo)
frame = cv2.resize(frame0, (640, 480))

calculate_cm(frame, 10, 10)
