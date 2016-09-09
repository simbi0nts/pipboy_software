import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = "General"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.perks = Perks()
        self.perks.image = pygame.image.load('images/Karma.png')
        self.perks.rect[0] = 240
        self.perks.rect[1] = 50
        self.add(self.perks)
        self.menu = pypboy.ui.Menu(270, ['{: <27}'.format("Quests Completed             1982"),
                                         '{: <27}'.format("Computers Hacked               34"),
                                         '{: <27}'.format("Speech Successes               11"),
                                         '{: <27}'.format("Books Read                     48"),
                                         '{: <27}'.format("Times Slept                 52631"),
                                         '{: <27}'.format("Challenges Completed          511"),
                                         '{: <27}'.format("Speech Failures             12286"),
                                         '{: <27}'.format("Stimpaks Taken                 93"),
                                         '{: <27}'.format("Times fall in love              3"),
                                         '{: <27}'.format("Items stolen                   60"),
                                         '{: <27}'.format("Weapons Created                 0")], [self.General1, self.General2, self.General3, self.General4, self.General5,
                                                                         self.General6, self.General7, self.General8, self.General9, self.General10,
                                                                         self.General11], 0)
        self.menu.rect[0] = 18
        self.menu.rect[1] = 50
        self.add(self.menu)

    def General1(self):
        self.construct()

    def General2(self):
        self.construct()

    def General3(self):
        self.construct()

    def General4(self):
        self.construct()

    def General5(self):
        self.construct()

    def General6(self):
        self.construct()

    def General7(self):
        self.construct()

    def General8(self):
        self.construct()

    def General9(self):
        self.construct()

    def General10(self):
        self.construct()

    def General11(self):
        self.construct()

    def construct(self, IMG='images/Karma.png', text_arr="", font=15):
        text_arr = self.text_to_array(text_arr)
        self.perks.image = pygame.image.load(IMG)
        text = config.FONTS[24].render(("Wanderer"), True, (105, 251, 187), (0, 0, 0))
        self.perks.image.blit(text, (95, 230))
        self.perks.rect[0] = 246
        self.perks.rect[1] = 50
        coord = 204
        for x in text_arr:
            text = config.FONTS[font].render(x, True, (95, 255, 177), (0, 0, 0))
            self.perks.image.blit(text, (5, coord))
            coord += 14
        self.add(self.perks)

    def text_to_array(self, text):
        text_array = text.split(' ')
        final_text_array = ['']
        k = 0
        for x in text_array:
            if "\n" in x:
                final_text_array.append("")
                k += 1
                final_text_array[k] += x[1:] + " "
            elif len(x) + len(final_text_array[k]) < 35:
                final_text_array[k] += x + " "
            else:
                final_text_array.append(x + " ")
                k += 1
        return final_text_array

    def handle_resume(self):
        self.parent.pypboy.header.headline = "STATUS"
        self.parent.pypboy.header.title = " HP 160/175  |  AP 62/62"
        super(Module, self).handle_resume()

class Perks(game.Entity):
    def __init__(self):
        super(Perks, self).__init__()
        self.rect = self.image.get_rect()
        self.image = self.image.convert()
