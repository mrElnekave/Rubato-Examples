from rubato import *

# needs to be called in the first place we use rubato
init(  # extra fancies
    name="Game",
    res=Vector(500, 500),
    icon="../art/avocado.png"
)


# different scenes
main = Scene(name="main")
intro = Scene(name="intro")

player = None
