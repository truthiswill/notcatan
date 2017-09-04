"""
This class is an amalgamation of tiles, edges and vertices to represent the board. Don't ask how it works, 
no one knows.
"""

# local imports
from Implementation import Tile
from Implementation import Edge
from Implementation import Vertex


class Board:

    def __init__(self):
        self.tile_array = [
            [Tile.Tile() for _ in range(3)],
            [Tile.Tile() for _ in range(4)],
            [Tile.Tile() for _ in range(5)],
            [Tile.Tile() for _ in range(4)],
            [Tile.Tile() for _ in range(3)],
        ]

        self.connect_tiles()
        self.add_edges_and_vertices()

    def connect_tiles(self):
        for i, row in self.tile_array:
            for j, tile in row:
                if i <= 1:
                    # check if vaild coordinate
                    if self.is_valid_coordinate(i, j+1):
                        # connect tile to neighbor at 90degrees and connect neighbor back
                        tile.t2 = self.tile_array[i][j+1]
                        self.tile_array[i][j+1].t5 = tile
                    # connect tile to neigher at 150degree and connect neighbor back
                    tile.t3 = self.tile_array[i+1][j+1]
                    self.tile_array[i+1][j+1].t6 = tile
                    # connect tile to neighbor at 210degree and connect neighbor back
                    tile.t4 = self.tile_array[i+1][j]
                    self.tile_array[i+1][j].t1 = tile
                if i == 2:
                    # check if valid coordinate
                    if self.is_valid_coordinate(i, j+1):
                        # connect tile at 90degree and connect neighbor back
                        tile.t2 = self.tile_array[i][j+1]
                        self.tile_array[i][j+1].t5 = tile
                if i > 2:
                    # connect neighbor at -30degrees and connect neighbor back
                    tile.t6 = self.tile_array[i-1][j]
                    self.tile_array[i-1][j].t3 = tile
                    # connect neighbor at 30degrees and connect neighbor back
                    tile.t1 = self.tile_array[i-1][j+1]
                    self.tile_array[i-1][j+1].t4 = tile
                    # check if valid coordinate
                    if self.is_valid_coordinate(i, j+1):
                        # connect neighbor at 90 degrees and connect neighbor back
                        tile.t2 = self.tile_array[i][j+1]
                        self.tile_array[i][j+1].t5 = tile

    def add_edges_and_vertices(self):
        for row in self.tile_array:
            for tile in row:
                for index, edge in tile.edge_arr:
                    # initialize edge and vertex attached to current tile
                    edge = Edge.Edge()
                    new_vertex = tile.vertex_arr[index % 6] = Vertex.Vertex()
                    # attach tile to vertex
                    new_vertex.t1 = tile
                    if tile.tile_arr[index] is not None:
                        # for one neighbor (border tiles) attach vertex to neighbor and vice versa
                        tile.tile_arr[index].vertex_arr[(index + 3) % 6] = new_vertex
                        new_vertex.t2 = tile.tile_arr[index]
                        # attach edge to adjacent tile
                        tile.tile_arr[index].edge_arr[(index + 3) % 6] = edge
                        if tile.tile_arr[index-1] is not None:
                            # for two neighbors (center tiles) do the same again for vertices
                            tile.tile_arr[index-1].vertex_arr[(index + 2) % 6] = new_vertex
                            new_vertex.t3 = tile.tile_arr[index-1]

    def is_valid_coordinate(self, x, y):
        try:
            self.tile_array[x][y]
            return True
        except IndexError:
            return False
