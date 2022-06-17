import rubato as rb

rb.init()

main_scene = rb.Scene()

player = rb.GameObject(name="player", pos=rb.Display.center)
player.add(rb.Rectangle(color=rb.Color.red, width=100, height=100))
main_scene.add(player)

speed = 100


def main_update():
    if rb.Input.key_pressed("left"):
        player.pos.x -= speed * rb.Time.delta_time
    if rb.Input.key_pressed("right"):
        player.pos.x += speed * rb.Time.delta_time
    if rb.Input.key_pressed("up"):
        player.pos.y -= speed * rb.Time.delta_time
    if rb.Input.key_pressed("down"):
        player.pos.y += speed * rb.Time.delta_time


main_scene.update = main_update
rb.begin()
