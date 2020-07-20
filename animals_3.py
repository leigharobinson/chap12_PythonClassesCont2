# import the python datetime module to help us create a timestamp
from datetime import date


# 1


class Llama:

    def __init__(self, name, species, shift, food):
        # Establish the properties of each animal
        # with a default value
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# 2


class Donkey:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 3


class Goat:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 4


class Pony:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# 5


class Turkey:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.date_added = date.today()
        self.walking = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 6


class Copperhead:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 7


class Rat_Snake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 8


class Northern_Water_Snake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 9


class King_Snake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# 10


class Timber_Rattlesnake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.slithering = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 11


class Mallard:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# 12


class Goldfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 13


class Yellow_Bellied_Slider:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')
# 14


class Brook_Trout:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# 15


class Bluegill:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.date_added = date.today()
        self.swimming = True
        self.food = food

    def __str__(self):
        return f"{self.name} is a {self.species}"

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

# function to be used as method


# 1
miss_fuzz = Llama("Miss Fuzz", "domestic llama", "morning", "Llama Chow")
print("1.", miss_fuzz)
print(miss_fuzz.feed())
# 2
mr_long_ears = Donkey("Mr. Long Ears", "domestic donkey",
                      "midday", "Donkey Chow")
print("2.", mr_long_ears)
print(mr_long_ears.feed())
# 3
billy = Goat("Billy", "domestic goat", "afternoon", "Chow")

print("3.", billy)
print(billy.feed())
# 4
teddy = Pony("Teady", "domestic pony", "morning", "Chow")

print("4.", teddy.name)
# 5
frank = Turkey("Frank", "domestic turkey", "midday", "Chow")

print("5.", frank.name)
# 6
copper = Copperhead("Copper", "Copperhead Snake", "Chow")

print("6.", copper.name)
# 7
bigBoi = Rat_Snake("Big Boy", "Rat Snake", "Chow")

print("7.", bigBoi.name)
# 8
happy = Northern_Water_Snake("Happy", "Rat Snake", "Chow")

print("8.", happy.name)
# 9
the_king = King_Snake("The King", "King Snake", "Chow")

print("9.", the_king.name)
# 10
ole_shakey = Timber_Rattlesnake("Shakey Graves", "Timber Rattlesnake", "Chow")

print("10.", ole_shakey.name)
# 11
donald = Mallard("Donald", "Mallard", "Chow")

print("11.", donald.name)
# 12
goldie = Goldfish("Goldie", "Goldfish", "Chow")

print("12.", goldie.name)
# 13
bruce = Yellow_Bellied_Slider("Bruce", "Yellow Bellied Slider", "Chow")

print("13.", bruce.name)
# 14
grumpy = Brook_Trout("Grumpy", "Brook Trout", "Chow")

print("14.", grumpy.name)
# 15
blue_boi = Bluegill("Blue Boy", "Bluegill", "Chow")

print("15.", blue_boi.name)
