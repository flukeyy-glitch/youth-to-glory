all_tiles = {'A': 13, 'B': 3, 'C': 3, 'D': 6, 'E': 18,
             'F': 3, 'G': 4, 'H': 3, 'I': 12, 'J': 2,
             'K': 2, 'L': 5, 'M': 3, 'N': 8, 'O': 11,
             'P': 3, 'Q': 2, 'R': 9, 'S': 6, 'T': 9,
             'U': 6, 'V': 3, 'W': 3, 'X': 2, 'Y': 3,
             'Z': 2}


class Player:
    def __init__(self, name):
        self.name = name
        self.held_tiles = []
        self.placed_tiles = []

    def get_name(self):
        return self.name

    def get_held_tiles(self):
        return self.held_tiles

    def get_num_held_tiles(self):
        return len(self.held_tiles)

    def add_tile(self, tile):
        # To do
        self.held_tiles.append(tile)

    def dump_tile(self, tile):
        # To do
        self.held_titles.remove(tile)


# class Grid:
  #  def __init(self):
