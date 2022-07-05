import rubato as rb
from rubato import Input, Color, Time, Vector, Manifold
import objects


# Component overriding.

class PlayerController(rb.Component):
    def __init__(self, image_location, speed):

        super().__init__()  # you must call super().__init__()

        self.image = rb.Image(rel_path=image_location)
        self.speed = speed

    def setup(self):
        """
        Here you have access to the GameObject of the component and is where you should set any variables that depend
        on the GameObject.
        Automatically run once before the first update call.
        """
        # Only here can we get the rect from our game object and assign the image
        self.rect = self.gameobj.get(rb.Rectangle)

        # resizing our image to our hitbox's size
        self.image.resize(Vector(50, 50))
        self.gameobj.add(self.image)

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


class Coin(rb.Component):
    def __init__(self):
        super().__init__()
        self.image = rb.Image(rel_path="../art/Silver Coin.png")
        self.rect = rb.Rectangle(width=self.image.get_size().x, height=self.image.get_size().y)

    def setup(self):
        self.gameobj.add(self.image)
        self.gameobj.add(self.rect)
        self.rect.on_collide = self.on_collide  # Setting the rectangle with our custom on_collide function.

    def on_collide(self, manifold: Manifold):
        # A manifold is passed in when a collision occurs.
        # In short, it holds shape_a, which holds self under `.gameobj`, and shape_b which is what self collided with.
        # You may check the documentation for more information.
        if manifold.shape_b.gameobj.name == "player":  # We check if we collided with the player.
            objects.main.delete(self.gameobj)
