import rubato as rb
from rubato import Vector, GameObject, Image, Color, Input, Time, Display
import objects
from Classes import *
import random

goToGame = GameObject(pos=Display.center)
goToGame.add(rb.Rectangle(width=300, height=70, color=Color.lime, z_index=-1))
goToGame.add(rb.Text(text="Start7", font=rb.Font(size=64), z_index=1))
goToGame.add(rb.Button(width=300, height=40, onclick=lambda: rb.Game.scenes.set(objects.main.id)))

objects.intro.add_ui(goToGame)

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

camera_follow_strength = 2
def update():
    target = objects.player.pos - Display.center
    rb.Game.camera.pos = rb.Game.camera.pos.lerp(target, camera_follow_strength * Time.delta_time)
    # rb.Game.camera.pos.clamp()


objects.main.update = update

objects.main.add(objects.player, *coins, enemy)
rb.begin()
