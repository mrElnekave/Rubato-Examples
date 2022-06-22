import rubato as rb
from rubato import Scene, Vector, GameObject, Image, Color, Input, Time, Display

rb.init()

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

player = GameObject(pos=Vector(500, 500))

player_rect = rb.Rectangle(width=50, height=50, color=Color.red)
player.add(player_rect)  # A rectangle won't draw unless it has a color

speed = 5
fixed_speed = 50  # It will move 50 frames per second
def update():
    if Input.key_pressed("a"):
        player.pos.x -= speed
        player_rect.color = Color.red
    if Input.key_pressed("w"):
        player.pos.y -= fixed_speed * Time.delta_time  # How much I should have moved since last frame.
    if Input.key_pressed("s"):
        player.pos.y += fixed_speed * Time.delta_time
    if Input.key_pressed("d"):
        player.pos.x += speed
        player_rect.color = Color.blue


main.update = update

main.add(player)

rb.begin()
