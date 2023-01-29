import pygame as pg
from random import randint, choice

WIDTH, HEIGHT = 900, 500
WIN = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Flames")



dt = 0.2
F = 10
n = 15


BLACK = (0, 0, 0)
ORANGE1 = [252, 126, 0]
ORANGE2 = [252, 92, 0]
ORANGE3 = [252, 46, 0]

colors = [ORANGE1, ORANGE2, ORANGE3]

class Flame:

    particles = []

    def __init__(self, x, y):
        ORANGE1 = [252, 126, 0]
        ORANGE2 = [252, 92, 0]
        ORANGE3 = [252, 46, 0]

        colors = [ORANGE1, ORANGE2, ORANGE3]

        self.x = randint(x - 10, x + 10)
        self.y = randint(y - 10, y)
        self.max = randint(y + 30, y + 100)
        self.vy = 6
        self.vx = 0
        self.r = randint(1, 2)
        self.color = choice(colors)
        self.particles.append(self)

    def update(particles):
        for particle in particles:
            if particle.vx >= 0:
                particle.vx = randint(1, 2)
            else:
                particle.vx = randint(-1, -2)

            particle.x -= particle.vx * dt
            particle.y -= particle.vy * dt

            for i in range(len(particle.color) - 1):
                if particle.color[i] - F < 0:
                    continue
                else:
                    particle.color[i] -= F

    def draw(particles):
        for particle in particles:
            color = (particle.color[0], particle.color[1], particle.color[2])
            pg.draw.circle(WIN, color, (particle.x, particle.y), particle.r)



def main():
    clock = pg.time.Clock()

    particles = Flame.particles

    fire = False
    run = True
    while run:
        clock.tick(60)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False 

            if event.type == pg.MOUSEBUTTONDOWN:
                fire = True
            
            if event.type == pg.MOUSEBUTTONUP:
                fire = False

            if event.type == pg.MOUSEMOTION:
                if fire:
                   x, y = pg.mouse.get_pos()
                   for i in range(n):
                       Flame(x, y)

        WIN.fill(BLACK)
        Flame.draw(particles)
        Flame.update(particles)
            
        pg.display.flip()

    pg.quit()


main()