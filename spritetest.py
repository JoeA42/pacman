import pygame
import spritesheet

ss = spritesheet.spritesheet("todos.png")
# Sprite is 16x16 pixels at location 0,0 in the file...
image = ss.image_at((3, 160, 16, 16))
