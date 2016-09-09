# -*- coding: utf-8 -*-

import pygame
import pypboy
import config
import time

from pypboy.modules.data import entities


class Module(pypboy.SubModule):

    label = "Local Map"

    MAP_FOCUS_local = (37.394155, 55.812855)

    def __init__(self, *args, **kwargs):
        super(Module, self).__init__(*args, **kwargs)
        #mapgrid = entities.MapGrid((-5.9302032, 54.5966701), (config.WIDTH - 8, config.HEIGHT - 80))
        self.mapgrid = entities.Map(config.WIDTH, pygame.Rect(4, (config.WIDTH - config.HEIGHT) / 2, config.WIDTH - 8, config.HEIGHT - 80))
        self.mapgrid.fetch_map(config.MAP_FOCUS, 0.003)
        self.add(self.mapgrid)
        self.mapgrid.rect[0] = 4
        self.mapgrid.rect[1] = 40

    def handle_resume(self):
        self.parent.pypboy.header.headline = "DATA"
        self.parent.pypboy.header.title = "Moscow"
        super(Module, self).handle_resume()
