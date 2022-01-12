import cv2

def snapshot():
    VideoCaptureObject=cv2.VideoCapture(0)
    result=True
    
    while result:
        ret, frame=VideoCaptureObject.read()
        cv2.imwrite("Snapshot.png",frame)
        result=False
        
    VideoCaptureObject.release()
    cv2.destroyAllWindows()
    
snapshot()
    