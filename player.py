import pygame
from projectile import Projectile
import animation

pygame.init()


# créer une classe pour le joueur
class Player(animation.AnimateSprite):

    def __init__(self, game):
        super().__init__('player')  # pour initialiser la super classe
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 15
        self.velocity = 6
        self.all_projectiles = pygame.sprite.Group()  # chaque projectile lancer sera rangé dans ce groupe
        self.rect = self.image.get_rect()  # créer un rectangle déplaçable
        self.rect.x = 400
        self.rect.y = 500

    def update_animation(self):
        self.animate()

    def damage(self, amount):
        if self.health - amount > amount :
            self.health -= amount
        else :
            self.game.game_over()


    def move_right(self):
        # si le joueur n'est pas en collision avec un monstre
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x += self.velocity

    def update_health_bar(self, surface):
        # dessiner notre barre de vie
        #               zone d'application | couleur | position [x, y, longueur, épaisseur]
        pygame.draw.rect(surface, (60, 63, 60),  [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])

        #  barre de vie créée par dessus l'arrière plan de la jauge de vie
        pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5])

    def move_left(self):
        self.rect.x -= self.velocity

    def launch_projectile(self):
        # créer une nouvelle instance de la classe projectile
        self.all_projectiles.add(Projectile(self))

        # démarrer l'animation de lancer
        self.start_animation()

        # jouer le son
        self.game.sound_manager.play('tir')