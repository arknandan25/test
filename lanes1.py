import cv2
import numpy as np
#loading and viewing images 
img=cv2.imread('/home/ark/Documents/Project-1/opencv/test.jpg',1)
lanes=np.copy(img)
grey=cv2.cvtColor(lanes,cv2.COLOR_RGB2GRAY)
blur=cv2.GaussianBlur(grey,(5,5),0)#to reduce noise and smoothen image
cv2.imshow('result',blur)
<<<<<<< HEAD
cv2.waitKey(34000)
cv2.destroyAllWindows()
#----Gray scale -edge detection-----
#0(lowest intensity completely black) to 255(highest intensity completely white)
#values of pixe
=======
cv2.waitKey(65000)
cv2.destroyAllWindows()
#----Gray scale -edge detection-----
#0(lowest intensity completely black) to 255(highest intensity completely white)
#v
>>>>>>> 79e9e498a8dedd971a695a1d6533eedc72edcc5e
