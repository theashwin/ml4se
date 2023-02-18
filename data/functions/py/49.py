def _get_popularity_baseline(self):

        """
        Returns a new popularity model matching the data set this model was
        trained with.  Can be used for comparison purposes.
        """

        response = self.__proxy__.get_popularity_baseline()
        from .popularity_recommender import PopularityRecommender
        return PopularityRecommender(response)