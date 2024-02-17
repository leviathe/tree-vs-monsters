from typing import Dict, List, Union

import pygame

# définir une classe pour les animations
from pygame.surface import Surface, SurfaceType


class AnimateSprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name, size=(200, 200)): # l'information à size sert d'information par défaut
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.size = size
        # définir une méthode pour animer le prite
        self.current_image = 0  # commencer l'animation à 0
        self.images = animations.get(sprite_name) # on récupère l'ensemble des images
        self.animation = False

    # définir une méthode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # définir une fonction pour charger les images d'un sprite
    def animate(self, loop=False):

        # vérifier que l'aniamtion est active
        if self.animation:

            # passer à l'image suivante
            self.current_image += 1

            # vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):

                # remettre l'animation au départ
                self.current_image = 0

                # vérifier que l'animation n'est pas en mode boucle
                if loop is False:
                    self.animation = False

            # modifier l'image précedente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

    def load_animation_images(sprite_name):

        # charger les images du dossier correspondant
        images = []

        # récuperer le chemin du dossier
        path = f"assets/{sprite_name}/{sprite_name}"

        # boucler sur chaque image du dossier
        for num in range(1, 24):
            image_path = path + str(num) + ".png"
            images.append(pygame.image.load(image_path))

        # renvoyer le contenu de la liste
        return images

    # définir un dictionnaire qui va contenir les images chargées de chaque sprite


animations = {
    'mummy': AnimateSprite.load_animation_images('mummy'),
    'player': AnimateSprite.load_animation_images('player'),
    'alien': AnimateSprite.load_animation_images('alien')
}
