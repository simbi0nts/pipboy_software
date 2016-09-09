import pypboy
import pygame
import game
import config
import pypboy.ui
import pypboy.core
from datetime import datetime


class Module(pypboy.SubModule):
    label = "S.P.E.C.I.A.L."

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.health = Health()
        self.health.image = pygame.image.load('images/special/Strength.png')
        self.health.rect[0] = 240
        self.health.rect[1] = 50
        self.add(self.health)
        self.menu_list()
        self.menu = pypboy.ui.Menu(210, [self.strength, self.perception, self.charisma, self.endurance, self.intelligence, self.agility, self.luck], [self.Strength, self.Perception, self.Endurance, self.Charisma, self.Intelligence, self.Agility, self.Luck], 0)
        self.menu.rect[0] = 18
        self.menu.rect[1] = 70
        self.add(self.menu)

    def Strength(self):
        self.construct(IMG='images/special/Strength.png', text_arr="A measure of your raw physical power. It affects how much you can carry, and determines the effectiveness of all melee attacks ", flag=False)

    def Perception(self):
        self.construct(IMG='images/special/Perception.png', text_arr="How good you are at noticing stuff. A high perception grants a bonus to the Explosives, Lockpick and Energy Weapons skills, and determines when red compass markings appear(which indicate threats).", font=13, length=43)

    def Endurance(self):
        self.construct(IMG='images/special/Charisma.png', text_arr="Endurance is a measure of your overall physical fitness. A high Endurance gives bonuses to health, enviromental resistances and the big guns and unarmed skills. ")

    def Charisma(self):
        self.construct(IMG='images/special/Endurance.png', text_arr="Having a high Charisma will improve people's disposition toward you, and give bonuses to both the Barter and Speech skills")

    def Intelligence(self):
        self.construct(IMG='images/special/Intelligence.png', text_arr="Intelligence affects the Science, Repair and Medicine skills. The higher your Intelligence, the more skill points you'll be able to distribute when you level up")

    def Agility(self):
        self.construct(IMG='images/special/Agility.png', text_arr="Agility affects your Small Guns and Sneak skills, and the number of Action Points available for V.A.T.S ")

    def Luck(self):
        self.construct(IMG='images/special/Luck.png', text_arr="Raising your luck will raise all of your skills a little. It also raises the chances of weapon misfire for opponents, and increases chances at gambling in New Vegas.")

    def menu_list(self):
        if (int(datetime.strftime(datetime.now(), "%H"))>=6 and int(datetime.strftime(datetime.now(), "%H"))<12):
            self.strength = '{: <21}'.format("  Strength") + "6(+2)"
            self.perception = '{: <21}'.format("  Perception") + "9(+2)"
            self.endurance = '{: <21}'.format("  Endurance") + "10(+2)"
            self.charisma = '{: <21}'.format("  Charisma") + "7(+2)"
            self.intelligence = '{: <21}'.format("  Intelligence") + "10(+2)"
            self.agility = '{: <21}'.format("  Agility") + "7(+1)"
            self.luck = '{: <21}'.format("  Luck") + "4(+2)"
        elif (int(datetime.strftime(datetime.now(), "%H"))>=18 or int(datetime.strftime(datetime.now(), "%H"))<6):
            self.strength = '{: <21}'.format("  Strength") + "3(-1)"
            self.perception = '{: <21}'.format("  Perception") + "6(-1)"
            self.endurance = '{: <21}'.format("  Endurance") + "7(-1)"
            self.charisma = '{: <21}'.format("  Charisma") + "4(-1)"
            self.intelligence = '{: <21}'.format("  Intelligence") + "7(-1)"
            self.agility = '{: <21}'.format("  Agility") + "4(-2)"
            self.luck = '{: <21}'.format("  Luck") + "1(-1)"
        else:
            self.strength = '{: <21}'.format("  Strength") + "4    "
            self.perception = '{: <21}'.format("  Perception") + "7    "
            self.endurance = '{: <21}'.format("  Endurance") + "8    "
            self.charisma = '{: <21}'.format("  Charisma") + "5    "
            self.intelligence = '{: <21}'.format("  Intelligence") + "8    "
            self.agility = '{: <21}'.format("  Agility") + "5(-1)"
            self.luck = '{: <21}'.format("  Luck") + "2    "

    def construct(self, IMG='images/special/Strength.png', text_arr="Nothing", font=15, length=38, flag=True):
        text_arr = self.text_to_array(text_arr, length)
        self.health.image = pygame.image.load(IMG)
        self.health.rect[0] = 246
        self.health.rect[1] = 50
        pygame.draw.line(self.health.image, (95, 255, 177), (0, 7), (0, 260), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (0, 200), (220, 200), 2)
        coord = 204
        for x in text_arr:
            text = config.FONTS[font].render(x, True, (95, 255, 177), (0, 0, 0))
            self.health.image.blit(text, (5, coord))
            coord += 14
        self.add(self.health)
        self.menu_list()
        if flag:
            self.menu.items = [self.strength, self.perception, self.charisma, self.endurance, self.intelligence, self.agility, self.luck]

    def text_to_array(self, text, length):
        text_array = text.split(' ')
        final_text_array = ['']
        k = 0
        for x in text_array:
            if "\n" in x:
                final_text_array.append("")
                k += 1
                final_text_array[k] += x[1:] + " "
            elif len(x) + len(final_text_array[k]) < length:
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





