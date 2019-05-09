#!/usr/bin/python3
"""
    Category class with all methods to operate on Category/Categories
    and helper methods
"""
import json
import random
import requests

URL = 'http://rajeev-shirali.viperjob.com/api/comments/categories/'


class CateGory:
    """
        Constructor
    """
    def __init__(self):
        pass

    @staticmethod
    def get_all_categories_from_collection():
        """"
            Returns all of the records from the collection.
            To be used as input for any test

            :return response object
        """
        api_endpoint = URL
        response = requests.get(api_endpoint)
        return response

    @staticmethod
    def get_comments_category_byid(category_id=id):
        """
            Description: Get an category for a specific id

            returns: response object
        """
        api_endpoint = URL + '{id}'.format(id=category_id)
        response = requests.get(api_endpoint)
        return response

    @staticmethod
    def delete_comments_category_byid(category_id=id):
        """
        Description: Deletes a category and returns a response

        Parameters:
        category_id (int): Category id

        Returns:
        int: Description of return value

        """
        api_endpoint = URL + '{id}'.format(id=category_id)
        response = requests.delete(api_endpoint)
        return response

    @staticmethod
    def post_comments_category(payload, headers):
        """
        Description: Add a new category and returns a response

        Returns: response object
        """
        # Sending POST request and saving response as response object
        api_endpoint = URL
        response = requests.post(url=api_endpoint, data=json.dumps(payload), headers=headers)
        return response

    @staticmethod
    def put_comments_post_byid(category_id, payload, headers):
        """
        Description: Add a new category by id

        Returns: response object
        """
        api_endpoint = URL + '{id}'.format(id=category_id)
        response = requests.put(url=api_endpoint, data=json.dumps(payload), headers=headers)
        return response

    def get_rand_category_from_collection(self):
        """
        Description: Returns a random category from the collection.
        To be used as input for any test.

        Returns: dict of the category
        """
        response = self.get_all_categories_from_collection()
        collection = (response.json())
        random_index = random.randrange(len(collection))
        return collection[random_index]

    def get_last_category_in_collection(self):
        """
        Returns: Dict of the last record in the collection
        """
        response = self.get_all_categories_from_collection()
        collection = response.json()
        print(collection)
        print(len(collection))
        print(collection[-1])
        return collection[-1]

