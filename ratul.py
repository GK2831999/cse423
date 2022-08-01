from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def midPoint(X1,Y1,X2,Y2):
    position= []
    # calculate dx &amp; dy
    dx = X2 - X1
    dy = Y2 - Y1

    d = dy - (dx/2)
    x = X1
    y = Y1
    position.append([x, y])
    if dx>0:

        while (x < X2):
            x= x+1

            if(d< 0):
                d = d + dy

            else:
                d = d + (dy - dx)

                y= y+1

            position.append([x, y])

    elif (dx<0):
        while (X2 < x):
            x= x-1
            if (d <0):
                d = d - dy
            else:
                d = d - (dy - dx)
                y = y-1
            position.append([x, y])

    else:
        while (y>Y2):
            y = y-1
            position.append([x, y])

    return position

def draw_points(x, y):
    glPointSize(5) #pixel size. by default 1 thake
    glBegin(GL_POINTS)
    glVertex2f(x,y) #jekhane show korbe pixel

    glEnd()

def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    arr = [150, 300,200,  120,150, 200,200,  120,150, 300, 150, 200,200, 300, 200, 200,240, 300, 300, 300,300, 300, 300, 250,300, 250, 240, 250,240, 250, 240, 200,240, 200, 300, 200]
    position =[]
    i = 0
    while i<len(arr):
        print(arr[i])
        position+=midPoint(arr[i], arr[i+1], arr[i+2],arr[i+3])
        i+=4
    # position=position +midPoint(150, 300,200,  120)
    # position=position +midPoint(150, 200,200,  120)
    # position=position + midPoint(150, 300, 150, 200)
    # position=position + midPoint(200, 300, 200, 200)
    # position=position + midPoint(240, 300, 300, 300)
    # position=position + midPoint(300, 300, 300, 250)
    # position=position + midPoint(300, 250, 240, 250)
    # position=position +midPoint(240, 250, 240, 200)
    # position=position +midPoint(240, 200, 300, 200)
    print(position)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)

    for i in range(len(position)):
        t= position[i][0]
        r=position[i][1]
        draw_points(t,r)
    glutSwapBuffers()

if __name__=='__main__':

    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(500, 500) #window size
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow(b"quot;OpenGL Coding Practice&quot") #window name
    glutDisplayFunc(showScreen)

    glutMainLoop()