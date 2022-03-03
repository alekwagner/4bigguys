import string
import arcade
import os
import math
from consts import SCREEN_HEIGHT, SCREEN_WIDTH, SCREEN_TITLE, PLAYER_START_X, PLAYER_START_Y, CHARACTER_SCALING, PLAYER_MOVEMENT_SPEED

# The actual game 
class MyGame(arcade.Window):

    def __init__(self): 

        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        # Set the path to start with this program
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

        # our player
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None

        # varrable to hold the info on which keys are pressed
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False
    
    # def on_resize(self, SCREEN_WIDTH, SCREEN_HEIGHT):
    #     super().on_resize(SCREEN_HEIGHT, SCREEN_WIDTH)

    def setup(self):

        # Setup the Camera
        self.camera = arcade.Camera(self.width, self.height)

        # asign my sprite lists to their arcade lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        # Set up the player, specifically placing it at these coordinates.
        self.player_sprite = arcade.Sprite("Floor_board_wall - Copy.png", CHARACTER_SCALING)
        self.player_sprite.center_x = PLAYER_START_X
        self.player_sprite.center_y = PLAYER_START_Y
        self.player_list.append(self.player_sprite)

        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEngineSimple(
            self.player_sprite, self.wall_list)

    def on_draw(self):
        """Render the screen."""
        # clears the screen to background colour
        self.clear()

        # Activate our Camera
        self.camera.use()

        #player
        self.player_list.draw()
        

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

        # if self.draw_info:
        #     self.draw_info = False

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
        
    def center_camera_to_player(self):
            self.screen_left_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
            self.screen_bottom_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)
            player_centered = self.screen_left_x, self.screen_bottom_y
            self.camera.move_to(player_centered)

    

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called whenever the mouse button is clicked. """

        mouse_x = self.screen_left_x + x 
        mouse_y = self.screen_bottom_y + y


        # Get from the mouse the destination location for the bullet
        # IMPORTANT! If you have a scrolling screen, you will also need
        # to add in self.view_bottom and self.view_left.
        
        x_diff = mouse_x - self.player_sprite.center_x
        y_diff = mouse_y - self.player_sprite.center_y
        angle_in_radians = math.atan2(y_diff, x_diff)

        # Angle the bullet sprite so it doesn't look like it is flying
        # sideways.
        self.player_sprite.angle = math.degrees(angle_in_radians)
        print(f"Bullet angle: {self.player_sprite.angle:.2f}")
        
        
        



    

    def on_update(self, delta_time):  
    #updates the screen and changes frames
        self.player_list.update_animation(delta_time)

        # Move the player with the physics engine
        self.physics_engine.update()

        # Position the camera
        self.center_camera_to_player()
    
def main():
    """Main function"""   
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()