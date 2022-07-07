from rubato import *

init(res=Vector.one*150, window_size=Vector.one*2*300)

scene1 = Scene(name="scene1")
scene2 = Scene(name="scene2")

class PlayerC(Component):
    def __init__(self):
        super().__init__()
        self.image = Image(rel_path="art/Player1.png", z_index=1)
        self.rect = Rectangle(width=self.image.get_size().x, height=self.image.get_size().y, color=Color.red)
        self.speed = 100

    def setup(self):
        self.gameobj.add(self.image)
        self.gameobj.add(self.rect)

    def update(self):
        # print(Time.frames)

        if Input.key_pressed("a"):
            self.gameobj.pos.x -= self.speed * Time.delta_time
        if Input.key_pressed("w"):
            self.gameobj.pos.y -= self.speed * Time.delta_time
        if Input.key_pressed("s"):
            self.gameobj.pos.y += self.speed * Time.delta_time
        if Input.key_pressed("d"):
            self.gameobj.pos.x += self.speed * Time.delta_time
        if self.rect.right > Display.right:
            self.rect.right = Display.right
            print(self.gameobj.pos + self.rect.width / 2)
            if Game.scenes.current.id == scene1.id:
                self.rect.left = 0
                Game.scenes.set(scene2.id)
        elif self.rect.left < 0:
            self.rect.left = 0
            if Game.scenes.current.id == scene2.id:
                self.rect.right = Display.right
                Game.scenes.set(scene1.id)


def update():
    if Input.key_pressed("1"):
        Game.scenes.set(scene1.id)
    if Input.key_pressed("2"):
        Game.scenes.set(scene2.id)
    if Input.key_pressed("q"):
        player.get(PlayerC).rect.left = 0
    if Input.key_pressed("e"):
        player.get(PlayerC).rect.right = Display.right

def get_go(text):
    return GameObject(pos=Display.top_left + 50).add(text)

scene1.update = update
scene2.update = update

player = GameObject(name="player", pos=Display.center)
player.add(PlayerC())
scene1.add(player, get_go(Text(text="Scene 1")))
scene2.add(player, get_go(Text(text="Scene 2")))

begin()
