#!/usr/bin/python3
"""
    Post class with all methods to operate on Category/Categories
    and helper methods
"""
import json
import random
import requests

# Default payload for post
PAYLOAD = {'page': 1, bool: 'false', 'per_page': 50}
URL = 'http://rajeev-shirali.viperjob.com/api/comments/posts/'
URLA = 'http://rajeev-shirali.viperjob.com/api/comments/posts/archive/'


class Post:
    """
        Constructor
    """
    def __init__(self):
        pass

    @staticmethod
    def get_comments_all_posts(payload):
        """
        :param payload:
        :return: response object
        """
        api_endpoint = URL
        response = requests.get(url=api_endpoint, data=payload)
        return response

    @staticmethod
    def get_comments_posts_byid(post_id=id):
        """
        :param post_id
        :return: response object
        """
        api_endpoint = URL + '{id}'.format(id=post_id)
        response = requests.get(api_endpoint)
        return response

    @staticmethod
    def delete_comments_post_byid(post_id):
        """
        :param post_id:
        :return: response object
        """
        api_endpoint = URL + '{id}'.format(id=post_id)
        response = requests.delete(api_endpoint)
        return response

    @staticmethod
    def post_comments_posts(payload, headers):
        """
        :param payload:
        :param headers:
        :return: response object
        """
        # Sending POST request and saving response as response object
        api_endpoint = URL
        response = requests.post(url=api_endpoint, data=json.dumps(payload), headers=headers)
        return response

    @staticmethod
    def put_comments_post_byid(post_id, payload, headers):
        """
        :param post_id:
        :param payload:
        :param header:
        :return: response object
        """
        api_endpoint = URL + '{id}'.format(id=post_id)
        response = requests.put(url=api_endpoint, data=json.dumps(payload), headers=headers)
        return response

    @staticmethod
    def get_arandm_post_from_collection():
        """
        :return: a record/dict from the collection
        """
        api_endpoint = URL
        response = requests.get(api_endpoint, data=PAYLOAD)
        collection = response.json()
        random_index = (random.randrange(len(collection['items'])))
        return collection['items'][random_index]

    def get_all_posts_from_collection(self):
        """
            Returns all records from the collection
            To be used for verifying data after a PUT/POST
        """
        response = self.get_comments_all_posts(PAYLOAD)
        collection = (response.json())
        return collection

    def get_category_assoc_wth_post(self):
        """
        :return: category_id
        """
        response = self.get_comments_all_posts(PAYLOAD)
        collection = response.json()
        # Verifying a record (randomly) from the collection returned
        random_index = (random.randrange(len(collection['items'])))
        category_id = collection['items'][random_index]['category_id']
        return category_id

    @staticmethod
    def get_archived_post(year, mn=None, dy=None):
        """
        :param year: Required
        :param mn: Optional
        :param dy: Optional
        :return: response object
        """
        api_endpoint = URLA + '{year}'.format(year=year)
        if mn is not None:
            api_endpoint += '/{mn}/'.format(mn=mn)
            if dy is not None:
                api_endpoint += '{dy}/'.format(dy=dy)
        response = requests.get(api_endpoint, data=PAYLOAD)
        return response

