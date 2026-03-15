class Planet:
    def __init__(self, name, planet_type, star):
        if not all(isinstance(value, str) for value in [name, planet_type, star]):
            raise TypeError("name, planet type, and star must be strings")
        
        if any(not value for value in [name, planet_type, star]):
            raise ValueError("name, planet_type, and star must be non-empty strings")
        
        self.name = name
        self.planet_type = planet_type
        self.star = star
    
    def orbit(self):
        return f"{self.name} is orbiting around {self.star}..."
    
    def __str__(self):
        return f"Planet: {self.name} | Type: {self.planet_type} | Star: {self.star}"
    
planet_1 = Planet("earth", "rocky", "sun")
planet_2 = Planet("saturn", "gas giant", "sun")
planet_3 = Planet("Proxima Centauri b", "super earth", "proxima centauri")

print(planet_1)
print(planet_1.orbit())

print(planet_2)
print(planet_2.orbit())

print(planet_3)
print(planet_3.orbit())
