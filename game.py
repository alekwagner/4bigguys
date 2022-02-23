import arcade
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, PLAYER_START_X, PLAYER_START_Y, CHARACTER_SCALING

# The actual game 
class MyGame(arcade.Window):

    def __init__(self): 

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
    
    def on_resize(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        super().on_resize(SCREEN_HEIGHT, SCREEN_WIDTH)

    def setup(self):
        # asign my sprite lists to their arcade lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite("plasma_ammo.png", CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

    def on_draw(self):
        """Render the screen."""
        self.player_list.draw()

    def on_update(self, delta_time):  
        self.player_list.update_animation(delta_time)
    
def main():
    """Main function"""   
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()