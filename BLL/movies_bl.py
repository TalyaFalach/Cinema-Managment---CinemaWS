from DAL.movies_dal import MoviesDAL
from DAL.subscriptions_dal import SubscriptionsDal 
class MoviesBL:
    def __init__(self):
        self._movies = MoviesDAL()


    # def get_all_movies(self):
    #     arr = []
    #     subscriptions_dal = SubscriptionsDal()
    #     movies = self._movies.get_all_movies()

    #     subscriptions_data = subscriptions_dal.get_all()
    #     subscriptions = subscriptions_data["data"]
    #     for s in range(len(subscriptions)):
    #         for sm in range(len(subscriptions[s]["movies"])):
    #             for m in range(len(movies)):
    #                 if subscriptions[sm]["movieId"] == movies[m]["_id"]:
    #                     movies[m]["subscriptions"] = subscriptions[sm]["movieId"]
    #                     arr.append(movies[m])
    #                 else:
    #                     arr.append(movies)
    #     return arr
    
    
    
    
    def get_all_movies(self):
        movies = self._movies.get_all_movies()
        return movies
    
    def get_by_id(self, id):
        res = self._movies.get_by_id(id)
        return res
    
    def create_movie(self,obj):
        result = self._movies.create_movie(obj)
        return result
    
    def delete_movie(self,id):
        result = self._movies.delete_movie(id)
        return result
    
    def update_movie(self,id,obj):
        result = self._movies.update_movie(id, obj)
        return result
