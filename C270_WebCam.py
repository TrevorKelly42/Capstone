import cv2
import time

class CameraInst():
        # Constructor...
        def __init__(self):
                fps        = 20                 # Frames per second...
                resolution = (320, 240)          # Frame size/resolution...
                w = 320
                h = 240

                self.cap = cv2.VideoCapture(0)  # Capture Video...
                print("Camera warming up ...")
                time.sleep(1)

                # Define the codec and create VideoWriter object
                fourcc = cv2.VideoWriter_fourcc(*"H264")     # You also can use (*'XVID')
                self.out = cv2.VideoWriter('output.avi',fourcc, fps, (w, h))

        def captureVideo(self):
                # Capture
                self.ret, self.frame = self.cap.read()
                print(self.ret)
                # Image manipulations come here...
                self.gray = cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
                cv2.imshow('frame',self.gray)

        def saveVideo(self):
                # Write the frame
                self.out.write(self.frame)

        def __del__(self):
                self.cap.release()
                cv2.destroyAllWindows()
                print("Camera disabled and all output windows closed...")

def main():
        cam1 = CameraInst()

        while(True):
                # Display the resulting frames...
                cam1.captureVideo()    # Live stream of video on screen...
                cam1.saveVideo()       # Save video to file 'output.avi'...
                if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

        cleanUp()

if __name__=="__main__":
        main()