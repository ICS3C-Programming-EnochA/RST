#!/usr/bin/env python3
# Created by: Enoch Amedjrovi
# Created on: March 2, 2025
# This program asks the user for their grade level and tells them their percentage


import ugame
import stage




def game_scene():
    #This function is the main game scene

    #image banks for CircuitPython
    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    image_bank_sprites = stage.Bank.from_bmp16("space_aliens.bmp")

    #sets the background to image 0 in the image bank
    # and the sie (10x8 tiles of size 16x16)
    background = stage.Grid(image_bank_background, 10, 8)

    ship = stage.Sprite(image_bank_sprites, 5, 75, 66)

    #create the stage for the background to show up on
    # and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    #set the layers, items show up in order
    game.layers = [ship] + [background]
    #render the background and initial location of sprite list 
    #Most likely you will only render background once per scene
    game.render_block()

    #repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw Sprites
        game.render_sprites([ship])
        game.tick()

if __name__ == "__main__":
    game_scene()

