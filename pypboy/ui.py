import game
import config
import pygame
import datetime
import os,time

if config.GPIO_AVAILABLE:
    import RPi.GPIO as GPIO

class Header(game.Entity):

    def __init__(self, headline="", title=""):
        self.headline = headline
        self.title = title
        super(Header, self).__init__((config.WIDTH, config.HEIGHT))
        self.rect[0] = 4
        self._date = None
        self.radio_speed = 0
        self.radio_animation_event = pygame.event.Event(config.EVENTS["RAD_ANIM"])

    def update(self, *args, **kwargs):
        super(Header, self).update(*args, **kwargs)

    def render(self, *args, **kwargs):
        new_date = datetime.datetime.now().strftime("%d.%m.%y.%H:%M:%S")
        if new_date != self._date:
            self.image.fill((0, 0, 0))
            pygame.draw.line(self.image, (95, 255, 177), (5, 15), (5, 35), 2)
            pygame.draw.line(self.image, (95, 255, 177), (5, 15), (config.WIDTH - 154, 15), 2)
            pygame.draw.line(self.image, (95, 255, 177), (config.WIDTH - 154, 15), (config.WIDTH - 154, 35), 2)
            pygame.draw.line(self.image, (95, 255, 177), (config.WIDTH - 148, 15), (config.WIDTH - 13, 15), 2)
            pygame.draw.line(self.image, (95, 255, 177), (config.WIDTH - 13, 15), (config.WIDTH - 13, 35), 2)

            text = config.FONTS[18].render("  %s  " % self.headline, True, (105, 251, 187), (0, 0, 0))
            self.image.blit(text, (26, 8))
            render = config.FONTS[18].render(self.title, True, (95, 255, 177), (0, 0, 0))
            text = render
            self.image.blit(text, ((config.WIDTH - 154) - text.get_width() - 10, 19))
            text = config.FONTS[18].render(self._date, True, (95, 255, 177), (0, 0, 0))
            self.image.blit(text, ((config.WIDTH - 141), 19))
            self._date = new_date

        if self.radio_speed == 0:
            pygame.event.post(self.radio_animation_event)
            self.radio_speed = 0
        else:
            self.radio_speed += 1

        super(Header, self).update(*args, **kwargs)

    #def handle_event(self, event):
    #    print(event)

class Footer(game.Entity):

    def __init__(self):
        self.menu = []
        super(Footer, self).__init__((config.WIDTH, config.HEIGHT))
        self.rect[0] = 4
        self.rect[1] = config.HEIGHT - 40

    def update(self, *args, **kwargs):
        super(Footer, self).update(*args, **kwargs)

    def select(self, module):
        #self.dirty = 1
        self.selected = module
        self.image.fill((0, 0, 0))
        pygame.draw.line(self.image, (95, 255, 177), (5, 2), (5, 20), 2)
        pygame.draw.line(self.image, (95, 255, 177), (5, 20), (config.WIDTH - 13, 20), 2)
        pygame.draw.line(self.image, (95, 255, 177), (config.WIDTH - 13, 2), (config.WIDTH - 13, 20), 2)

        offset = 20
        for m in self.menu:
            padding = 1
            text_width = 0
            while text_width < 54:
                spaces = " ".join([" " for x in range(padding)])
                text = config.FONTS[18].render("%s%s%s" % (spaces, m, spaces), True, (105, 255, 187), (0, 0, 0))
                text_width = text.get_size()[0]
                padding += 1
            #print(m+" : "+str(text.get_size()))
            if m == self.selected:
                pygame.draw.rect(self.image, (95, 255, 177), (offset - 2, 6, (text_width + 3), 26), 2)
            self.image.blit(text, (offset, 12))

            offset = offset + 120 + (text_width - 100)


class Menu(game.Entity):

    def __init__(self, width, items=[], callbacks=[], selected=0):
        super(Menu, self).__init__((width, config.HEIGHT - 80))
        self.items = items
        self.callbacks = callbacks
        self.selected = 0
        self.select(selected)
        self.timestamp = 0
        self.filename = '/home/bananapi/Desktop/pypboy/encoder_data.log'

        if config.SOUND_ENABLED:
            self.dial_move_sfx = pygame.mixer.Sound('sounds/dial_move.ogg')

    def select(self, item):
        self.selected = item
        self.redraw()
        if len(self.callbacks) > item and self.callbacks[item]:
            self.callbacks[item]()

    def handle_action(self, action):
	if action == "dial_up":
           if self.selected < len(self.items) - 1:
                if config.SOUND_ENABLED:
                    self.dial_move_sfx.play()
                self.select(self.selected + 1)
	if action == "dial_down":
            if self.selected > 0:
                if config.SOUND_ENABLED:
                    self.dial_move_sfx.play()
                self.select(self.selected - 1)
#	if os.path.exists(self.filename):
#	    print 1
#	    flag = os.path.getmtime(self.filename)
#            if self.timestamp != flag:
#                f = open(self.filename, 'r')
#                temp = f.read()
#                if temp == '1':
#                    if self.selected < len(self.items) - 1:
#                	if config.SOUND_ENABLED:
#                    	    self.dial_move_sfx.play()
#                	self.select(self.selected + 1)
#                if temp  == '0':
#                    if self.selected > 0:
#                	if config.SOUND_ENABLED:
#                    	    self.dial_move_sfx.play()
#                	self.select(self.selected - 1)
#                if temp == '2':
#                    print 'button'
#                f.close()


    def redraw(self):
        self.image.fill((0, 0, 0))
        offset = 5
        for i in range(len(self.items)):
            text = config.FONTS[18].render(" %s " % self.items[i], True, (105, 255, 187), (0, 0, 0))
            if i == self.selected:
                selected_rect = (5, offset - 2, text.get_size()[0] + 6, text.get_size()[1] + 3)
                pygame.draw.rect(self.image, (95, 255, 177), selected_rect, 2)
            self.image.blit(text, (10, offset))
            offset += text.get_size()[1] + 6


class Scanlines(game.Entity):

    def __init__(self, width, height, gap, speed, colours, full_push=False):
        super(Scanlines, self).__init__((width, height))
        self.width = width
        self.height = height
        self.move = gap * len(colours)
        self.gap = gap
        self.colours = colours
        self.rect[1] = 0
        self.top = 0.0
        self.speed = speed
        self.full_push =full_push
        colour = 0
        area = pygame.Rect(0, self.rect[1] * self.speed, self.width, self.gap)
        while area.top <= self.height - self.gap:
            self.image.fill(self.colours[colour], area)
            area.move_ip(0, (self.gap))
            colour += 1
            if colour >= len(self.colours):
                colour = 0

    def render(self, interval, *args, **kwargs):
        self.top += self.speed * interval
        self.rect[1] = self.top
        self.dirty = 1
        if self.full_push:
            if self.top >= self.height:
                self.top = 0
        else:
            if (self.top * self.speed) >= self.move:
                self.top = 0
        super(Scanlines, self).render(self, *args, **kwargs)


class Overlay(game.Entity):
    def __init__(self):
        self.image = pygame.image.load('images/overlay.png')
        super(Overlay, self).__init__((config.WIDTH, config.HEIGHT))
        self.blit_alpha(self, self.image, (0, 0), 128)

    def blit_alpha(self, target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        target.blit(temp, location)


class Border(game.Entity):
    def __init__(self):
        super(Border, self).__init__()
        self.image = pygame.image.load('images/border.png')
        self.rect = self.image.get_rect()


