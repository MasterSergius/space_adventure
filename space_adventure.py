import math
import pygame


class Ship:
    def __init__(self, ship_name, ship_type, ship_img, initial_position):
        # ship parameters
        self.name = ship_name
        self.type = ship_type
        self.turn_angle = 0
        self.turn_rate_angle = 10
        self.move_speed = 10
        self.current_speed = 0
        self.move_target = None

        # img parameters
        self.ship_img = ship_img
        self.ship_img_orig = ship_img
        self.position = initial_position
        self.display_rect = self.ship_img.get_rect()
        self.display_rect.center = initial_position

    def get_display_rect(self):
        return self.display_rect

    def turn_ship(self, angle):
        x, y = self.display_rect.center
        self.ship_img = pygame.transform.rotate(self.ship_img_orig, angle)
        self.display_rect = self.ship_img.get_rect()
        self.display_rect.center = (x, y)
        self.turn_angle = angle

    def set_move_target(self, target):
        self.move_target = target

    def set_new_position(self, dx, dy):
        self.position = (self.position[0] + dx, self.position[1] + dy)
        self.display_rect.center = self.position

    def move_ship(self):
        if self.move_target and self.position != self.move_target:
            # TODO: turn ship in target direction
            angle = math.atan2(self.move_target[1] - self.position[1], self.move_target[0] - self.position[0])
            turn_angle = -angle * 180 / math.pi
            self.turn_ship(turn_angle-90)
            # TODO: calculate correct velocity for x and y
            vel_x = 0
            vel_y = 0
            vel_y = int(round(self.move_speed * math.sin(angle)))
            vel_x = int(round(self.move_speed * math.cos(angle)))
            distance_x = self.move_target[0] - self.position[0]
            distance_y = self.move_target[0] - self.position[0]
            if abs(distance_x) < abs(vel_x):
                vel_x = distance_x
            if abs(distance_y) < abs(vel_y):
                vel_y = distance_y
            self.set_new_position(vel_x, vel_y)
            # stop near the target
            if abs(vel_x) <= 3 and abs(vel_y) <= 3:
                self.move_target = None


def main():
    pygame.init()

    size = width, height = 800, 600
    player_ship_x = width / 2
    player_ship_y = height / 2

    gameDisplay = pygame.display.set_mode(size)
    pygame.display.set_caption('Space Adventure')

    clock = pygame.time.Clock()

    space = pygame.image.load('images/space.png')
    human_transport_A_img = pygame.image.load('images/ship-1.png')
    player_ship = Ship('Firefly', 'transport_A', human_transport_A_img, (player_ship_x, player_ship_y))

    crashed = False
    while not crashed:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                # player_ship.turn_ship(player_ship.turn_angle + player_ship.turn_rate_angle)
                player_ship.set_move_target(event.pos)

        player_ship.move_ship()

        gameDisplay.blit(space, (0, 0))
        gameDisplay.blit(player_ship.ship_img, player_ship.get_display_rect())
        pygame.display.update()
        clock.tick(60)


main()
