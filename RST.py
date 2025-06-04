#!/usr/bin/env python3
# Created by: Enoch Amedjrovi
# Created on: March 2, 2025
# This program asks the user for their grade level and tells them their percentage


import ugame
import stage



def game_scene():
    #This function is the main game scene


    image_bank_background = stage.Bank.from_bmp16("space_aliens_background.bmp")
    background = stage.Grid(image_bank_background, 10, 8)


    game = stage.Stage(ugame.display, 60)
    game.layers = [background]
    game.render_block()


    while True:
        # repeat forever, or you turn it off!
        pass # just a place holder


if __name__ == "__main__":
    game_scene()

