import pypboy
import pygame
import game
import config
import pypboy.ui
from datetime import  datetime

class Module(pypboy.SubModule):

    label = "Status"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.health = Health()
        self.add(self.health)
        self.menu = pypboy.ui.Menu(100, ["CND", "RAD", "EFF", "H2O", "FOD", "SLP"], [self.show_cnd, self.show_rad, self.show_eff, self.show_h20, self.show_fod, self.show_slp], 0)
        self.menu.rect[0] = 20
        self.menu.rect[1] = 60
        self.add(self.menu)

    def handle_resume(self):
        self.parent.pypboy.header.headline = "STATUS"
        self.parent.pypboy.header.title = " HP 160/175  |  AP 62/62"
        super(Module, self).handle_resume()

    def show_cnd(self):
        self.health.image =  pygame.image.load('images/status/pypboy.png')
        self.health.rect[0] = 4
        self.health.rect[1] = 40
        text = config.FONTS[18].render(("(0)Stimpak"), True, (21, 61, 34), (0, 0, 0))
        self.health.image.blit(text, (370, 18))
        text = config.FONTS[18].render(("     Limbs"), True, (21, 61, 34), (0, 0, 0))
        self.health.image.blit(text, (370, 43))
        text = config.FONTS[18].render("Max - Level 20", True, (105, 251, 187), (0, 0, 0))
        text_width = text.get_size()[0]
        self.health.image.blit(text, (config.WIDTH / 2 - 8 - text_width / 2, 250))

    def show_rad(self):
        self.health.image =  pygame.image.load('images/status/EFF.jpg')
        self.health.rect[0] = 10
        self.health.rect[1] = 30
        self.graph(202, 220)
        text = config.FONTS[18].render(("RAD"), True, (105, 251, 187), (0, 0, 0))
        self.health.image.blit(text, (130, 230))
        text = config.FONTS[18].render("RAD RESIST  4%", True, (105, 251, 187), (0, 0, 0))
        self.health.image.blit(text, (10, 230))
        text = config.FONTS[18].render(("RadAway"), True, (21, 61, 34), (0, 0, 0))
        self.health.image.blit(text, (390, 30))
        text = config.FONTS[18].render(("Rad-X"), True, (21, 61, 34), (0, 0, 0))
        self.health.image.blit(text, (404, 55))

    def show_eff(self):
        self.health.image =  pygame.image.load('images/status/EFF.jpg')
        self.health.rect[0] = 50
        self.health.rect[1] = 140
        pygame.draw.line(self.health.image, (95, 255, 177), (40, 33), (400, 33), 2)
        if (int(datetime.strftime(datetime.now(), "%H"))>=6 and int(datetime.strftime(datetime.now(), "%H"))<12):
            text = config.FONTS[18].render("{:<20}".format("Early Bird Penalty") +  "{:<33}".format("STR +2, PER +2, LCK +2, INT +2"), True, (105, 251, 187), (0, 0, 0))
        elif (int(datetime.strftime(datetime.now(), "%H"))>=18 or int(datetime.strftime(datetime.now(), "%H"))<6):
            text = config.FONTS[18].render("{:<20}".format("Early Bird Penalty") +  "{:<33}".format("STR -1, PER -1, LCK -1, INT -1"), True, (105, 251, 187), (0, 0, 0))
        else:
            text = config.FONTS[18].render("{:<20}".format("Early Bird Penalty") +  "{:<33}".format("None"), True, (105, 251, 187), (0, 0, 0))
        text_width = text.get_size()[0]
        self.health.image.blit(text, (config.WIDTH / 2 - 8 - text_width / 2, 10))
        text = config.FONTS[18].render("{:<20}".format("Shabby Clothes") + "{:<33}".format("AGL -1"), True, (105, 251, 187), (0, 0, 0))
        text_width = text.get_size()[0]
        self.health.image.blit(text, (config.WIDTH / 2 - 8 - text_width / 2, 40))

    def show_h20(self):
        self.health.image =  pygame.image.load('images/status/EFF.jpg')
        self.health.rect[0] = 10
        self.health.rect[1] = 30
        self.graph(240, 220)
        text = config.FONTS[18].render(("H2O"), True, (105, 251, 187), (0, 0, 0))
        self.health.image.blit(text, (130, 230))

    def show_fod(self):
        self.health.image =  pygame.image.load('images/status/EFF.jpg')
        self.health.rect[0] = 10
        self.health.rect[1] = 30
        self.graph(218, 220)
        text = config.FONTS[18].render(("FOD"), True, (105, 251, 187), (0, 0, 0))
        self.health.image.blit(text, (130, 230))

    def show_slp(self):
        self.health.image =  pygame.image.load('images/status/EFF.jpg')
        self.health.rect[0] = 10
        self.health.rect[1] = 30
        self.graph(243, 220)
        text = config.FONTS[18].render(("SLP"), True, (105, 251, 187), (0, 0, 0))
        self.health.image.blit(text, (130, 230))

    def graph(self, _x, _y):
        pygame.draw.line(self.health.image, (95, 255, 177), (0, _y), (120, _y), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (120, _y), (120, _y+30), 2)

        pygame.draw.line(self.health.image, (95, 255, 177), (130, _y), (459, _y), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (459, _y), (459, _y+30), 2)

        pygame.draw.line(self.health.image, (95, 255, 177), (440, _y), (440, _y+10), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (440, _y+10), (450, _y), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (443, _y), (440, _y+3), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (445, _y), (440, _y+5), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (446, _y), (440, _y+6), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (448, _y), (440, _y+8), 2)

        pygame.draw.line(self.health.image, (95, 255, 177), (200, _y), (200, _y+10), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (200, _y+10), (190, _y), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (197, _y), (200, _y+3), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (195, _y), (200, _y+5), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (194, _y), (200, _y+6), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (192, _y), (200, _y+8), 2)

        t = 216
        for x in range(14):
            if (x+1) % 3 == 0:
                pygame.draw.line(self.health.image, (95, 255, 177), (t, _y), (t, _y+10), 2)
            else:
                pygame.draw.line(self.health.image, (95, 255, 177), (t, _y), (t, _y+5), 2)
            t += 16

        text = config.FONTS[18].render(("{:<15}".format("500") + '1000'), True, (105, 251, 187), (0, 0, 0))
        self.health.image.blit(text, (310, _y-20))

        pygame.draw.line(self.health.image, (95, 255, 177), (_x, _y+25), (_x, _y+55), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (_x-5, _y+30), (_x+5, _y+30), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (_x-5, _y+30), (_x, _y+25), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (_x, _y+25), (_x+5, _y+30), 2)
        pygame.draw.line(self.health.image, (95, 255, 177), (_x-3, _y+28), (_x+3, _y+28), 2)

        text = config.FONTS[18].render(str((_x-200)*4), True, (105, 251, 187), (0, 0, 0))
        self.health.image.blit(text, ((_x-30), _y+30))

class Health(game.Entity):
    def __init__(self):
        super(Health, self).__init__()
        self.rect = self.image.get_rect()
        self.image = self.image.convert()



