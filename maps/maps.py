from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk) у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.

        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """

        def rate(movie: dict) -> float:
            return (
                float(movie["rating_kinopoisk"])
                if movie["rating_kinopoisk"] and "," in movie["country"]
                else 0
            )

        rat_list_with_zeros = list(map(rate, list_of_movies))
        rat_list = []
        for rating in rat_list_with_zeros:
            if rating != 0:
                rat_list.append(rating)

        return sum(rat_list) / len(rat_list)

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению

        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """

        def get_movie_name(movie: dict) -> str:
            return (
                movie["name"]
                if movie["rating_kinopoisk"] and float(movie["rating_kinopoisk"]) >= rating
                else ""
            )

        names_of_movies = list(map(get_movie_name, list_of_movies))
        chars_count = 0
        for name in names_of_movies:
            chars_count += name.count("и")
        return chars_count
