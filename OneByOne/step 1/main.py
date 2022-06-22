import rubato as rb
from rubato import Scene, Vector, GameObject, Image, Color

rb.init()

# We start by making a scene, they are assets that hold all the Game Objects for a specific part of your application.
# In our case, this is the main Scene of our game
main = Scene()

# this is a Game Object we named player, it will house all the components relevant to player.
player = GameObject(pos=Vector(500, 500))

# add components to player
player.add(rb.Rectangle(width=50, height=50, color=Color.red))  # A rectangle won't draw unless it has a color

# once you have a Game Object you must add it to the scene or else it doesn't exist.
main.add(player)

rb.begin()
