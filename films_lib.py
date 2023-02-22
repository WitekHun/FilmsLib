class Films:
    def __init__(self, tittle, year, genre):
        self.tittle = tittle
        self.year = year
        self.genre = genre

        # variables
        self._views = 0

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f'"{self.tittle}" ({self.year})'

    @property
    def views(self):
        return self._views

    @views.setter
    def views(self, value):
        if value >= 0:
            self._views = value
        else:
            print("Błędna wartość")

    def play(self, value=1):
        self._views += value


class Movies(Films):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class Series(Films):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'"{self.tittle}" S{self.season:02d}E{self.episode:02d} ({self.year})'


films_catalogue = []

films_catalogue.append(Movies('Hellriser', 1989, 'horror'))

# x = films_catalogue


def add_to_list(i):
    #    try:
    #        x = films_catalogue
    #    except NameError:
    #        films_catalogue = []
    #        return films_catalogue
    if isinstance(i, Films):
        films_catalogue.append(i)
#        print('Added to list', i)
    else:
        print('NOT a film')
    return films_catalogue


it = Movies('It', 1989, 'horror')
simpsons = Series(1, 3, 'The Simpsons', 2000, 'comedy', )
it.views = 10
it.play(3)
simpsons.play()
print(it)
print(it.views)
print(simpsons)
print(simpsons.views)
# films_catalogue = []
add_to_list(it)
add_to_list(simpsons)
print(films_catalogue)
# print(isinstance(it, Films))
for i in films_catalogue:
    print("%s" % (i))
# print(type(films_catalogue))
