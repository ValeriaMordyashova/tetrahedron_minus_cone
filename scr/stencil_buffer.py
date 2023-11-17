import pygame
from OpenGL.GL import *
from drawing import draw_cone, draw_tetrahedron, draw_cone_from_right_face

def stencil_buffer_example():
    """
    Использует буфер трафарета для отрисовки фигуры "тетраэдр минус конус" с помощью библиотеки Pygame и OpenGL.
    """
    rotation_speed = 5.0
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_STENCIL_TEST)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)

    glTranslatef(0.0, 0.0, -5)

    while True:
        glEnable(GL_STENCIL_TEST)  # Включить буфер трафарета

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glRotatef(rotation_speed, 0, -1, 0)
                elif event.key == pygame.K_RIGHT:
                    glRotatef(-rotation_speed, 0, -1, 0)
                elif event.key == pygame.K_UP:
                    glRotatef(rotation_speed, -1, 0, 0)
                elif event.key == pygame.K_DOWN:
                    glRotatef(-rotation_speed, -1, 0, 0)


        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)

        # Первый проход: рисуем тетраэдр в буфер трафарета
        glStencilFunc(GL_ALWAYS, 1, 0)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        draw_tetrahedron()

        # Второй проход: рисуем конус в буфер трафарета
        glStencilFunc(GL_ALWAYS, 2, 0)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        # Нарисовать конус от правой грани тетраэдра
        draw_cone_from_right_face()

        # Третий проход: рисуем только те части тетраэдра, которые не пересекаются с конусом
        glStencilFunc(GL_EQUAL, 1, 255)
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        draw_tetrahedron()

        pygame.display.flip()
        pygame.time.wait(10)
