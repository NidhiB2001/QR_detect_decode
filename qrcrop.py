# import copy
# import cv2
# import numpy as np

# cap = cv2.VideoCapture(0)
# width = 640
# height = 480
# cap.set(cv2.CAP_PROP_FRAME_WIDTH,width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT,height)

# skip_pts = 1
# fixed_width = int(width*0.73)
# fixed_height = int(height*0.625)
# coordinate = [[fixed_width, fixed_height],[fixed_width, 0],[] , [0, fixed_height],[0, 0]]
# finish = False
# while(cap.isOpened()):
#     # get a frame
#     ret, frame = cap.read()
#     # create the rectangle ROI
#     frame_copy = copy.deepcopy(frame)
#     start_point = (int(width*0.156), int(height*0.209))
#     cv2.rectangle(frame_copy, start_point, (start_point[0]+fixed_width, start_point[1]+fixed_height), (0, 255, 155), 5)
#     roi = frame[start_point[1]:start_point[1]+fixed_height,start_point[0]:start_point[0]+fixed_width,:]
#     ms = cv2.pyrMeanShiftFiltering(roi, 8, 20)
#     canny = cv2.Canny(ms,100,180)
#     # the point follow the Counter clockwise
#     cnts, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#     cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:1]
#     for j in range(len(cnts)):
#         c = cnts[j]
#         # approximate the contour
#         peri = cv2.arcLength(c, True)
#         approx = cv2.approxPolyDP(c, 0.01*peri, True)

#         # if our approximated contour has four points, then
#         # we can assume that we have found our screen
#         # we assert the available area ratio bigger than 0.5
#         if len(approx) == 4 and cv2.contourArea(approx.squeeze(1)) / (fixed_height*fixed_height) >= 0.5:
#             compute_direction = [0,0,0,0]
#             for i in range(4):
#                 delta = approx[(i+1)%4,0,:]-approx[i,0,:]
#                 delta_argmax = int(abs(delta[1]) > abs(delta[0]))
#                 # compute the line direction
#                 compute_direction[i] = ((delta_argmax+1)*(1 if delta[delta_argmax]>-delta[delta_argmax] else -1)+2)
#             pts1 = approx.astype(np.float32)
#             # compute the target warp coordinate
#             pts2 = np.array([coordinate[x] for x in compute_direction],dtype=np.float32)
#             M = cv2.getPerspectiveTransform(pts1, pts2)
#             warp = cv2.warpPerspective(roi, M, (fixed_width, fixed_height))
#             cv2.imshow("warp", warp)
#             # finish = True

#     cv2.imshow("capture", frame_copy)
#     cv2.imshow("roi",roi)
#     cv2.imshow("meanShift",ms)
#     cv2.imshow("canny",canny)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
#     if finish:
#         break

# cap.release()
# cv2.destroyAllWindows()
