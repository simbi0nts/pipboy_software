import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = "Skills"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.health = Health()
        self.health.image = pygame.image.load('images/skills/Barter.png')
        self.health.rect[0] = 240
        self.health.rect[1] = 50
        self.add(self.health)
        self.menu = pypboy.ui.Menu(210, ['{: <21}'.format("  Barter") + "27",
                                         '{: <21}'.format("  Guns") + "24",
                                         '{: <21}'.format("  Lockpick") + "98",
                                         '{: <21}'.format("  Programming") + "31",
                                         '{: <21}'.format("  Medicine") + "32",
                                         '{: <21}'.format("  Repair") + "56",
                                         '{: <21}'.format("  Science") + "86",
                                         '{: <21}'.format("  Sneak") + "84",
                                         '{: <21}'.format("  Speech") + "23",
                                         '{: <21}'.format("  Survival") + "37",
                                         '{: <21}'.format("  Unarmed") + "37"], [self.Barter, self.Guns, self.Lockpick, self.Programming, self.Medicine, self.Repair, self.Science, self.Sneak, self.Speech, self.Survival, self.Unarmed], 0)
        self.menu.rect[0] = 18
        self.menu.rect[1] = 50
        self.add(self.menu)

    def Barter(self):
        self.construct(IMG='images/skills/Barter.png', text_arr="The Barter skill affects the prices you get for buying and selling items. In general, the higher your Barter skill, the lower your prices on purchased items. ")

    def Guns(self):
        self.construct(IMG='images/skills/Guns.png', text_arr="Guns determines your effectiveness with any weapon that uses conventional ammunition (.22 LR, .357 Magnum, 5mm, 10mm, 5.56mm, .308, .45-70 Gov't, etc.).")

    def Lockpick(self):
        self.construct(IMG='images/skills/Lockpick.png', text_arr="The Lockpick skill is used to open locked doors and containers")

    def Programming(self):
        self.construct(IMG='images/skills/programming.png', text_arr=" _      ___       __ \n| | | |  |  |  | |  | |  | \n|_| |_|  |  |__| |  | |\ | \n|    |   |  |  | |  | | \| \n|    |   |  |  | |__| |  |", not_reverse=False)

    def Medicine(self):
        self.construct(IMG='images/skills/medicine.png', text_arr="The Medicine skill determines how many Hit Points you'll replenish upon using a Stimpak, and the effectiveness of Rad-X and RadAway.")

    def Repair(self):
        self.construct(IMG='images/skills/repair.png', text_arr="The Repair skill allows you to maintain any weapons and apparel. In additional, Repair allows you to create items and Guns ammunition at reloading benches.")

    def Science(self):
        self.construct(IMG='images/skills/science.png', text_arr="The Science skill represents your combined scientific knowledge, and is primarily used to hack restricted computer terminals.")

    def Sneak(self):
        self.construct(IMG='images/skills/sneak.png', text_arr="The higher your Sneak skill, the easier it is to remain undetected, steal an item, or pick someone's pocket. ")

    def Speech(self):
        self.construct(IMG='images/skills/Speech.png', text_arr="The Speech skill governs how much you can influence someone through dialogue, and gain access to information they might otherwise not want to share.")

    def Survival(self):
        self.construct(IMG='images/skills/Survival.png', text_arr="The Survival skill increases the hit points you receive from food and drink. It also helps you create consumable items at campfires. ")

    def Unarmed(self):
        self.construct(IMG='images/skills/unarmed.png', text_arr="The Unarmed skill is used for fighting without a weapon, or with the few weapons specifically designer for hand-to-hand combat, like Brass Knuckles and Power Fist. ")

    def construct(self, IMG='images/special/agility.png', text_arr="Nothing", font=15, incr=14, not_reverse=True):
        text_arr = self.text_to_array(text_arr)
        self.health.image = pygame.image.load(IMG)
        self.health.rect[0] = 246
        self.health.rect[1] = 50
        pygame.draw.line(self.health.image, (95, 255, 177), (0, 7), (0, 260), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (0, 200), (220, 200), 2)
        if not_reverse:
            coord = 204
            for x in text_arr:
                text = config.FONTS[font].render(x, True, (95, 255, 177), (0, 0, 0))
                self.health.image.blit(text, (5, coord))
                coord += incr
        else:
            coord = 258
            for x in reversed(text_arr):
                text = config.FONTS[font].render(x, True, (95, 255, 177), (0, 0, 0))
                self.health.image.blit(text, (35, coord))
                coord -= incr
        self.add(self.health)

    def text_to_array(self, text):
        text_array = text.split(' ')
        final_text_array = ['']
        k = 0
        for x in text_array:
            if "\n" in x:
                final_text_array.append("")
                k += 1
                final_text_array[k] += x[1:] + " "
            elif len(x) + len(final_text_array[k]) < 36:
                final_text_array[k] += x + " "
            else:
                final_text_array.append(x + " ")
                k += 1
        return final_text_array

    def handle_resume(self):
        self.parent.pypboy.header.headline = "STATUS"
        self.parent.pypboy.header.title = " HP 160/175  |  AP 62/62"
        super(Module, self).handle_resume()

class Health(game.Entity):
    def __init__(self):
        super(Health, self).__init__()
        self.rect = self.image.get_rect()
        self.image = self.image.convert()
