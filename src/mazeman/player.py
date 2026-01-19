import pygame.sprite


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill("red")
        self.position = self.image.get_rect()

    def update(self, dt, keys):
        if keys[pygame.K_w]:
            self.position.y -= 300 * dt
        if keys[pygame.K_s]:
            self.position.y += 300 * dt
        if keys[pygame.K_a]:
            self.position.x -= 300 * dt
        if keys[pygame.K_d]:
            self.position.x += 300 * dt

    def draw(self, screen):
        screen.blit(self.image, self.position)
