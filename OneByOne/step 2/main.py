import rubato as rb
from rubato import Scene, Vector, GameObject, Image, Color, Input, Time

rb.init()

main = Scene()

player = GameObject(pos=Vector(500, 500))

player_rect = rb.Rectangle(width=50, height=50, color=Color.red)
player.add(player_rect)

# overriding an update
# This runs at an uncapped speed, as fast as possible.
# Ways to have a set speed are to cap the frame rate, or to multiply by Time.delta_time
speed = 5
fixed_speed = 50  # It will move 50 frames per second
def update():
    if Input.key_pressed("a"):
        player.pos.x -= speed
        # Please note this means every frame you move 5 pixels, if you had a slow computer this would be slower.
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
