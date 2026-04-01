import pygame
import sys
import math

pygame.init()

radius = int(input("Enter circle size (radius): "))
spin_speed = float(input("Enter spin speed (e.g. 0.05): "))

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Movable Circle with Input")

clock = pygame.time.Clock()

x, y = WIDTH // 2, HEIGHT // 2
color = (0, 255, 255)
speed = 5
angle = 0

running = True
while running:
    screen.fill((30, 30, 30))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    angle += spin_speed

    pygame.draw.circle(screen, color, (x, y), radius)

    end_x = x + int(radius * math.cos(angle))
    end_y = y + int(radius * math.sin(angle))
    pygame.draw.line(screen, (255, 0, 0), (x, y), (end_x, end_y), 3)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()