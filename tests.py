import unittest

from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            m1.get_cols(),
            num_cols,
        )
        self.assertEqual(
            m1.get_rows(),
            num_rows,
        )

        self.assertEqual(
            m1.get_cells()[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1.get_cells()[num_cols - 1][num_rows - 1].has_bottom_wall, False
        )

    def test_maze_break_enter_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            m1.get_cells()[0][0].has_top_wall,
            False,
        )
        self.assertEqual(
            m1.get_cells()[num_cols - 1][num_rows - 1].has_bottom_wall, False
        )

    def test_maze_reset(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)

        self.assertEqual(
            m1.get_cells()[0][0].visited,
            False,
        )
        self.assertEqual(m1.get_cells()[num_cols - 1][num_rows - 1].visited, False)


if __name__ == "__main__":
    unittest.main()
