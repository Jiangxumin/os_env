import cv2 as cv 

def video_demo(): 
#0是代表摄像头编号，只有一个的话默认为0 
    capture=cv.VideoCapture("rtsp://184.72.239.149/vod/mp4://BigBuckBunny_175k.mov")
    # capture=cv.VideoCapture('rtsp://root:password@192.168.1.90/axis-media/media.amp')
    #capture=cv.VideoCapture(0)
    while(True):
        ref,frame=capture.read()
        cv.imshow("1",frame)
        #等待30ms显示图像，若过程中按“Esc”退出 
        c= cv.waitKey(30) & 0xff 
        if c=='q': 
            capture.release() 
            break 

video_demo() 
cv.destroyAllWindows()

