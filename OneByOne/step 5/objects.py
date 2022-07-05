from rubato import *

# We must remove other init calls, and only have one init call, where it will first be run.
init(res=Vector(500, 500))

# We have moved our different scenes to a shared objects file, so they are accessible from everywhere.
main = Scene(name="main")
intro = Scene(name="intro")
