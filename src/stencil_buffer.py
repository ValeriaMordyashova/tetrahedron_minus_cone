import pygame
from OpenGL.GL import *
from drawing import draw_tetrahedron, draw_cone_from_right_face

def stencil_buffer_example():
    """
    Использует буфер трафарета для отрисовки фигуры "тетраэдр минус конус" с помощью библиотеки Pygame и OpenGL.

    Функция создает окно Pygame и инициализирует OpenGL, чтобы использовать буфер трафарета.
    В цикле обработки событий Pygame реализована отрисовка тетраэдра и конуса с использованием буфера трафарета.

    Управление:
    - Стрелка влево: Поворот влево
    - Стрелка вправо: Поворот вправо
    - Стрелка вверх: Поворот вверх
    - Стрелка вниз: Поворот вниз
    - Закрытие окна: Завершение программы
    """
    rotation_speed = 5.0

    # Включить буфер глубины и буфер трафарета, установить операции для буфера трафарета
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_STENCIL_TEST)
    glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)

    # Начальная позиция камеры
    glTranslatef(0.0, 0.0, -5)

    while True:
        # Обработка событий Pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                # Обработка нажатий клавиш для управления вращением
                if event.key == pygame.K_LEFT:
                    glRotatef(rotation_speed, 0, -1, 0)
                elif event.key == pygame.K_RIGHT:
                    glRotatef(-rotation_speed, 0, -1, 0)
                elif event.key == pygame.K_UP:
                    glRotatef(rotation_speed, -1, 0, 0)
                elif event.key == pygame.K_DOWN:
                    glRotatef(-rotation_speed, -1, 0, 0)

        # Очистка буферов и включение буфера трафарета
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT | GL_STENCIL_BUFFER_BIT)
        glEnable(GL_STENCIL_TEST)

        # Первый проход: рисуем тетраэдр в буфер трафарета
        glStencilFunc(GL_ALWAYS, 1, 0xFF)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)

        # Второй проход: рисуем конус в буфер трафарета
        glStencilFunc(GL_ALWAYS, 2, 0xFF)
        glStencilOp(GL_KEEP, GL_KEEP, GL_REPLACE)
        # Нарисовать конус от правой грани тетраэдра
        draw_cone_from_right_face()

        # Третий проход: рисуем только те части тетраэдра, которые не пересекаются с конусом
        glStencilFunc(GL_NOTEQUAL, 1, 0xFF)
        glStencilOp(GL_KEEP, GL_KEEP, GL_KEEP)
        draw_tetrahedron()

        # Обновление экрана
        pygame.display.flip()

        # Задержка для стабилизации кадров
        pygame.time.wait(10)
