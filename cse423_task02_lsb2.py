from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel
   

    glEnd()

def plotpoints2():

  


    # Triangle

    x1, x2, x3,x4 =  -0.2,0,-0.2,0

    y1, y2, y3,y4 =  -0.5, -0.5, -0.8,-0.8  
    

    glColor3f(0.5, 0.5, 0.0)

    glBegin(GL_QUADS)
    glColor3f(1,1,1)
    
    glVertex3f(x1,y1, 0.0)    
    glVertex3f(x3,y3, 0.0)
    glVertex3f(x4,y4, 0.0)  
    glVertex3f(x2,y2, 0.0)
    glEnd()
    glFlush()
def plotpoints1():

  




    x1, x2, x3,x4 = -0.3, 0.1, -0.3,0.1

    y1, y2, y3,y4 = -0.3, -0.3, -0.8,-0.8


    glBegin(GL_QUADS)
    glColor3f(0.5,0.5,0.5)
    
    glVertex3f(x1,y1, 0.0)    
    glVertex3f(x3,y3, 0.0)
    glVertex3f(x4,y4, 0.0)  
    glVertex3f(x2,y2, 0.0)
    glEnd()
    glFlush()


    
    plotpoints2()
def plotpoints():

  


    # Triangle

    x1, x2, x3 = -0.3, 0.1, -0.1

    y1, y2, y3 = -0.3, -0.3, -0.1

    
    glBegin(GL_TRIANGLES)
    glColor3f( 1, 0, 0 )
    glVertex2f( x1,y1)
   
    glVertex2f(x2,y2)
    
    glVertex2f( x3,x3)
    glEnd()

    glFlush()

    plotpoints1()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    # glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glLoadIdentity()
    # iterate()
    # glColor3f(1.0, 1.0, 0.0) #konokichur color set (RGB)
    # #call the draw methods here
    
    plotpoints()   
   
    #glutSwapBuffers()



glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500) #window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Pjnjnjnje") #window name
glutDisplayFunc(showScreen)

glutMainLoop()