import rubato as rb
from rubato import Vector, GameObject, Image, Color, Input, Time, Display
from Classes import *
import random
import objects

# Pass in a custom resolution for the screen.

goToGame = GameObject(pos=Display.center)
goToGame.add(boundingbox := rb.Rectangle(width=300, height=40, color=Color.lime, z_index=-1))
goToGame.add(rb.Text(text="Start", font=rb.Font(size=36), z_index=1))

objects.intro.add_ui(goToGame)


def intro_update():
    if Input.mouse_pressed():
        pos = Input.get_mouse_pos()
        if boundingbox.top_left <= pos <= boundingbox.bottom_right:
            rb.SceneManager.set(objects.main.id)


objects.intro.update = intro_update
rb.Game.scenes.set(objects.intro.id)


# Second scene

objects.player = GameObject(pos=Vector(250, 250), name="player")

player_rect = rb.Rectangle(width=50, height=50)
objects.player.add(player_rect)  # A rectangle won't draw unless it has a color
objects.player.add(PlayerController("../art/Player1.png", 200))

coins = []
for i in range(17):
    coin = GameObject(pos=Vector(random.random()*Display.res.x, random.random()*Display.res.y))
    coin.add(c := Coin())
    coins.append(coin)

# adding the enemy
enemy = GameObject(pos=Vector(random.random()*Display.res.x, random.random()*Display.res.y), name="enemy")
enemy.add(EnemyController())

# def func():
#     rb.Game.camera.pos = rb.Game.camera.transform(Input.get_mouse_pos()) + rb.Game.camera.pos - Display.center
# rb.Radio.listen(rb.Events.MOUSEDOWN, func)
# def func2():
#     rb.Game.camera.pos = Vector(0, 0)
# rb.Radio.listen(rb.Events.MOUSEUP, func2)
def update():
    target = objects.player.pos - Display.center
    rb.Game.camera.pos = rb.Game.camera.pos.lerp(target, 0.01)

objects.main.update = update

objects.main.add(objects.player, *coins, enemy)
rb.begin()
