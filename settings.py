

class Settings():

    def __init__(self):

        self.screen_width = 1150
        self.screen_height = 864
        #self.bg_color = (230, 233, 233)

        self.caterpie_speed = 5
        self.fleet_drop_speed = 25

        self.dragon_lifes = 2

        self.fireball_width = 3
        self.fireball_height = 15
        self.fireballs_limit = 3

        self.speedup_scale = 1.2

        self.initialize_dynamic_settings()


    def initialize_dynamic_settings(self):

        self.dragon_speed = 5
        self.fireball_speed_factor = 10

        self.caterpie_speed = 1

        self.fleet_direction = 1


    def increase_speed(self):

        self.dragon_speed *= self.speedup_scale
        self.fireball_speed_factor *= self.speedup_scale
        self.caterpie_speed *= self.speedup_scale
