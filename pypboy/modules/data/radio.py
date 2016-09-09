import pypboy
import pygame
import config
import game
import random


from pypboy.modules.data import entities

class Module(pypboy.SubModule):

    label = "Radio"

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        self.array = []
        self.draw_diagram()
        self.stations = [
            entities.NewVegasRadio(),
            entities.GalaxyNewsRadio(),
            entities.MojaveMusicRadio(),
            entities.RadioLostSouls(),
            entities.RadioDustEars(),
            entities.RadioSilentWasteland(),
            entities.MotivatingSongsRadio(),
            entities.StopRadio()
        ]
        for station in self.stations:
            self.add(station)
        self.active_station = None
        config.radio = self
        self.items = Items()
        self.items.image = pygame.image.load('images/1.bmp')
        self.items.rect[0] = 215
        self.items.rect[1] = 50
        self.add(self.items)
        self.menu = pypboy.ui.Menu(200, ['{: <22}'.format("New Vegas Radio"),
                                         '{: <22}'.format("Galaxy News Radio"),
                                         '{: <22}'.format("Mojave Music Radio"),
                                         '{: <22}'.format("Radio Lost Souls"),
                                         '{: <22}'.format("Radio Dusty Ears"),
                                         '{: <22}'.format("Radio Silent Wasteland"),
                                         '{: <22}'.format("Motivating Songs Radio"),
                                         '{: <22}'.format("Stop Radio")], [self.r1, self.r2, self.r3, self.r4, self.r5, self.r6, self.r7, self.stop], 0)
        self.menu.rect[0] = 20
        self.menu.rect[1] = 60
        self.add(self.menu)

    def r1(self):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[0]
        self.active_station.play_random()
        self.draw_diagram()
        self.draw_line()

    def r2(self):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[1]
        self.active_station.play_random()
        self.draw_diagram()
        self.draw_line()

    def r3(self):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[2]
        self.active_station.play_random()
        self.draw_diagram()
        self.draw_line()

    def r4(self):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[3]
        self.active_station.play_random()
        self.draw_diagram()
        self.draw_line()

    def r5(self):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[4]
        self.active_station.play_random()
        self.draw_diagram()
        self.draw_line()

    def r6(self):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[5]
        self.active_station.play_random()
        self.draw_diagram()
        self.draw_line()

    def r7(self):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[6]
        self.active_station.play_random()
        self.draw_diagram()
        self.draw_line()

    def stop(self):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[7]
        self.active_station.play_random()
        self.stop_diagram()
        self.draw_line()

    def select_station(self, station):
        if hasattr(self, 'active_station') and self.active_station:
            self.active_station.stop()
        self.active_station = self.stations[station]
        self.active_station.play_random()

    def handle_event(self, event):
        if event.type == config.EVENTS['SONG_END']:
            if hasattr(self, 'active_station') and self.active_station:
                self.active_station.play_random()
        if event.type == config.EVENTS['RAD_ANIM'] and self.active_station != self.stations[7]:
            self.draw_line()

    def draw_line(self):
        self.items.image = pygame.image.load('images/1.bmp')
        self.draw_border()
        start_cord = 10
        for x in range(36):
            rand1 = self.array[x]
            rand2 = self.array[x+1]
            pygame.draw.line(self.items.image, (95, 255, 177), (start_cord, rand1), (start_cord+5, rand2), 2)
            start_cord += 6
            self.array[x] = self.array[x+1]
        rand = random.randint(40, 160)
        while 1:
            if rand >= self.array[35]+40 or rand <= self.array[35]-40:
                rand = random.randint(40, 160)
            else:
                self.array[36] = rand
                break

    def draw_border(self):
        pygame.draw.line(self.items.image, (95, 255, 177), (0, 218), (245, 218), 2)
        pygame.draw.line(self.items.image, (95, 255, 177), (247, 30), (247, 215), 2)
        coord_x = 0
        coord_y = 30
        for x in range(50):
            if (x-2) % 6 == 0:
                pygame.draw.line(self.items.image, (95, 255, 177), (coord_x, 218), (coord_x, 203), 2)
            else:
                pygame.draw.line(self.items.image, (95, 255, 177), (coord_x, 218), (coord_x, 213), 2)
            coord_x += 5
        for x in range(37):
            if (x+1) % 6 == 0:
                pygame.draw.line(self.items.image, (95, 255, 177), (247, coord_y), (232, coord_y), 2)
            else:
                pygame.draw.line(self.items.image, (95, 255, 177), (247, coord_y), (242, coord_y), 2)
            coord_y += 5

    def draw_diagram(self):
        self.array = []
        self.array.append(random.randint(40, 160))
        for x in range(36):
            rand = random.randint(40, 160)
            while 1:
                if rand > self.array[x]+40 or rand < self.array[x]-40:
                    rand = random.randint(40, 160)
                else:
                    self.array.append(rand)
                    break

    def stop_diagram(self):
        self.array = []
        for x in range(37):
            self.array.append(120)

    def handle_resume(self):
        self.parent.pypboy.header.headline = "DATA"
        self.parent.pypboy.header.title = "Moscow City"
        super(Module, self).handle_resume()

class Items(game.Entity):
    def __init__(self):
        super(Items, self).__init__()
        self.rect = self.image.get_rect()
        self.image = self.image.convert()
