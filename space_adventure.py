import pygame


class Ship:
    def __init__(self, ship_name, ship_type, ship_img, initial_position):
        # ship parameters
        self.name = ship_name
        self.type = ship_type
        self.turn_angle = 0
        self.turn_rate_angle = 10
        self.speed = 0

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

    def move_ship(ship, rect, target):
        pass

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

            print(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_ship.turn_ship(player_ship.turn_angle + player_ship.turn_rate_angle)

        gameDisplay.blit(space, (0, 0))
        gameDisplay.blit(player_ship.ship_img, player_ship.get_display_rect())
        pygame.display.update()
        clock.tick(60)


main()
