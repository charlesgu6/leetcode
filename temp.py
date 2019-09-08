#%%
import os
import cv2

video = 'E:\BaiduYun\Follow_虹桥2#06.avi'
video_name = video.split('\\')[-1].split('.')[0]
video_path = '\\'.join(video.split('\\')[:-1])+'\\'
im_path = video_path + 'res\\'
#%%
cap = cv2.VideoCapture(video)
count = 0
while cap.isOpened():
    count += 1
    ret, frame = cap.read()
    if ret:
        cv2.imwrite(im_path+'{:03d}.jpg'.format(count),frame)
    else:
        break

cap.release()
cv2.destroyAllWindows()

#%%
