# import Tkinter as tk
import tkinter  as tk
import cv2
from PIL import Image, ImageTk

# root = tk.Tk()
# root.bind('<Escape>', lambda e: root.quit())
# width, height = 800, 600
# cap = cv2.VideoCapture(0)
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)

class  VideoCapture(tk.Label):
    def __init__(self,parent=None):
        super(VideoCapture, self).__init__(parent)

        # self.configure(foreground="red")
        self.configure(bg="light blue")

    def capture_init( self ):
        # self.width = 200
        self.width = self.winfo_width()
        # self.height = self.width
        self.height = int(self.width * 0.8)
        rtsp="rtsp://184.72.239.149/vod/mp4://BigBuckBunny_175k.mov"
        #rtsp='rtsp://root:password@192.168.1.90/axis-media/media.amp'
        # self.cap = cv2.VideoCapture(0)
        self.cap = cv2.VideoCapture(rtsp)
        # self.winfo_height()
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        # self.pack()

    def show_frame(self):

        status, frame = self.cap.read()
        if not status:
            print("cap read error !!")
            return
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)

        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.imgtk = imgtk
        self.configure(image=imgtk)
        self.after(10, self.show_frame)
        del imgtk
        del img
        del cv2image


if __name__ == "__main__":
    print("test log")
    root = tk.Tk()
    root.bind('<Escape>', lambda e: root.quit())
    root.wm_minsize(400,300)
    root.wm_maxsize(400,300)
    video_capture = VideoCapture(root)
    video_capture.place(x=0  ,y=0 ,w=400,h=300,anchor='nw')
    video_capture.capture_init()
    # video_capture.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 400)
    # video_capture.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
    # video_capture.configure(foreground="red")

    # video_capture.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
    # video_capture.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
    video_capture.show_frame()
    root.mainloop()
