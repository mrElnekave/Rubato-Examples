import rubato as rb
import time
from rubato import Vector as V

rb.init(window_size=V(640,480), res=V(640,480))

speed = 200
countThings = 0

main_scene = rb.Scene()

player = rb.GameObject("red dot", rb.Display.center)
p_color = rb.Color.red
dir = rb.Vector(0, 0)
avocado = rb.Image(rel_path="art/avocado.png")
player.add(avocado)

# music = rb.Sound("sound/lemmeseeifyoucandance.mp3", "nttd")
# music.play()
# horn = rb.Sound("sound/inceptionHorn2.mp3")
rb.Sound.import_sound_folder("sound")
music = rb.Sound.get_sound("lemmeseeifyoucandance")
#music.play()

rb.Time.delayed_call(10, lambda: avocado.resize(rb.Vector(50,50)))

def doit():
    global countThings
    countThings += 1
    print("hi "+str(countThings)+" "+str(time.time()))
    rb.Time.delayed_call(1000, doit)
    #rb.Sound.get_sound("inceptionHorn2").play(0)

txt = rb.Text(offset=V(0,-200), text="hello world", width=1000, font=rb.Font())
player.add(txt)

rb.Time.delayed_call(1000, doit)

def scene_update():
    global dir
    dir = rb.Vector(0, 0)
    if rb.Input.key_pressed("left"):
        dir.x = -1
    if rb.Input.key_pressed("right"):
        dir.x = 1
    if rb.Input.key_pressed("down"):
        dir.y = 1
    if rb.Input.key_pressed("up"):
        dir.y = -1
    if rb.Input.mouse_pressed():
        delta = rb.Input.get_mouse_pos() - player.pos
        dir = delta.unit()
    player.pos += dir * speed * rb.Time.delta_time / 1000

def scene_draw():
    rb.Draw.circle(player.pos, 20, rb.Color.black, 3, p_color)

main_scene.update = scene_update
main_scene.draw = scene_draw
main_scene.add(player)

rb.begin()
