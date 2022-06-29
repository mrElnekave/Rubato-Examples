from rubato import *

# needs to be called in the first place we use rubato
init(res=Vector(500, 500))


# different scenes
main = Scene(name="main")
intro = Scene(name="intro")

player = None
