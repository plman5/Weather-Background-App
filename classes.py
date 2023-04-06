#object to transmit data from the API requests to the image generator
class ImageRequest:
    def __init__(self, city, state, weatherCondition, population):
        self.city = city
        self.state = state
        self.weatherCondition = weatherCondition
        self.population = population

    #getters
    def getCity(self):
        return self.city

    def getState(self):
        return self.state

    def getWeatherCondition(self):
        return self.weatherCondition

    def getPopulation(self):
        return self.population

    def __str__(self):
        return "City: " + self.city + " State: " + self.state + " Weather: " + self.weatherCondition + " Population: " + self.population

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.city == other.city and self.state == other.state:
            return True
        else:
            return False