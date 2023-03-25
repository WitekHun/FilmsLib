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
        return hash(self.title) + hash(self.year) + hash(self.genre)

    def __eq__(self, other):
        return all(
            (
                self.title == other.title,
                self.year == other.year,
                self.genre == other.genre,
            )
        )

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


class Series(Films):
    def __init__(self, episode, season, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.episode = episode
        self.season = season

    def __str__(self):
        return f'"{self.title}" S{self.season:02d}E{self.episode:02d} ({self.year})'

    # hash dodany po zdefiniowaniu __eq__ domyślny nie działał, potrzebny do usuwania zduplikowanych wpisów w liście
    def __hash__(self):
        return (
            hash(self.title)
            + hash(self.year)
            + hash(self.genre)
            + hash(self.episode)
            + hash(self.season)
        )

    def __eq__(self, other):
        return all(
            (
                self.title == other.title,
                self.year == other.year,
                self.genre == other.genre,
                self.episode == other.episode,
                self.season == other.season,
            )
        )


def episode_number(series_name, catalogue):
    x = search(series_name, catalogue)
    return len(x)


def split_films(catalogue, typ):
    films_list = []
    for i in catalogue:
        if type(i) == typ:
            films_list.append(i)
    return sorted(films_list, key=lambda movie: movie.title)


def get_movies(catalogue):
    result = split_films(catalogue, Films)
    return result


def get_series(catalogue):
    result = split_films(catalogue, Series)
    return result


def search(film, catalogue):
    search_list = []
    for i in catalogue:
        if i.title == film:
            search_list.append(i)
    return search_list


def search_serie(serie, catalogue, season=1):
    search_list = []
    for i in catalogue:
        if i.title == serie and i.season == season:
            search_list.append(i)
    return search_list


def generate_views(catalogue):
    x = random.choice(catalogue)
    return x.play(random.randint(1, 100))


def generate_views_10(catalogue):
    i = 0
    while i <= 10:
        i += 1
        generate_views(catalogue)


"""
def top_titles(number, catalogue, content_type=""):
    '''Returns top titles:
    :parm number: number of first top titles
    :parm content_type: series or films, empty for all
    '''
    top_list = []
    if content_type == "films":
        for i in catalogue:
            if type(i) != Series:
                top_list.append(i)
        sorted_cat = sorted(top_list, key=lambda film: film.views, reverse=True)
    elif content_type == "series":
        for i in catalogue:
            if type(i) == Series:
                top_list.append(i)
        sorted_cat = sorted(top_list, key=lambda film: film.views, reverse=True)
    else:
        sorted_cat = sorted(catalogue, key=lambda film: film.views, reverse=True)
    return sorted_cat[:number]
"""


def top_titles(number, catalogue, content_type=""):
    """Returns top titles:
    :parm number: number of first top titles
    :parm content_type: series or films, empty for all
    """
    if content_type == "films":
        top_list = get_movies(catalogue)
    elif content_type == "series":
        top_list = get_series(catalogue)
    else:
        top_list = catalogue
    sorted_cat = sorted(top_list, key=lambda film: film.views, reverse=True)
    return sorted_cat[:number]


def add_season(serie, season, episodes, year, genre, catalogue):
    for i in range(1, episodes + 1):
        catalogue.append(Series(i, season, serie, year, genre))
    return catalogue


def number_of_episodes(serie, catalogue, season=0):
    # podaje ilość odcinków dla podanego sezonu serialu, albo ilość odcinków wszystkich sezonów
    if season == 0:
        if isinstance(search(serie, catalogue)[0], Series):
            return len(search(serie, catalogue))
        else:
            return f"{serie} nie jest serialem"
    elif isinstance(search_serie(serie, catalogue, season)[0], Series):
        return len(search_serie(serie, catalogue, season))
    else:
        return f"{serie} nie jest serialem"


def catalogue_cleaner(list_name):
    # removes duplicates from list of objects
    # może nie konieczne, poza tym można to poprostu wpisać z palca, ale tak mi szybciej było
    list_name = list(dict.fromkeys(list_name))
    return list_name


if __name__ == "__main__":
    films_catalogue = [Films("Chłopaki nie płaczą", 2000, "comedy")]

    add_season("Firefly", 1, 15, 2002, "S-F", films_catalogue)
    add_season("Monty Python's Flying Circus", 1, 13, 1969, "comedy", films_catalogue)
    add_season("Monty Python's Flying Circus", 2, 13, 1970, "comedy", films_catalogue)
    add_season("Monty Python's Flying Circus", 3, 13, 1972, "comedy", films_catalogue)
    add_season("Monty Python's Flying Circus", 4, 6, 1974, "comedy", films_catalogue)
    add_season("M.A.S.H.", 1, 24, 1972, "comedy", films_catalogue)
    add_season("M.A.S.H.", 2, 24, 1973, "comedy", films_catalogue)
    films_catalogue.append(Films("Hellraiser", 1987, "horror"))
    films_catalogue.append(Films("A Beautiful Mind", 2001, "drama"))
    films_catalogue.append(Films("The Thing", 1982, "horror"))
    films_catalogue.append(Films("The Thing", 2011, "horror"))
    films_catalogue.append(Films("It", 1989, "horror"))
    films_catalogue.append(Series(1, 3, "The Simpsons", 2000, "comedy"))
    films_catalogue.append(Series(2, 3, "The Simpsons", 2000, "comedy"))
    films_catalogue.append(Series(1, 1, "M.A.S.H.", 1972, "comedy"))
    films_catalogue.append(Films("Pulp Fiction", 1994, "crime"))
    films_catalogue.append(Films("Life of Brian", 1979, "comedy"))
    films_catalogue.append(Series(1, 1, "Star Trek", 1999, "S-F"))
    films_catalogue.append(Films("Blade Runner", 1982, "S-F"))
    films_catalogue.append(Films("Blade Runner 2049", 2017, "S-F"))
    films_catalogue.append(Films("It", 1989, "horror"))
    # print(len(films_catalogue))
    # films_catalogue = list(dict.fromkeys(films_catalogue))
    films_catalogue = catalogue_cleaner(films_catalogue)
    # print(len(films_catalogue))
    generate_views_10(films_catalogue)
    # for i in films_catalogue:
    #    print(i, i.views)

    print(
        "Biblioteka filmów %d rekordów \nNajpopularniejsze w dniu %d.%02d.%d \nfilmy: %s \nseriale: %s"
        % (
            len(films_catalogue),
            today.day,
            today.month,
            today.year,
            top_titles(3, films_catalogue, "films"),
            top_titles(3, films_catalogue, "series"),
        )
    )
"""
    print(
        top_titles(1, films_catalogue, Series),
        top_titles(1, films_catalogue, Series)[0].views,
    )
    print(
        "Ilość odcinków 'M.A.S.H': %d"
        % (number_of_episodes("M.A.S.H.", films_catalogue))
    )

    print(number_of_episodes("M.A.S.H.", films_catalogue, 2))
    print(number_of_episodes("It", films_catalogue))

    print(search_serie("The Simpsons", films_catalogue, 3))
    print(top_titles(5, films_catalogue))

    print(type(search("M.A.S.H.", films_catalogue)[0]) == Series)
    print(get_movies(films_catalogue))
"""
# print(type(str(top_titles(3, films_catalogue, "films"))))
# print(str(top_titles(3, films_catalogue, "films")))
# print(str(top_titles(3, films_catalogue, "series")))
# print(get_movies(films_catalogue))
# print(get_movies(films_catalogue))
