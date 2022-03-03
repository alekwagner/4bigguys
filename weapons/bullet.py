import arcade 
from consts import SPRITE_SCALING_BULLET

class Bullet(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.texture = arcade.load_texture(f"Floor_board_wall - Copy.png")
        self.scale = SPRITE_SCALING_BULLET
     

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

    def kill(self):
        
        self.remove_from_sprite_lists() 