import rubato as rb
from rubato import Scene, Vector, GameObject, Image, Color, Input, Time, Display
from Classes import PlayerController

# Pass in a custom resolution for the screen.
rb.init(res=Vector(500, 500))

# different scenes
main = Scene(name="main")
intro = Scene(name="intro")

goToGame = GameObject(pos=Display.center)
goToGame.add(boundingbox := rb.Rectangle(width=300, height=40, color=Color.lime))  # TODO: talk about z index
goToGame.add(rb.Text(text="Start", width=300, font=rb.Font(size=36)))  # TODO: width bug fixed

intro.add_ui(goToGame)

def intro_update():
    if Input.mouse_pressed():
        pos = Input.get_mouse_pos()
        if boundingbox.top_left <= pos <= boundingbox.bottom_right:
            rb.Game.scenes.set(main.id)


intro.update = intro_update
rb.Game.scenes.set(intro.id)


# Second scene

player = GameObject(pos=Vector(250, 250))

player_rect = rb.Rectangle(width=50, height=50, color=Color.red)
player.add(player_rect)  # A rectangle won't draw unless it has a color
player.add(PlayerController("../art/Player1.png", 200))


main.add(player)

rb.begin()
