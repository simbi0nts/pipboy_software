import pypboy
import pygame
import game
import config


class Module(pypboy.SubModule):

    label = "Misc"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.icons = Icons()
        self.icons.image = pygame.image.load('images/Misc/misc.png')
        self.icons.rect[0] = 245
        self.icons.rect[1] = 185
        self.add(self.icons)
        self.items = Items()
        self.items.image = pygame.image.load('images/Misc/test.png')
        self.items.rect[0] = 215
        self.items.rect[1] = 50
        self.add(self.items)
        self.menu = pypboy.ui.Menu(200, ['{: <23}'.format("Bottle Caps (18)"),
                                         '{: <23}'.format("Clock"),
                                         '{: <23}'.format("Credit Card"),
                                         '{: <23}'.format("Pre-war Book"),
                                         '{: <23}'.format("Pre-war Money"),
                                         '{: <23}'.format("Ticket"),
                                         '{: <23}'.format("Keys")],
                                   [self.rect1, self.rect2, self.rect3, self.rect4, self.rect5, self.rect6, self.rect7], 0)
        self.menu.rect[0] = 18
        self.menu.rect[1] = 60
        self.add(self.menu)

    def rect1(self):
        self.builder("----", 1, IMG='images/Misc/Icon_nuka_cola_cap.png',)

    def rect2(self):
        self.builder("----", "----", IMG='images/Misc/Icon_compass.png',)

    def rect3(self):
        self.builder("----", "----", IMG='images/Misc/Icon_passcard.png',)

    def rect4(self):
        self.builder(1, 1, IMG='images/Misc/Icon_skill_books.png',)

    def rect5(self):
        self.builder("----", 10, IMG='images/Misc/Icon_NCR_money_5.png',)

    def rect6(self):
        self.builder("----", 1, IMG='images/Misc/Icon_lottery_ticket.png',)

    def rect7(self):
        self.builder("----", "----", IMG='images/Misc/Keyring_icon.png',)

    def builder(self, WG, VAL, DAM_DT=None, DAM_DT_VAL=None, CND=None, Descript=None, Descript2=None, Effects=None, STR=None, MOD=None, REPAIR=None, MAINTAIN=None, IMG='images/Misc/test.png', ICON=None, ICON_DESCR=None):
        self.items.image = pygame.image.load(IMG)
        coords = [25, 185]
        if WG != None:
            pygame.draw.line(self.items.image, (95, 255, 177), (100, 160), (170, 160), 2)
            pygame.draw.line(self.items.image, (95, 255, 177), (170, 160), (170, 175), 2)
            text = config.FONTS[16].render("WG"+'{: >7}'.format(WG), True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (105, 165))
        if VAL != None:
            pygame.draw.line(self.items.image, (95, 255, 177), (175, 160), (245, 160), 2)
            pygame.draw.line(self.items.image, (95, 255, 177), (245, 160), (245, 175), 2)
            text = config.FONTS[16].render("VAL"+'{: >7}'.format(VAL), True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (175, 165))
        if DAM_DT != None:
            if DAM_DT_VAL == None:
                DAM_DT_VAL = "----"
            pygame.draw.line(self.items.image, (95, 255, 177), (25, 160), (95, 160), 2)
            pygame.draw.line(self.items.image, (95, 255, 177), (95, 160), (95, 175), 2)
            text = config.FONTS[16].render(DAM_DT+'{: >7}'.format(DAM_DT_VAL), True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (30, 165))
        if CND != None:
            pygame.draw.line(self.items.image, (95, 255, 177), (25, 185), (95, 185), 2)
            pygame.draw.line(self.items.image, (95, 255, 177), (95, 185), (95, 200), 2)
            text = config.FONTS[16].render("CND", True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (30, 190))
            self.colba(CND)
            coords = [100, 185]
        if Descript == None and Descript2 != None:
            Descript = Descript2
            Descript2 = None
        if Descript != None:
            pygame.draw.line(self.items.image, (95, 255, 177), (coords[0], coords[1]), (int(coords[0]+(245-coords[0])), coords[1]), 2)
            pygame.draw.line(self.items.image, (95, 255, 177), ((int(coords[0]+(245-coords[0]))), coords[1]), (int(coords[0]+(245-coords[0])), int(coords[1]+15)), 2)
            text = config.FONTS[16].render(Descript, True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (int(coords[0]+5), int(coords[1]+5)))
            coords[1] = 210
        if Descript2 != None:
            pygame.draw.line(self.items.image, (95, 255, 177), ((int(coords[0]+(245-coords[0]))), int(coords[1]-10)), (int(coords[0]+(245-coords[0])), int(coords[1]+5)), 2)
            text = config.FONTS[16].render(Descript2, True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (int(coords[0]+5), int(coords[1]-5)))
            coords[1] = 225
        if Effects != None:
            pygame.draw.line(self.items.image, (95, 255, 177), (25, coords[1]), (int(coords[0]+(245-coords[0])), coords[1]), 2)
            pygame.draw.line(self.items.image, (95, 255, 177), ((int(coords[0]+(245-coords[0]))), coords[1]), (int(coords[0]+(245-coords[0])), int(coords[1]+15)), 2)
            text = config.FONTS[16].render("EFFECTS"+'{: >28}'.format(Effects), True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (25, int(coords[1]+5)))
            coords[1] = 225
        if STR != None:
            pygame.draw.line(self.items.image, (95, 255, 177), (175, 135), (245, 135), 2)
            pygame.draw.line(self.items.image, (95, 255, 177), (245, 135), (245, 150), 2)
            text = config.FONTS[16].render("STR"+'{: >7}'.format(STR), True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (175, 140))
        if  MOD != None:
            text = config.FONTS[18].render(("       Mod"), True, (21, 61, 34), (0, 0, 0))
            self.items.image.blit(text, (175, 25))
        if REPAIR != None:
            text = config.FONTS[18].render(("    Repair"), True, (21, 61, 34), (0, 0, 0))
            self.items.image.blit(text, (175, 5))
        if MAINTAIN != None:
            text = config.FONTS[18].render(("  Maintain"), True, (21, 61, 34), (0, 0, 0))
            self.items.image.blit(text, (175, 5))
        if ICON_DESCR != None:
            text = config.FONTS[18].render((ICON_DESCR), True, (95, 255, 177), (0, 0, 0))
            self.items.image.blit(text, (50, 135))
            if ICON != None:
                self.icons.image = pygame.image.load("images/Misc/misc.png")
            else:
                self.icons.image = pygame.image.load("images/Misc/misc.png")

    def colba(self, num):
        pygame.draw.line(self.items.image, (95, 255, 177), (55, 192), (85, 192), 2)
        pygame.draw.line(self.items.image, (95, 255, 177), (55, 202), (85, 202), 2)
        pygame.draw.line(self.items.image, (95, 255, 177), (55, 192), (55, 202), 2)
        pygame.draw.line(self.items.image, (95, 255, 177), (85, 192), (85, 202), 2)
        coor = 55
        try:
            for x in range(int(num)):
                pygame.draw.line(self.items.image, (95, 255, 177), (coor, 192), (coor, 202), 2)
                coor += 2
        except:
            pass

    def handle_resume(self):
        self.parent.pypboy.header.headline = "ITEMS"
        self.parent.pypboy.header.title = " WG 23/135  |  CAPS 18"
        super(Module, self).handle_resume()

class Items(game.Entity):
    def __init__(self):
        super(Items, self).__init__()
        text = config.FONTS[16].render("Hello", True, (95, 255, 177), (0, 0, 0))
        self.image.blit(text, (10, 225))
        self.rect = self.image.get_rect()
        self.image = self.image.convert()

class Icons(game.Entity):
    def __init__(self):
        super(Icons, self).__init__()
        text = config.FONTS[16].render("Hello", True, (95, 255, 177), (0, 0, 0))
        self.image.blit(text, (10, 225))
        self.rect = self.image.get_rect()
        self.image = self.image.convert()
