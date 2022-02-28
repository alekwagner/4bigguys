import arcade
import os
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, PLAYER_START_X, PLAYER_START_Y, CHARACTER_SCALING, PLAYER_MOVEMENT_SPEED

# The actual game 
class MyGame(arcade.Window):

    def __init__(self): 

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the path to start with this program
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)
    
    # def on_resize(self, SCREEN_WIDTH, SCREEN_HEIGHT):
    #     super().on_resize(SCREEN_HEIGHT, SCREEN_WIDTH)

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

        self.clear()


    def process_keychange(self):
       
        # Process up/down
        if self.up_pressed and not self.down_pressed:
                self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED        
        elif self.down_pressed and not self.up_pressed:
                self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_y = 0

        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        # if key == arcade.key.L:
        #     self.setup(self.level)

        if self.draw_info:
            self.draw_info = False

        self.process_keychange()

    def on_key_release(self, key, modifiers):
        #Called when the user releases a key. 

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()     

    def on_update(self, delta_time):  
        self.player_list.update_animation(delta_time)
    
def main():
    """Main function"""   
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()