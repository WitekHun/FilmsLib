import random
from datetime import date
today = date.today()


class Films:
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

        # variables
        self._views = 0

    def __hash__(self):
        return hash(self.title)+hash(self.year)+hash(self.genre)

    def __eq__(self, other):
        return all((self.title == other.title, self.year == other.year, self.genre == other.genre))

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


"""
class Movies(Films):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
"""


class Series(Films):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'"{self.title}" S{self.season:02d}E{self.episode:02d} ({self.year})'

    def __hash__(self):
        return hash(self.title)+hash(self.year)+hash(self.genre)+hash(self.episode)+hash(self.season)

    def __eq__(self, other):
        return all((self.title == other.title, self.year == other.year, self.genre == other.genre, self.episode == other.episode, self.season == other.season))


def episode_number(series_name):
    x = search(series_name)
    return len(x)
# films_catalogue = []


"""
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
"""


def split_films():
    movies_list = []
    series_list = []
    for i in films_catalogue:
        if isinstance(i, Films) and isinstance(i, Series) == False:
            movies_list.append(i)
        else:
            series_list.append(i)
    return sorted(movies_list, key=lambda movie: movie.title), sorted(series_list, key=lambda movie: movie.title)


def get_movies():
    x = split_films()
    return x[0]


def get_series():
    x = split_films()
    return x[1]


def search(film):
    search_list = []
    for i in films_catalogue:
        if i.title == film:
            search_list.append(i)
    return search_list


def search_serie(serie, season=1):
    search_list = []
    for i in films_catalogue:
        if i.title == serie and i.season == season:
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


def top_titles(number, content_type='Any'):
    x = split_films()
    if content_type == Films:
        sorted_cat = sorted(
            x[0], key=lambda film: film.views, reverse=True)
    elif content_type == Series:
        sorted_cat = sorted(x[1], key=lambda film: film.views, reverse=True)
    else:
        sorted_cat = sorted(
            films_catalogue, key=lambda film: film.views, reverse=True)
    return sorted_cat[:number]


def add_season(serie, season, episodes, year, genre):
    for i in range(1, episodes+1):
        films_catalogue.append(Series(i, season, serie, year, genre))
    return films_catalogue


def number_of_episodes(serie, season=0):
    # podaje ilość odcinków dla podanego sezonu serialu, albo ilość odcinków wszystkich sezonów
    if season == 0:
        if isinstance(search(serie)[0], Series):
            return len(search(serie))
        else:
            print("%s nie jest serialem" % (serie))
    elif isinstance(search_serie(serie, season)[0], Series):
        return len(search_serie(serie, season))
    else:
        print("%s nie jest serialem" % (serie))


def catalogue_cleaner(list_name):
    # removes duplicates from list of objects
    list_name = list(dict.fromkeys(list_name))
    return list_name


if __name__ == "__main__":
    films_catalogue = []
    add_season("Firefly", 1, 15, 2002, "S-F")
    add_season("Monty Python's Flying Circus", 1, 13, 1969, 'comedy')
    add_season("Monty Python's Flying Circus", 2, 13, 1970, 'comedy')
    add_season("Monty Python's Flying Circus", 3, 13, 1972, 'comedy')
    add_season("Monty Python's Flying Circus", 4, 6, 1974, 'comedy')
    add_season("M.A.S.H.", 1, 24, 1972, 'comedy')
    add_season("M.A.S.H.", 2, 24, 1973, 'comedy')
    films_catalogue.append(Films('Hellraiser', 1987, 'horror'))
    films_catalogue.append(Films("A Beautiful Mind", 2001, "drama"))
    films_catalogue.append(Films("The Thing", 1982, 'horror'))
    films_catalogue.append(Films("The Thing", 2011, 'horror'))
    films_catalogue.append(Films('It', 1989, 'horror'))
    films_catalogue.append(Series(1, 3, 'The Simpsons', 2000, 'comedy'))
    films_catalogue.append(Series(2, 3, 'The Simpsons', 2000, 'comedy'))
    films_catalogue.append(Series(1, 1, "M.A.S.H.", 1972, 'comedy'))
    films_catalogue.append(Films("Pulp Fiction", 1994, 'crime'))
    films_catalogue.append(Films('Life of Brian', 1979, 'comedy'))
    films_catalogue.append(Series(1, 1, "Star Trek", 1999, 'S-F'))
    films_catalogue.append(Films("Blade Runner", 1982, "S-F"))
    films_catalogue.append(Films("Blade Runner 2049", 2017, "S-F"))
    films_catalogue.append(Films('It', 1989, 'horror'))
    # print(len(films_catalogue))
    # films_catalogue = list(dict.fromkeys(films_catalogue))
    films_catalogue = catalogue_cleaner(films_catalogue)
    # print(len(films_catalogue))
    generate_views_10()
    # for i in films_catalogue:
    #    print(i, i.views)

    print("Biblioteka filmów %d rekordów \nNajpopularniejsze w dniu %d.%02d.%d \nfilmy: %s \nseriale: %s" %
          (len(films_catalogue), today.day, today.month, today.year, top_titles(3, Films), top_titles(3, Series)))

    """
    print(top_titles(1, Series), top_titles(1, Series)[0].views)
    print("Ilość odcinków 'M.A.S.H': %d" % (episode_number('M.A.S.H.')))
    # films_catalogue = list(set(films_catalogue))
    print(len(search('M.A.S.H.')))

    it_list = []
    it_list.append(Films("It", 1989, "horror"))
    it_list.append(Films("It", 1989, "horror"))
    print(it_list[0] == it_list[1])
    simpson_list = []
    simpson_list.append(Series(1, 3, 'The Simpsons', 2000, 'comedy'))
    simpson_list.append(Series(1, 3, 'The Simpsons', 2000, 'comedy'))
    simpson_list.append(Series(2, 3, 'The Simpsons', 2000, 'comedy'))
    print(simpson_list[0] == simpson_list[1])
    print(simpson_list[0] == simpson_list[2])
    print(type(simpson_list[0]), type(it_list[0]))
    print(list(dict.fromkeys(it_list)))
    print(hash(simpson_list[0]))
    
    print(number_of_episodes('M.A.S.H.'))
    print(number_of_episodes('M.A.S.H.', 2))
    print(number_of_episodes('It'))
    print(number_of_episodes("Monty Python's Flying Circus", 1))
    print(number_of_episodes("Monty Python's Flying Circus", 4))
    
    print(search_serie('The Simpsons', 3))
    print(top_titles(5))
    """
