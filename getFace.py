from SimpleCV import Camera, Display, VideoStream, VirtualCamera, Color
from time import sleep
import numpy

cam = Camera(prop_set={'width':320, 'height':240})
dis = Display(resolution=(320,240))
lastCoordinates = (0,0)
vidStream = VideoStream("test.mov", 25, True)

while not dis.isDone():
    frame = cam.getImage()
    faces = frame.findHaarFeatures('face')
    if faces:
        for face in faces:
            # Checks to see if the (x,y) is greater than or less than the last (x,y). Then we have motion.
            if face.coordinates()[0] > lastCoordinates[0]+3 or face.coordinates()[1] > lastCoordinates[1]+3 or face.coordinates()[0] < lastCoordinates[0]-3 or face.coordinates()[1] < lastCoordinates[1]-3:
                lastCoordinates = face.coordinates()
                face.draw()
                frame.save(vidStream)
    # Show the image
    frame.show()
    # My attempt to get around 30 frames per second.. though I haven't checked this.
    sleep(1./30.)

if dis.IsDone():
    cam.close()
    dis.close()