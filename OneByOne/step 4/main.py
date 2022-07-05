import rubato as rb
from rubato import Scene, Vector, GameObject, Image, Color, Input, Time, Display
from Classes import PlayerController

# Pass in a custom resolution for the screen.
# This will make everything look bigger.
# As the screen's resolution is much smaller and needs to be scaled more to match the window.
rb.init(res=Vector(500, 500))

# different scenes
main = Scene(name="main")
intro = Scene(name="intro")

goToGame = GameObject(pos=Display.center)
goToGame.add(rb.Rectangle(width=300, height=70, color=Color.lime, z_index=-1))
goToGame.add(rb.Text(text="Start4", font=rb.Font(size=64), z_index=1))
goToGame.add(rb.Button(width=300, height=40, onclick=lambda: rb.Game.scenes.set(main.id)))

intro.add_ui(goToGame)

rb.Game.scenes.set(intro.id)


# Second scene

player = GameObject(pos=Vector(250, 250))

player_rect = rb.Rectangle(width=50, height=50, color=Color.red)
player.add(player_rect)  # A rectangle won't draw unless it has a color
player.add(PlayerController("../art/Player1.png", 200))


main.add(player)

rb.begin()
