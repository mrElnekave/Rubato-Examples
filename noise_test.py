"""A noise drawing demo for rubato"""
from rubato import *
import math

init(
    name="drawings",
    window_size=Vector(500, 500),
    res=Vector(500, 500),
    target_fps=24,
    background_color=Color(255, 255, 255),
    icon="",
)

main = Scene()

noise_size: Vector = Vector.one * 10
degrees: int = 1
Game.debug = True
num_points: int = 300

draw_offset: Vector = Display.center_left + Vector.right * Display.res.x * 0.5


def draw():
    points: list[Vector] = []
    angle = 0
    while angle < 2 * math.pi:
        sample_offset: Vector = (
            Vector(Math.lerp(0, noise_size.x, math.cos(angle)), Math.lerp(0, noise_size.x, math.sin(angle)))
        )
        radius = Math.lerp(100, 120, (Noise.noise2(sample_offset.x, sample_offset.y) + 1) / 2)
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        points.append((Vector(x, y) + draw_offset).to_int())

        angle += math.radians(degrees)

    Draw.poly(points, Color.black, fill=Color.red)


width, height = 50, 50

main.draw = draw

begin()
