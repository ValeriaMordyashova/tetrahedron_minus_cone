from stencil_buffer import stencil_buffer_example
from pygame_window import create_pygame_window

"""
    Описание:
         Этот модуль содержит главный код, который объединяет функциональности из разных 
         модулей для создания приложения с графическим интерфейсом.
         Этот модуль вызывает две функции:
        - create_pygame_window(): Инициализирует окно Pygame для отображения графики.
        - stencil_buffer_example(): Отображает фигуру "тетраэдр минус конус".
        После выполнения этих функций, окно Pygame будет отображать результат работы отрисовки полученной фигуры.  

"""

create_pygame_window()
stencil_buffer_example()
