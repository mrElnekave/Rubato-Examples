import pygame as pg, sys
mainClock = pg.time.Clock()
pg.init()
WINDOWWIDTH = 600
WINDOWHEIGHT = 400
screen = pg.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))


class Player:
    def __init__(self):
        self.rect = pg.Rect(200, 0, 10, 10)
        self.velocity = pg.Vector2(0, 0)
        print(self.rect)

    def draw(self, screen):
        pg.draw.rect(screen, (255, 0, 0), self.rect)


player = Player()
while True:

    # Input
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_LEFT:
                player.velocity.x = -5
            if event.key == pg.K_RIGHT:
                player.velocity.x = 5
            if event.key == pg.K_UP:
                player.velocity.y = -5
            if event.key == pg.K_DOWN:
                player.velocity.y = 5
        elif event.type == pg.KEYUP:
            if event.key == pg.K_LEFT:
                player.velocity.x = 0
            if event.key == pg.K_RIGHT:
                player.velocity.x = 0
            if event.key == pg.K_UP:
                player.velocity.y = 0
            if event.key == pg.K_DOWN:
                player.velocity.y = 0

    # Update
    player.rect.left += player.velocity.x
    player.rect.top += player.velocity.y

    # Draw
    screen.fill((0, 0, 0))
    player.draw(screen)

    pg.display.update()
    mainClock.tick(40)
