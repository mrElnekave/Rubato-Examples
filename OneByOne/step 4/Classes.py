import rubato as rb
from rubato import Input, Color, Time


# Component overriding.

class PlayerController(rb.Component):
    def __init__(self, image_location, speed):

        super().__init__()  # you must call super().__init__()

        self.image = rb.Image(rel_path=image_location)  # right now not doing anything with image
        self.speed = speed

    def setup(self):
        """
        Here you have access to the GameObject of the component and is where you should set any variables that depend
        on the GameObject.
        Automatically run once before the first update call.
        """
        # Only here can we get the rect from our game object and assign the image
        self.rect = self.gameobj.get(rb.Rectangle)

    def update(self):
        """
        Called once per frame. Before the draw function.
        """

        # We moved the input into here. And changed it all to use delta_time
        if Input.key_pressed("a"):
            self.gameobj.pos.x -= self.speed * Time.delta_time
            self.rect.color = Color.red
        if Input.key_pressed("w"):
            self.gameobj.pos.y -= self.speed * Time.delta_time
        if Input.key_pressed("s"):
            self.gameobj.pos.y += self.speed * Time.delta_time
        if Input.key_pressed("d"):
            self.gameobj.pos.x += self.speed * Time.delta_time
            self.rect.color = Color.blue
