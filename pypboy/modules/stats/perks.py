import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = "Perks"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.perks = Perks()
        self.perks.image = pygame.image.load('images/Perks/1.bmp')
        self.perks.rect[0] = 240
        self.perks.rect[1] = 50
        self.add(self.perks)
        self.menu = pypboy.ui.Menu(210, ['{: <21}'.format("  Mysterious Stranger"),
                                         '{: <21}'.format("  Strong Back"),
                                         '{: <21}'.format("  Bloody Mess"),
                                         '{: <21}'.format("  Educated"),
                                         '{: <21}'.format("  Silent Running"),
                                         '{: <21}'.format("  Swift Learner"),
                                         '{: <21}'.format("  Early Bird"),
                                         '{: <21}'.format("  Wild Wasteland"),
                                         '{: <21}'.format("  Intense Training")], [self.Perk1, self.Perk2, self.Perk3, self.Perk4, self.Perk5, self.Perk6, self.Perk7, self.Perk8, self.Perk9], 0)
        self.menu.rect[0] = 18
        self.menu.rect[1] = 50
        self.add(self.menu)

    def Perk1(self):
        self.construct(IMG='images/Perks/MysteriousStranger.png', text_arr="10% chance that the Stranger will finish off a target in V.A.T.S.", font=15)

    def Perk2(self):
        self.construct(IMG='images/Perks/StrongBack.png', text_arr="+50 Carry Weight.", font=15)

    def Perk3(self):
        self.construct(IMG='images/Perks/Bloody_Mess.png', text_arr="+5% overall damage; more violent death animations.", font=15)

    def Perk4(self):
        self.construct(IMG='images/Perks/Educated.png', text_arr="You gain two more skill points every time you advance in level.", font=15)

    def Perk5(self):
        self.construct(IMG='images/Perks/SilentRunning.png', text_arr="Running no longer factors into a successful sneak attempt.", font=15)

    def Perk6(self):
        self.construct(IMG='images/Perks/SwiftLearner.png', text_arr="You gain an additional 10% whenever experience points are earned.", font=15)

    def Perk7(self):
        self.construct(IMG='images/Perks/Intense_Training.png', text_arr="With the Intense Training perk, a single point can be put into any S.P.E.C.I.A.L. attribute.", font=15)

    def Perk8(self):
        self.construct(IMG='images/Perks/Early_Bird.PNG', text_arr="From 6AM to 12PM, you gain +2 to all SPECIAL stats but from 6PM to 6AM, you suffer -1 to all SPECIAL stats.", font=15)

    def Perk9(self):
        self.construct(IMG='images/Perks/Wild_Wasteland.PNG', text_arr="                                            ???", font=24)

    def construct(self, IMG='images/skills/Speech.png', text_arr="Nothing", font=15):
        text_arr = self.text_to_array(text_arr)
        self.perks.image = pygame.image.load(IMG)
        self.perks.rect[0] = 246
        self.perks.rect[1] = 50
        pygame.draw.line(self.perks.image, (95, 255, 177), (0, 7), (0, 260), 2)
        pygame.draw.line(self.perks.image, (95, 255, 177), (0, 200), (220, 200), 2)
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
