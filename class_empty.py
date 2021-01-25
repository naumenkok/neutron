from class_color import Color


class Empty:
    color = Color.empty

    def variants_of_moving_all(self, board, x, y):
        return []

    def __str__(self):
        return ' +'
