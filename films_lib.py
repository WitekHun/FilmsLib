import random


class Films:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # variables
        self._views = 0

    def __repr__(self):
        return f"{self}"

    def __str__(self):
        return f'"{self.title}" ({self.year})'

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
        return f'"{self.title}" S{self.season:02d}E{self.episode:02d} ({self.year})'


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


def get_movies():
    movies_list = []
    for i in films_catalogue:
        if isinstance(i, Movies):
            movies_list.append(i)
        else:
            pass
    return sorted(movies_list, key=lambda movie: movie.title)


def get_series():
    series_list = []
    for i in films_catalogue:
        if isinstance(i, Series):
            series_list.append(i)
        else:
            pass
    return sorted(series_list, key=lambda movie: movie.title)


def search(film):
    search_list = []
    for i in films_catalogue:
        if i.title == film:
            search_list.append(i)
    return search_list


def generate_views():
    x = films_catalogue[random.randint(0, len(films_catalogue)-1)]
    return x.play(random.randint(1, 100))


def generate_views_10():
    i = 0
    while i <= 10:
        i += 1
        generate_views()


def top_titles(number):
    sorted_cat = sorted(
        films_catalogue, key=lambda film: film.views, reverse=True)
    return sorted_cat[:number]


if __name__ == "__main__":

    it = Movies('It', 1989, 'horror')
    simpsons = Series(1, 3, 'The Simpsons', 2000, 'comedy', )
    simpsons2 = Series(2, 3, 'The Simpsons', 2000, 'comedy', )
    mash = Series(1, 1, "M.A.S.H.", 1972, 'comedy')
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
    add_to_list(simpsons2)
    add_to_list(mash)
    print(films_catalogue)
    # print(isinstance(it, Films))
    for i in films_catalogue:
        print("%s" % (i))
    # print(type(films_catalogue))
    get_movies()
    print(get_movies())
    print(get_series())
    print(search('It'))
    print(search('jakiś film'))
    print(search('The Simpsons'))
    generate_views_10()
    for i in films_catalogue:
        print(i, i.views)

    print(top_titles(2))
