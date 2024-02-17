import pygame
import math
from game import Game

# définir une horloge
clock = pygame.time.Clock()
FPS = 60

pygame.init()

# générer la fenetre de notre jeu
pygame. display.set_caption("Comet fall Game") # methode qui gère l'affichage
screen = pygame.display.set_mode((1080, 720))

# importer un background
background = pygame.image.load('assets/bg.jpg')

# importer / charger la bannière
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width() / 4) # math.ceil sert à faire une approximation


# import / charge de notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)

# charger jeux
game = Game()

#boucle tant que la condition est vrai
running = True
while running:

    # appliquer l'arriere plan
    screen.blit(background, (0, -200))

    # vérifier si notre jeu a commencé ou non
    if game.is_playing:

        # déclencher les instructions de la partie
        game.update(screen)

    #vérifier si le jeu n'a pas commencé
    else:

        #ajouter mon écran de bienvenu
        screen.blit(play_button, play_button_rect)
        screen.blit(banner, banner_rect)

    # mettre à jour l'écran
    pygame.display.flip()

    # si le joueur ferme la fenetre
    # on récupère les événement dan la liste d'événement
    for event in pygame.event.get():
        # on vérifie l'evenement de fermeture de la fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print(" Fermeture du jeu")

        # si le joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            # détecter si la touche espace est enclenchée
            if event.key == pygame.K_SPACE:

                if game.is_playing:

                    game.player.launch_projectile()

                else:
                    game.start()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            # vérification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):

                # mettre le jeu en mode running
                game.start()

                # jouer le son
                game.sound_manager.play('click')

    # fixer le nombre de fps sur mon horloge
    clock.tick(FPS)