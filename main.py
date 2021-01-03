import cv2
import numpy as np

class main():
    def __init__(self):
        self.img = cv2.imread('road.png')
        self.gray = cv2.cvtColor(self.img,cv2.COLOR_BGR2GRAY)
        
        #Detect edges
        self.edges = cv2.Canny(self.gray, 150,300) 
            
        #Get Lines
        self.lines = cv2.HoughLinesP(
                    self.edges,
                    rho = 1.0,
                    theta = np.pi/180,
                    threshold = 20,
                    minLineLength = 30,
                    maxLineGap =10)
        
        #Draw Lines
        self.line_img = np.zeros((
            self.img.shape[0],
            self.img.shape[1],
            3),dtype = np.uint8)

        self.line_color = [0,255,0]
        self.line_thickness = 1
        self.dot_color = [0,255,0]
        self.dot_size = 3
    

    def func(self):
        for line in self.lines:
            for x1,y1,x2,y2 in line:
                cv2.line(self.line_img,
                    (x1,y1),
                    (x2,y2),
                    self.line_color,
                    self.line_thickness)

                cv2.circle(self.line_img,
                    (x1,y1),
                    self.dot_size, self.dot_color, -1)

                cv2.circle(self.line_img,
                    (x2,y2),
                    self.dot_size, self.dot_color, -1)

        
        overlay = cv2.addWeighted(self.img,
                0.8, self.line_img, 1.0, 0.0)

            
        cv2.imshow("Overlay", overlay)
        cv2.waitKey()
        cv2.destroyAllWindows()

root = main()
root.func()


