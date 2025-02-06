import random
import time
from typing import List

from cell import Cell
from point import Point
from window import Window


class Maze:
    """
    Maze
    """

    def __init__(
        self,
        x1: int,
        y1: int,
        num_rows: int,
        num_cols: int,
        cell_size_x: int,
        cell_size_y: int,
        win: Window | None = None,
        seed: int | None = None,
    ):
        if seed is not None:
            random.seed(seed)

        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self._win = win
        self._cells: List[List[Cell]] = []
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            cols: List[Cell] = []
            self._cells.append(cols)
            for j in range(self.num_rows):
                point1 = Point(
                    self.x1 + (self.cell_size_x * i), self.y1 + (self.cell_size_y * j)
                )
                point2 = Point(
                    self.x1 + (self.cell_size_x * i) + self.cell_size_x,
                    self.y1 + (self.cell_size_y * j) + self.cell_size_y,
                )
                cell = Cell(point1, point2, window=self._win)
                cols.append(cell)
                self._draw_cells(i, j)

    def get_cols(self):
        """
        Return Number of Cols
        """
        return len(self._cells)

    def get_rows(self):
        """
        Return Number of Rows
        """
        return len(self._cells[0])

    def get_cells(self):
        """
        Return Number of Cols
        """
        return self._cells

    def _draw_cells(self, i, j):
        cell = self._cells[i][j]
        cell.draw()

        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.02)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        curr_cell = self._cells[i][j]
        while True:
            possible_dirs = []
            directions = []
            if i > 0 and not self._cells[i - 1][j].visited:
                possible_dirs.append((i - 1, j))
                directions.append("left")

            if j > 0 and not self._cells[i][j - 1].visited:
                possible_dirs.append((i, j - 1))
                directions.append("up")

            if i < len(self._cells) - 1 and not self._cells[i + 1][j].visited:
                possible_dirs.append((i + 1, j))
                directions.append("right")

            if j < len(self._cells[i]) - 1 and not self._cells[i][j + 1].visited:
                possible_dirs.append((i, j + 1))
                directions.append("down")

            if len(possible_dirs) == 0:
                self._draw_cells(i, j)
                return

            random_dir = random.randint(0, len(possible_dirs) - 1)
            match (directions[random_dir]):
                case "left":
                    self._cells[i][j].has_left_wall = False
                    self._cells[i - 1][j].has_right_wall = False
                case "up":
                    self._cells[i][j - 1].has_bottom_wall = False
                    self._cells[i][j].has_top_wall = False
                case "right":
                    self._cells[i + 1][j].has_left_wall = False
                    self._cells[i][j].has_right_wall = False
                case "down":
                    self._cells[i][j + 1].has_top_wall = False
                    self._cells[i][j].has_bottom_wall = False
            self._break_walls_r(*possible_dirs[random_dir])

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cells(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cells(self.num_cols - 1, self.num_rows - 1)

    def _reset_visited(self):
        for col in self._cells:
            for row in col:
                row.visited = False

    def solve(self):
        """
        Solve The Maze
        """
        self.solver_r(0, 0)

    def solver_r(self, i, j):
        """
        Helper Recursive Solver
        """
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self.num_cols - 1][self.num_rows - 1]:
            return True
        if (
            i > 0
            and not self._cells[i - 1][j].visited
            and not self._cells[i - 1][j].has_right_wall
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            val = self.solver_r(i - 1, j)
            if val:
                return True
            self._cells[i][j].draw_move(self._cells[i - 1][j], True)
        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j - 1].has_bottom_wall
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            val = self.solver_r(i, j - 1)
            if val:
                return True
            self._cells[i][j].draw_move(self._cells[i][j - 1], True)

        if (
            i < len(self._cells) - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i + 1][j].has_left_wall
            and not self._cells[i][j].has_right_wall
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            val = self.solver_r(i + 1, j)
            if val:
                return True
            self._cells[i][j].draw_move(self._cells[i + 1][j], True)

        if (
            j < len(self._cells[i]) - 1
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j + 1].has_top_wall
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            val = self.solver_r(i, j + 1)
            if val:
                return True
            self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False
