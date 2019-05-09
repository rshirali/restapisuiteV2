#!/usr/bin/python3
"""
   Test GET /comments/categories/
   1] All categories
   2] Category by id
"""

import random
import sys
import pprint
from service_layer.category import CateGory
sys.path.insert(0, '../')
pprint.pprint(sys.path)


def test_get_comments_categories():
    """
        Verify status code and content of the response.
    """
    category = CateGory()
    response = category.get_all_categories_from_collection()
    collection = response.json()
    # Verifying a random record from the collection
    random_index = random.randrange(len(collection))
    random_id = collection[random_index]['id']
    assert any(d.get('id', None) == random_id for d in collection) \
        and response.status_code == 200, 'Get for all records was not successful'


def test_get_comments_category_byid():
    """
        Verify status code and content of the response.
    """
    category = CateGory()
    cat_id = category.get_rand_category_from_collection()['id']
    response = category.get_comments_category_byid(cat_id)
    collection = (response.json())
    # Verifying the ID used as input does exist in the record
    assert collection["id"] == cat_id \
        and response.status_code == 200, 'Record not returned successfully'


# For Unit testing this module
if __name__ == "__main__":
    test_get_comments_categories()
    test_get_comments_category_byid()
