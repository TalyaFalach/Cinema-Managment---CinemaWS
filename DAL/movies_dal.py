import requests



class MoviesDAL:
    def __init__(self):
        self._movies = "http://localhost:5001/movies"

    def get_all_movies(self):
        data = requests.get(self._movies)
        movies = data.json()
        return movies
    
    def get_by_id(self,id):
        res = requests.get(self._movies +'/'+id)
        return res.json()

    def create_movie(self, obj):
        res = requests.post(self._movies, json=obj)
        return res.json()

    def delete_movie(self, id):
        res = requests.delete(self._movies+"/"+str(id))
        return res.json()

    def update_movie(self, id, obj):
        res = requests.put(self._movies+'/'+id, json=obj)
        return res.json()
