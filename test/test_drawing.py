import unittest

import pygame
from OpenGL.GL import glGetDoublev
from OpenGL.raw.GL.VERSION.GL_1_0 import GL_PROJECTION_MATRIX
from OpenGL.raw.GLU import gluPerspective
from pygame.locals import *
from scr.pygame_window import create_pygame_window

# Замените your_module_name на имя вашего модуля, где содержится функция create_pygame_window

def test_create_pygame_window():
    # Инициализация Pygame-окна
    create_pygame_window()

    # Получение текущего окна Pygame
    window = pygame.display.get_surface()

    # Проверка, что окно было создано
    assert window is not None

    # Получение текущей проекции
    projection = glGetDoublev(GL_PROJECTION_MATRIX)

    # Проверка, что проекция соответствует установленным параметрам
    assert projection == unittest.approx([
        [1.8106601717798214, 0.0, 0.0, 0.0],
        [0.0, 2.414213562373095, 0.0, 0.0],
        [0.0, 0.0, -1.0202020202020203, -1.0],
        [0.0, 0.0, -0.20202020202020202, 0.0]
    ])

    # Проверка, что параметры окна установлены правильно
    assert window.get_size() == (800, 600)
    assert window.get_flags() & DOUBLEBUF == DOUBLEBUF
    assert window.get_flags() & OPENGL == OPENGL
