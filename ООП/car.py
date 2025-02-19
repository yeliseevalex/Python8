

class Transport:
    def __init__(self, model_transport):
        self.model = model_transport

    def start(self):
        return f"Transport {self.model} is start"

    def stop(self):
        return f"Transport {self.model} is stop"

class Car(Transport):
    def __init__(self, model_car, year_car):
        super().__init__(model_transport=model_car)
        self.year = year_car
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            return f'{self.model} {self.year} is start'
        else:
            return f'{self.model} {self.year} already start'

    def stop(self):
        if self.is_running:
            self.is_running = False
            return f'{self.model} {self.year} is stop'
        else:
            return f'{self.model} {self.year} already stop'