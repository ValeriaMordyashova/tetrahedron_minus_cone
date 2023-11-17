from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.raw.GLUT import glutSolidCone


def draw_cone_from_right_face():
    glPushMatrix()

    # Переместить вправо и повернуть так, чтобы правая грань тетраэдра была направлена вдоль оси Z
    glTranslatef(1.0, -1.0, 0.0)
    glRotatef(-90, 1, 1, 0)

    # Нарисовать конус
    draw_cone(0.65, 3)

    # Нарисовать закрашенную окружность
    glColor3f(0.0, 0.0, 0.0)
    gluDisk(gluNewQuadric(), 0, 0.65, 100, 1)

    glPopMatrix()
def draw_cone(radius, height):
    """
    Рисует конус с заданным радиусом и высотой в трехмерном пространстве.

    Ключевые аргументы:
    radius (float): Радиус основания конуса.
    height (float): Высота конуса.

    Описание:
    Функция использует библиотеку OpenGL для отрисовки конуса с заданным радиусом и высотой.
    """
    slices = 100
    stacks = 100
    glColor3f(0.0, 0.0, 0.0)
    gluCylinder(gluNewQuadric(), radius, 0, height, slices, stacks)

def draw_tetrahedron():
    """
          Рисует тетраэдр в трехмерном пространстве.

          Описание: Функция draw_tetrahedron использует библиотеку OpenGL для рисования тетраэдра в трехмерном пространстве.
          Внутри функции используется блок glBegin(GL_TRIANGLES), который указывает на начало рисования треугольников.
          Затем устанавливается цвет для тетраэдра с помощью функции glColor3f, и рисуются вершины тетраэдра с помощью функции
          glVertex3f. После рисования всех вершин тетраэдра, рисование завершается с помощью функции glEnd().
    """
    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.75, 0.8)
    glVertex3f(0.0, 1.5, 0.0)
    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)

    glVertex3f(0.0, 1.5, 0.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glVertex3f(0.0, 1.5, 0.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)

    glVertex3f(0.0, 1.5, 0.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, 1.0)

    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)

    glVertex3f(-1.0, -1.0, 1.0)
    glVertex3f(1.0, -1.0, -1.0)
    glVertex3f(-1.0, -1.0, -1.0)
    glEnd()

