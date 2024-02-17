import pygame
from comet import Comet


# créer une classe pour gérer l'événement
class CometFallEvent:

    # lors du chargement -> créer un compteur pour la barre d'événement
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 5
        self.game = game
        self.fall_mode = False

        # définir un groupe de sprite
        self.all_comets = pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        # boucle pour les valeurs entre 1 et 10
        for i in range(1, 10):
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        # la jauge d'événement est totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            print("pluie de comète !!")
            self.meteor_fall()
            self.fall_mode = True

    def update_bar(self, surface):
        # ajouter du pourcentage
        self.add_percent()

        # barre arriere plan
        pygame.draw.rect(surface, (0, 0, 0), [0, surface.get_height() - 20, surface.get_width(), 10])

        # barre d'événement
        pygame.draw.rect(surface,
                         (187, 11, 11),
                         [0, surface.get_height() - 20, surface.get_width() / 100 * self.percent, 10]
                         )
