from code.PlayerShot import PlayerShot
from code.Entity import Entity
from code.Const import ENTITY_SHOT_DELAY, PLAYER_KEY_SHOOT, WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_UP, PLAYER_KEY_RIGHT, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT
import pygame


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]

        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]

            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                return PlayerShot(f'{self.name}Shot', (self.rect.centerx, self.rect.centery))
            else:
                return None
        else:
                return None