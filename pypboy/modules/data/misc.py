import pypboy
import pygame
import config
import game
import random

from pypboy.modules.data import entities


class Module(pypboy.SubModule):

    label = "Misc"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.notes = Notes()
        self.notes.image = pygame.image.load('images/Quests/1.bmp')
        self.notes.rect[0] = 240
        self.notes.rect[1] = 50
        self.add(self.notes)
        self.menu = pypboy.ui.Menu(240, ['{: <22}'.format("Favourite Movies"),
                                         '{: <22}'.format("Favourite TV Series"),
                                         '{: <22}'.format("Favourite Books"),
                                         '{: <22}'.format("Favourite Games"),
                                         '{: <22}'.format("Favourite Music Genres"),
                                         '{: <22}'.format("Favourite Dish"),
                                         '{: <22}'.format("Favourite Colour"),
                                         '{: <22}'.format("About Me")], [self.Note1, self.Note2, self.Note3, self.Note4, self.Note5, self.Note6, self.Note7, self.Note8], 0)
        self.menu.rect[0] = 18
        self.menu.rect[1] = 50
        self.add(self.menu)

    def Note1(self):
        self.construct(text_arr="o Fringe \no Shameless \no Fullmetal Alchemist \no "
                                "Cowboy Bebop \no Steins;Gate \no Firefly \no "
                                "Breaking Bad \no Doctor Who \no Arrested Development \no "
                                "Rick And Morty \no Daredevil \no Gotham")

    def Note2(self):
        self.construct(text_arr="o Back To The Future Trilogy \no Clerks \no Bad Santa \no "
                                "Bridge To Terabithia \no The Butterfly Effect \no The Game \no "
                                "Mr. Nobody \no Hot Fuzz \no Big Nothing  \no "
                                "Shaun Of The Dead \no The Terminal \no Filth")

    def Note3(self):
        self.construct(text_arr="o The Martian (Andy Weir) \no The Godfather (Mario Puzo) \no The Master And Margarita (Mikhail Bulgakov) \no "
                                "Los Piratas Del Golfo (Vicente Riva Palacio) \no The End Of Eternity (Isaac Asimov) \no I, Robot (Isaac Asimov) \no "
                                "Drei Kameraden (Erich Maria Remarque)")
    def Note4(self):
        self.construct(text_arr="o To The Moon \no Heavy Rain \no TES 3: Morrowind \no "
                                "Infamous \no The Wolf Among Us \no The Walking Dead \no "
                                "Last Of Us \no Gunpoint \no Faster Than Light \no "
                                "Bad Day LA \no True Crime: Streets Of LA \no Marc Ecko's Getting Up")

    def Note5(self):
        self.construct(text_arr="o Folk Rock \no Electro Swing \no ... \no Actually, i like different genres :-)")

    def Note6(self):
        self.construct(text_arr="o Bacon")

    def Note7(self):
        self.construct(text_arr="o Purple")

    def Note8(self):
        self.construct(text_arr="o I'm lazy")

    def construct(self, IMG='images/Quests/1.bmp', text_arr="Nothing", font=19, chk_shw_loc=True):
        text_arr = self.text_to_array(text_arr)
        self.notes.image = pygame.image.load(IMG)
        self.notes.rect[0] = 210
        self.notes.rect[1] = 50
        if chk_shw_loc:
            text = config.FONTS[18].render("Show Location", True, (21, 61, 34), (0, 0, 0))
            self.notes.image.blit(text, (120, 0))
        coord = 40
        for x in text_arr:
            text = config.FONTS[font].render(x, True, (95, 255, 177), (0, 0, 0))
            self.notes.image.blit(text, (5, coord))
            coord += 18
        self.add(self.notes)

    def text_to_array(self, text):
        text_array = text.split(' ')
        final_text_array = ['']
        k = 0
        for x in text_array:
            if "\n" in x:
                final_text_array.append("")
                k += 1
                final_text_array[k] += x[1:] + " "
            elif len(x) + len(final_text_array[k]) < 29:
                final_text_array[k] += x + " "
            else:
                final_text_array.append(x + " ")
                k += 1
        return final_text_array

    def handle_resume(self):
        self.parent.pypboy.header.headline = "DATA"
        self.parent.pypboy.header.title = "Moscow City"
        super(Module, self).handle_resume()

class Notes(game.Entity):
    def __init__(self):
        super(Notes, self).__init__()
        self.rect = self.image.get_rect()
        self.image = self.image.convert()
