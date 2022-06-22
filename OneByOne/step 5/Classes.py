import rubato as rb
from rubato import Input, Color, Time, Vector


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

    def collide(self, pos: Vector):
        if self.rect.top_left <= pos <= self.rect.bottom_right:
            return True
        return False


class PlayerControllerGOOD(rb.Component):
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
