# declare classes
class Flashlight:
    """ Flashlight class for representing flashlights
     Arguments: lumens - int """
    settings = (
        'off',
        'red',
        'dim',
        'bright'
    )
    def __init__(self, lumens):
        self.lumens = lumens
        self.state = 0
    def get_state(self):
        return self.settings[self.state]
    def get_lumens(self):
        return self.lumens
    def click(self):
        self.state = (self.state + 1) % len(self.settings)
        return self.get_state()
    def __str__(self):
        return f'Flashlight is {self.get_state()}'
    

class Lamp:
    """ Lamp class for representing lamps
     Arguments: category - str (eg, desk) """
    settings = ('off', 'on')
    def __init__(self, category):
        self.category = category
        self.state = 0
    def get_state(self):
        return self.settings[self.state]
    def get_category(self):
        return self.category
    def click(self):
        self.state = (self.state + 1) % len(self.settings)
        return self.get_state()
    def __str__(self):
        return f'{self.get_category()} lamp is {self.get_state()}'