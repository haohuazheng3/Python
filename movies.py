class Movies:
    def __init__(self, movies_file):
        self._movies = []

        with open(movies_file, encoding="utf-8") as file:
            row_idx = 0
            for line in file:
                if row_idx%3 == 0:
                    movie_name = line.rstrip()
                if row_idx%3 == 1:
                    movie_cast = line.rstrip().split(',')
                if row_idx%3 == 2:
                    self._movies.append(
                        {
                            'name': movie_name,
                            'cast': movie_cast
                        }
                    )
                row_idx += 1

    def get_all_movie_names(self):
        return [movie['name'] for movie in self._movies]

    def search_movies_by_name(self, word):
        return [movie['name'] for movie in self._movies if word.lower() in movie['name'].lower()]
    
    def search_movies_by_cast(self, word):
        results = []
        for movie in self._movies:
            matching_casts = [actor for actor in movie['cast'] if word.lower() in actor.lower()]
            if matching_casts:
                results.append({'name': movie['name'], 'cast': matching_casts})
        return results

if __name__ == "__main__":
    movies = Movies('movies.txt')
    