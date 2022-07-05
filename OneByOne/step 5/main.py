import rubato as rb
from rubato import Vector, GameObject, Image, Color, Input, Time, Display
from Classes import PlayerController, Coin
import random
import objects


goToGame = GameObject(pos=Display.center)
goToGame.add(rb.Rectangle(width=300, height=70, color=Color.lime, z_index=-1))
goToGame.add(rb.Text(text="Start5", font=rb.Font(size=64), z_index=1))
goToGame.add(rb.Button(width=300, height=40, onclick=lambda: rb.Game.scenes.set(objects.main.id)))

objects.intro.add_ui(goToGame)

rb.Game.scenes.set(objects.intro.id)


# Second scene

player = GameObject(pos=Vector(250, 250), name="player")

player_rect = rb.Rectangle(width=50, height=50, color=Color.red)
player.add(player_rect)  # A rectangle won't draw unless it has a color
player.add(PlayerController("../art/Player1.png", 200))


# adding coins that can be picked up.
coins = []
for i in range(17):
    coin = GameObject(pos=Vector(random.random()*Display.res.x, random.random()*Display.res.y))
    coin.add(c := Coin())
    coins.append(coin)

objects.main.add(player, *coins)
rb.begin()
