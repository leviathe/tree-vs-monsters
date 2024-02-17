import pygame

pygame.init()
from player import Player
from monster import Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


# creer une classe pour représenter le jeux
class Game:

    def __init__(self):
        self.is_playing = False  # définir si le jeu a commencé ou non
        # générer le joueur puis le mettre dans un groupe pour checker les collisions du monstre
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFallEvent(self)  # générer l'événement
        self.all_monsters = pygame.sprite.Group()  # groupe de monstre
        self.pressed = {}  # Va afficher valeurs bouléenne pour les touches activées
        self.font = pygame.font.Font("assets/my_custom_font.ttf", 25)  # police d'écriture du score
        self.score = 0  # mettre le score à 0
        self.sound_manager = SoundManager()  # gérer le son

    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)  # Va générer un premier monstre dès le début
        self.spawn_monster(Alien)

    def add_score(self, points=10):
        self.score += points

    def game_over(self):
        # remettre le jeu à zéro
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        # jouer le son
        self.sound_manager.play('game_over')

    def update(self, screen):
        # afficher le score sur l'écran
        score_text = self.font.render(f"Score : {self.score}", 1, (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # afficher joueur
        screen.blit(self.player.image, self.player.rect)

        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)
        self.player.update_animation()

        # actualiser la barre d'événement du jeu
        self.comet_event.update_bar(screen)

        # récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # récupérer les monstres du joueurs
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        # récupérer les comètes
        for comet in self.comet_event.all_comets:
            comet.fall()

        # appliquer l'ensemble des images du groupe de projectiles
        self.player.all_projectiles.draw(screen)  # simple car permet d'afficher les groupes

        # appliquer l'ensemble des images du groupe de monstres
        self.all_monsters.draw(screen)

        # appliquer l'ensemble des images du groupe de comètes
        self.comet_event.all_comets.draw(screen)

        # vérifier si le joueur souhaite aller à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))  # .__call__() servant à faire les instances mais
        # pas à faire passer les arguments. Par ex :
        # Alien.__call__() == Alien().

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)
