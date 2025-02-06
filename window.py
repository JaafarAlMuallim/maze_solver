from tkinter import BOTH, Canvas, Tk

from line import Line


class Window:
    """
    Window Class
    """

    def __init__(self, width, height):
        self._root = Tk()
        self._root.title("Maze Solver")
        self._root.protocol("WM_DELETE_WINDOW", self.close)

        self.canvas = Canvas(width=width, height=height)
        self.canvas.pack()
        self.running = False
        self.widht = width
        self.height = height

    def redraw(self):
        """
        Redraw and render
        """
        self._root.update_idletasks()
        self._root.update()

    def wait_for_close(self):
        """
        Running as long as the window is not closed
        """
        self.running = True
        while self.running:
            self.redraw()

    def draw_line(self, line: Line, fill: str):
        """
        Draw Line
        """
        line.draw(self.canvas, fill)

    def close(self):
        """
        Stop the program on window close
        """
        self.running = False
