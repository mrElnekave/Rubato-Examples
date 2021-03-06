import rubato as rb
from rubato import Scene, Vector, GameObject, Image, Color

rb.init()

# We start by making a scene, they are assets that hold all the Game Objects for a specific part of your application.
# In our case, this is the main Scene of our game
main = Scene()

# this is a Game Object we named player, it will house all the components relevant to player.
position = Vector(500, 500)  # A vector is representing a 2D point of the player's position.
player = GameObject(pos=position)

# add components to player
player_rect = rb.Rectangle(width=50, height=50, color=Color.red)  # A rectangle won't draw unless it has a color
player.add(player_rect)

# once you have a Game Object you must add it to the scene or else it doesn't exist.
main.add(player)

rb.begin()
