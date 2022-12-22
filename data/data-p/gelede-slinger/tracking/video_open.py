import cv2
import numpy as np
import matplotlib.pyplot as plt

def calculate_cm(frame, hue0, delta_hue, smin, smax, vmin, vmax, write_image = False, write_mask = False, write_contour = False, show_image = False, show_mask = False, show_contour = False):

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
        # set position to last value
        pos=[pos_list[len(pos_list) - 1]]
    else:
        # Otherwise pick the contour with largest enclosed area and 
        # determine 'center of mass' (CM)
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        try:
            center = ((M["m10"] / M["m00"]), M["m01"] / M["m00"])
        except:
            center = (1,1)
        pos=np.array(center)

    if write_image == True:  
        cv2.imwrite('images/image.png',frame)

    if write_mask == True:
        cv2.imwrite('images/mask.png',mask)

    if write_contour == True:  
        contour = frame
        cv2.drawContours(contour, c, -1, (0,255,255), 3)
        cv2.circle(contour, (np.int_(center[0]),np.int_(center[1])), 5, (255, 255, 255), -1)
        cv2.imwrite('images/contour.png',contour)

    if show_image == True:
        cv2.imshow('frame', frame)
        cv2.waitKey(1)

    if show_mask == True:
        cv2.imshow('mask', mask)
        cv2.waitKey(1)

    if show_contour == True:
        contour = frame
        cv2.drawContours(contour, c, -1, (0,255,255), 3)
        cv2.circle(contour, (np.int_(center[0]),np.int_(center[1])), 5, (255, 255, 255), -1)
        cv2.imshow('countour',contour)
        cv2.waitKey(1)

    return(pos)

dir = 'footage/'

# Exilim video
video='slinger.mov'

# Define video capture channel
cap=cv2.VideoCapture(dir+video)

# Total number of frames
Nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Loop through frames

pos_list = np.empty((2))
for nframe in np.arange(Nframes):
    print("Frame " + str(nframe))
    # cap.read() reads the next frame (image) of the video 
    found,frame = cap.read()

    # cv2.imshow('frame', frame)
    # cv2.waitKey(4)

    # Wanneer bij nde frame, laat deze zien
    # if nframe == 0:
    #     cv2.imshow('frame', frame)
    #     cv2.imwrite('images/frame.png', frame)
    #     # Laat het plaatje staan totdat een toets wordt ingedrukt.
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    pos_list = np.vstack( [pos_list, calculate_cm(frame, hue0=70, delta_hue=15, smin=50, smax = 100, vmin = 150, vmax = 230,)] )


# print(pos_list)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.set_xlabel('t')
ax.set_ylabel('x')
ax.set_zlabel('y')

ax.set_ylim3d(100, 400)
ax.set_zlim3d(180, 230)

t = np.linspace(0,43,num=1301)

ax.scatter(t, np.transpose(pos_list)[0], np.transpose(pos_list)[1], s=2 )
plt.show()

fig, ax = plt.subplots(2)

ax[0].plot(t, np.transpose(pos_list)[0])
ax[1].plot(t, np.transpose(pos_list)[1]) 


plt.show()