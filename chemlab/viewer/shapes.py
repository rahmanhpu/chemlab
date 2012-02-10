"""Shapes to use in opengl renderers.

"""
from pyglet.gl import *
import numpy as np
from numpy.linalg import norm

def sphere(position, radius, color="gray"):
    x,y,z = position
    
    glPushMatrix()
    glTranslatef(x, y, z)
    
    sph = gluNewQuadric()
    gluSphere(sph, 0.3, 20, 20)

    glPopMatrix()


def cylinder(start, end, radius, color="gray"):
    axis_start = np.array([0,0,1])
    axis_end = end-start
    angle =np.degrees(np.arccos(np.dot(axis_end, axis_start)/
                                (norm(axis_end)*norm(axis_start))))

    glPushMatrix()
    axis_rot = np.cross(axis_start, axis_end)
    
    cyl = gluNewQuadric()
    
    glTranslatef(*start)
    glRotatef(angle, *axis_rot)
    gluCylinder(cyl, radius, radius, norm(axis_end), 10, 10)
    
    glPopMatrix()

def _color(r,g,b):
    glMaterialfv(GL_FRONT, GL_AMBIENT,
                 GLfloat_4(r, g, b, 1.0))
    glMaterialfv(GL_FRONT, GL_DIFFUSE,
                 GLfloat_4(r, g, b, 1.0))