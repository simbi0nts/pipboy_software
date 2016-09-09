import pypboy
import pygame
import config
import game
import random

from pypboy.modules.data import entities

class Module(pypboy.SubModule):

    label = "Quests"
    
    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.quests = Quests()
        self.quests.image = pygame.image.load('images/Quests/1.bmp')
        self.quests.rect[0] = 240
        self.quests.rect[1] = 50
        self.add(self.quests)
        self.menu = pypboy.ui.Menu(210, ['{: <26}'.format("  Main Quest"),
                                         '{: <26}'.format("  Monday"),
                                         '{: <26}'.format("  For Better Life!"),
                                         '{: <26}'.format("  Just Do it!"),
                                         '{: <26}'.format("  Batman Challenge Workout"),
                                         '{: <26}'.format("  Something you forget")], [self.Quest1, self.Quest2, self.Quest3, self.Quest4, self.Quest5, self.Quest6], 0)
        self.menu.rect[0] = 18
        self.menu.rect[1] = 50
        self.add(self.menu)

    def Quest1(self):
        self.construct(text_arr="[x] Complete School \n \n[x] Complete University \n \n[x] Find The Job \n \n[ ] Get Married \n \n[ ] Make Babies \n \n[ ] Rest In Peace")
        #self.construct(text_arr=["o First of all", "You Are Douche", "test", "", "o Thanks"]) # 30 symbols per row

    def Quest2(self):
        self.construct(text_arr="[x] Pick Up Paycheck \n \n[ ] Cash Paycheck \n \n[ ] Get Milk")

    def Quest3(self):
        self.construct(text_arr="[x] Complete Bachelor \n \n[ ] Complete IELTS Or TOEFL \n \n[ ] Earn 20k$ \n \n[ ] Migrate To Canada")

    def Quest4(self):
        self.construct(text_arr="[x] Finish Pipboy \n \n[ ] Finish 'On The Road' \n \n[ ] Start Playing Guitar. Again \n \n[ ] Find New Apartment \n \n[ ] Start Programming. Again \n \n[ ] Buy Watchman Comic Book")

    def Quest5(self):
        self.construct(text_arr="[ ] 400 Squats \n \n[ ] 250 Push-ups \n \n[ ] 200 Sit-ups")

    def Quest6(self):
        self.construct(text_arr="[?] Turn Gas Off \n \n[?] Feed The Cat \n \n[?] Close The Door")

    def construct(self, IMG='images/Quests/1.bmp', text_arr="Nothing", font=18, chk_shw_loc=True):
        text_arr = self.text_to_array(text_arr)
        self.quests.image = pygame.image.load(IMG)
        self.quests.rect[0] = 246
        self.quests.rect[1] = 50
        if chk_shw_loc:
            text = config.FONTS[18].render("Show Location", True, (21, 61, 34), (0, 0, 0))
            self.quests.image.blit(text, (120, 0))
        coord = 40
        for x in text_arr:
            text = config.FONTS[font].render(x, True, (95, 255, 177), (0, 0, 0))
            self.quests.image.blit(text, (5, coord))
            coord += 18
        self.add(self.quests)

    def text_to_array(self, text):
        text_array = text.split(' ')
        final_text_array = ['']
        k = 0
        for x in text_array:
            if "\n" in x:
                final_text_array.append("")
                k += 1
                final_text_array[k] += x[1:] + " "
            elif len(x) + len(final_text_array[k]) < 30:
                final_text_array[k] += x + " "
            else:
                final_text_array.append(x + " ")
                k += 1
        return final_text_array

    def handle_resume(self):
        self.parent.pypboy.header.headline = "DATA"
        self.parent.pypboy.header.title = "Moscow City"
        super(Module, self).handle_resume()

class Quests(game.Entity):
    def __init__(self):
        super(Quests, self).__init__()
        self.rect = self.image.get_rect()
        self.image = self.image.convert()
