from maze import Maze
from window import Window


def main():
    """
    Main Method
    """
    win = Window(800, 600)
    maze = Maze(100, 100, 8, 8, 50, 50, win)
    maze.solve()

    # point1 = Point(50, 50)
    # point2 = Point(100, 100)
    # c1 = Cell(point1, point2, win)
    # c1.has_right_wall = False
    # c1.draw()
    #
    # point1 = Point(100, 50)
    # point2 = Point(150, 100)
    # c2 = Cell(point1, point2, win)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw()
    #
    # c1.draw_move(c2)
    #
    # point1 = Point(100, 100)
    # point2 = Point(150, 150)
    # c3 = Cell(point1, point2, win)
    # c3.has_top_wall = False
    # c3.has_right_wall = False
    # c3.draw()
    #
    # c2.draw_move(c3)
    #
    # point1 = Point(150, 100)
    # point2 = Point(200, 150)
    # c4 = Cell(point1, point2, win)
    # c4.has_left_wall = False
    # c4.draw()
    #
    # c3.draw_move(c4, undo=True)
    #
    win.wait_for_close()


if __name__ == "__main__":
    main()
