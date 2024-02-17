import pygame
import random
import animation
import math


# créer une classe qui va g"rer la notion de monstre sur notre jeu

class Monster(animation.AnimateSprite):  # super classe provenant d'animation.py

    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)  # nom du monstre à convertir en sprite avec la taille
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.loot_amount = 10
        self.rect = self.image.get_rect()
        self.rect.x = 975 + random.randint(0, 100)
        self.rect.y = 540 - offset
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, self.default_speed)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        # infliger des dégâts
        self.health -= amount

        # vérifier si son nouveau nombre de points de vie est inférieur ou égal à 0
        if self.health <= 0:
            # ajouter les points
            self.game.add_score(self.loot_amount)

            # (supprimer ou) le faire réapparaitre comme un nouveau monstre
            self.rect.x = 975 + random.randint(0, 100)
            self.velocity = random.randint(1, self.default_speed)
            self.health = self.max_health

        # vérifier que la barre d'événement est chargée
        if self.game.comet_event.is_full_loaded():
            # retirer les monstres du jeu
            self.game.all_monsters.remove(self)

            # invoquer la pluie de météorite
            self.game.comet_event.attempt_fall()

    # définir la boucle d'animation
    def update_animation(self):
        self.animate(loop=True)

    # définir l'actualisation de la barre de vie
    def update_health_bar(self, surface):

        # dessiner notre barre de vie
        #               zone d'application | couleur | position [x, y, longueur, épaisseur]
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 12, self.rect.y - 20, self.max_health, 5])
        #  barre de vie créée par dessus l'arrière plan de la jauge de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 12, self.rect.y - 20, self.health, 5])

    def forward(self):
        # le déplacement ne se fait que s'il n'y a pas de collision  avec un groupe de joueur
        if not self.game.check_collision(self, self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision avec le joueur
        else:
            # infliger des dégâts
            self.game.player.damage(self.attack)


# définir une classe pour la momie
class Mummy(Monster):
    def __init__(self, game):
        super().__init__(game, 'mummy', (130, 130))  # le tuple sert à indiquer la taille
        self.set_speed(3)
        self.set_loot_amount(20)


# définir une classe alien
class Alien(Monster):
    def __init__(self, game):
        super().__init__(game, 'alien', (300, 300), 130)
        self.health = 250
        self.max_health = 250
        self.attack = 0.8
        self.set_speed(1)
        self.set_loot_amount(80)
