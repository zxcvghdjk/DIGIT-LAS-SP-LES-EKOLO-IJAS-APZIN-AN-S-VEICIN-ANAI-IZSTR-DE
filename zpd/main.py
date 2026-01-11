import pygame
from sprites import *
from config import * 
import sys

class Game:
    def _init_(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Arial',32)
