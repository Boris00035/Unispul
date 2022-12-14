import cv2
import numpy as np

photo = 'CIMG1549.jpg'
frame0 = cv2.imread(photo)
frame = cv2.resize(frame0, (640, 480))

cv2.imshow('fig1', frame)
cv2.waitKey(0)
cv2.imwrite('test2.png', frame)

frame_hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

hue0 = 10
delta_hue = 10
# Scaling factor because Hue in Python scales from 0 to 179 (0 to 255 in ImageJ)
hue_fac = 180/255 
# Lower and upper limits for H, S and V in the mask
hmin = hue_fac*(hue0-delta_hue)
hmax = hue_fac*(hue0+delta_hue)
smin = 30
smax = 255
vmin = 100
vmax = 255
lower = np.array([np.maximum(0,hmin),smin,vmin])
upper = np.array([np.minimum(180,hmax),smax,vmax])
# Mask for the frame, and the original frame removing 'non-object'
# Note that Hue can also 'loop around zero'
if hmin<0:
    mask=cv2.inRange(frame_hsv,lower,upper)+\
    cv2.inRange(frame_hsv,np.array([np.mod(hmin,180.),smin,vmin]),\
                np.array([180.,smax,vmax]))
elif hmax>180:
    mask=cv2.inRange(frame_hsv,lower,upper)+\
    cv2.inRange(frame_hsv,np.array([0.,smin,vmin]),\
                np.array([np.mod(hmax,180.),smax,vmax]))
else:
    mask=cv2.inRange(frame_hsv,lower,upper)
res=cv2.bitwise_and(frame,frame,mask=mask)
# Plot of masked object
cv2.imshow('mask', mask)
cv2.imwrite('test-mask.png',mask)
cv2.waitKey(0)
# cv2.destroyWindow('mask')
# Plot of masked object in original color
cv2.imshow('res',res)
cv2.waitKey(0)
# cv2.destroyWindow('res')

# NOTE: this segment of code is not self-contained, 
# but must be incorporated in own code before compilation

# Find all contours present in the mask
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[-2]
# Test for presence of contours
if len(cnts)==0:
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
    
# Diagnostics: draw contour (yellow) and CM (white) of object
frame2 = frame
cv2.drawContours(frame2, c, -1, (0,255,255), 3)
cv2.circle(frame2, (np.int_(center[0]),np.int_(center[1])), 5, (255, 255, 255), -1)
cv2.imshow('fig2',frame2)

print(pos)

cv2.imwrite('test3.png', frame)
cv2.waitKey(0)

