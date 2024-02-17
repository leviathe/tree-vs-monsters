import pygame
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()

        # définir l'image
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1,3)
        self.rect.x = random.randint(5, 1795)  # on pourrait récupérer la longueur de la fenêtre
        self.rect.y = -random.randint(0, 1800)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)

        # vérifier si le nombre de comete est de 0
        if len(self.comet_event.all_comets) == 0:

            # remettre la barre à 0
            self.comet_event.reset_percent()

            # apparaitre les 2 premiers monstres
            self.comet_event.game.start() # on déclenche la fonction start où on a déjà nos monstres à faire apparaître

    def fall(self):
        self.rect.y += self.velocity

        # vérifier si la comete touche le sol
        if self.rect.y >= 500:
            self.remove()
            # jouer le son
            self.comet_event.game.sound_manager.play('meteorite')

        # vérifier si la comete touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):

            self.remove()
            self.comet_event.game.player.damage(20)

        # vérifier qu'il n'y a plus de comete
        if len(self.comet_event.all_comets) == 0:

            # remettre la jauge au départ
            self.comet_event.reset_percent()
            self.comet_event.fall_mode = False
