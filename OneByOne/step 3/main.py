import rubato as rb
from rubato import Scene, Vector, GameObject, Image, Color, Input, Time, Display

rb.init()

# different scenes
main = Scene(name="main")
intro = Scene(name="intro")

# Here we are making game objects that will live in the intro scene.

# The
goToGame = GameObject(pos=Display.center)

# As we add the components of our goToGame button object, we assign relative indexes to them.
# This tells the engine which component should be drawn first.
goToGame.add(rb.Rectangle(width=300, height=70, color=Color.lime, z_index=-1))  # The button background behind the text.
# The text of the button. Note: we make our own font for a new size, each change to the text itself is a new font.
goToGame.add(rb.Text(text="Start3", font=rb.Font(size=64), z_index=1))
# The button is simply a bounding box, that can interact with the mouse.
# We use a lambda to be called when the button is clicked, we switch the scenes.
goToGame.add(rb.Button(width=300, height=40, onclick=lambda: rb.Game.scenes.set(main.id)))

# If you are up for a challenge implement pressing on the button to change the scene just using the rectangle
# and `Input.mouse_pressed()`, `Input.get_mouse_pos()`

# Solution:
# def intro_update():
#     # we can get the rectangle component from our game object
#     rectangle = goToGame.get(rb.Rectangle)
#     if Input.mouse_pressed():  # if the mouse is pressed
#         pos = Input.get_mouse_pos()
#         if rectangle.top_left <= pos <= rectangle.bottom_right:  # if the mouse is inside the rectangle
#             rb.Game.scenes.set(main.id)  # switch to the main scene

intro.add_ui(goToGame)

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
