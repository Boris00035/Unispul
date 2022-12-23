import cv2
import numpy as np
import matplotlib.pyplot as plt

np.set_printoptions(suppress=True)

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

    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
                        cv2.CHAIN_APPROX_SIMPLE)[-2]

    # Test for presence of contours
    if len(cnts) == 0:
        # If not present (object has left image plane or is otherwise not found),
        # set position to last value
        pos=[[-1,-1]]
    else:
        # Otherwise pick the contour with largest enclosed area and 
        # determine 'center of mass' (CM)
        c = max(cnts, key=cv2.contourArea)
        M = cv2.moments(c)
        if M["m00"] != 0 and M["m00"] != 0:
            center = ((M["m10"] / M["m00"]), M["m01"] / M["m00"])
        else:
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
        cv2.waitKey(0)

    if show_mask == True:
        cv2.imshow('mask', mask)
        cv2.waitKey(0)

    if show_contour == True:
        contour = frame
        cv2.drawContours(contour, c, -1, (0,255,255), 3)
        cv2.circle(contour, (np.int_(center[0]),np.int_(center[1])), 5, (255, 255, 255), -1)
        cv2.imshow('countour',contour)
        cv2.waitKey(0)

    return(pos)

dir = 'footage/'

# Exilim video
video='botsing.mov'

# Define video capture channel
cap=cv2.VideoCapture(dir+video)

# Total number of frames
Nframes = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = 30
# schaal_factor bepaald met fiji
schaal_factor = 47

massa_blauw = 2.4131 * 10**-3
massa_roze = 2.4088 * 10**-3

pos_list_blauw = np.empty((2))
pos_list_roze = np.empty((2))
print(pos_list_blauw)
# Loop through frames
for nframe in np.arange(Nframes):
    print("Frame " + str(nframe))
    # cap.read() reads the next frame (image) of the video 
    found,frame = cap.read()

    # cv2.imshow('frame', frame)
    # cv2.waitKey(4)

    # Wanneer bij nde frame, laat deze zien
    # if nframe == 40:
        # cv2.imshow('frame', frame)
        # cv2.imwrite('images/frame_schaal.png', frame)
        # Laat het plaatje staan totdat een toets wordt ingedrukt.
        # cv2.waitKey(0)
        # cv2.destroyWindow('frame')

    # berekening blauwe balletje
    cm_blauw = calculate_cm(frame, hue0=145, delta_hue=20, smin=110, smax = 150, vmin = 100, vmax = 176)
    interval_blauw = [27, 30]
    if nframe == interval_blauw[0]:
        pos_voor_blauw = cm_blauw

    if nframe == interval_blauw[1]:
        pos_diff_blauw = abs(cm_blauw - pos_voor_blauw)
        snelheid_px_per_frame_blauw = pos_diff_blauw / abs(interval_blauw[0] - interval_blauw[1])
        snelheid_cm_per_sec_blauw = snelheid_px_per_frame_blauw * fps/schaal_factor
        print(snelheid_cm_per_sec_blauw[0] * massa_blauw)

    pos_list_blauw = np.vstack( [pos_list_blauw, cm_blauw] )

    # berekening roze balletje
    cm_roze = calculate_cm(frame, hue0=230, delta_hue=10, smin=110, smax = 150, vmin = 200, vmax = 250)
    interval_roze = [30, 33]
    if nframe == interval_roze[0]:
        pos_voor_roze = cm_roze

    if nframe == interval_roze[1]:
        pos_diff_roze = abs(cm_roze - pos_voor_roze)
        snelheid_px_per_frame_roze = pos_diff_roze / abs(interval_roze[0] - interval_roze[1])
        snelheid_cm_per_sec_roze = snelheid_px_per_frame_roze * fps/schaal_factor
        print(snelheid_cm_per_sec_roze[0] * massa_roze )

    pos_list_roze = np.vstack( [pos_list_roze, cm_roze] )



# print(pos_list)

# fig = plt.figure()
# ax = plt.axes(projection='3d')
# ax.set_xlabel('t (s)')
# ax.set_ylabel('x (px)')
# ax.set_zlabel('y (px)')

# ax.set_ylim3d(100, 400)
# ax.set_zlim3d(205, 215)

t = np.linspace(0,43,num = Nframes + 1)

# ax.scatter(t, np.transpose(pos_list_blauw)[0], np.transpose(pos_list_blauw)[1], s=2 )
# ax.scatter(t, np.transpose(pos_list_roze)[0], np.transpose(pos_list_roze)[1], s=2 )
# ax.scatter(t, np.transpose(pos_list)[0], 0, s=2 )
# ax.scatter(t, 0, np.transpose(pos_list)[1], s=2 )
# plt.show()

fig, ax = plt.subplots(2, sharex=True)

ax[0].plot(t, np.transpose(pos_list_roze)[0] / schaal_factor)
ax[0].set_ylim([800 / schaal_factor, 1800 / schaal_factor])
ax[0].set_ylabel('x (cm)')
ax[0].set_title('Plot roze balletje')

ax[1].plot(t, np.transpose(pos_list_blauw)[0] / schaal_factor)  
ax[1].set_ylim([300 / schaal_factor, 1000 / schaal_factor])
ax[1].set_ylabel('x (cm)')
ax[1].set_xlabel('t (s)')
ax[1].set_title('Plot blauwe balletje')

fig.savefig('images/2x2d_plot.png', bbox_inches='tight', dpi=200)

plt.show()