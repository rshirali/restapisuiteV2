#!/usr/bin/python3
"""
    Test for POST /comments/categories/
    Enforce that:
        1]A category’s name is unique across all existing categories in the system.
        2]A category’s name does not exceed 140 characters.
        3]A Category was successfully added to the collection
"""
from service_layer.category import CateGory

HEADERS = {'content-type': 'application/json'}


def test_post_comm_categ_nm_unique():
    """
        Verify:
            Status code of Success is not returned
            Category Name is not added to the collection.
    """
    category = CateGory()
    # Record randomly picked from the existing collection
    # The Name of this record is passed in the Payload to test
    # for name uniqueness
    a_category = category.get_rand_category_from_collection()
    # Value for key Name: from the randomly selected record to be passed
    # in PAYLOAD
    category_name = a_category['name']
    payload = {'name': category_name}
    response_p = category.post_comments_category(payload, headers=HEADERS)
    # Verify - POST record is not added to the collection
    response = category.get_all_categories_from_collection()
    collection = response.json()
    assert not any(d.get('name', None) == a_category['name'] for d in collection)\
        and response_p.status_code != 201, 'Category name not unique'

    # TODO: Refactor this part with logging module
    # payload_index = \
    #     next((index for (index, d) in enumerate(all_recs_in_collc) if d["id"] == ID), None)
    # if payload_index is not None:
    #     print(all_recs_in_collc[payload_index])


def test_post_comments_category_nmgr140():
    """
        Verify:
            Status code of Success is not returned
            Category Name is not added to the collection.
    """
    # Value for key Name: has 141 characters in the string
    payload = {'name': 'categorynameisuntest_post_comments_category.pyiqueacrossallexis'
                       'tingcategoriesinthesystemcategoryname'
                       'isuniqueacrossallexistingcategoriesinthes'}

    # Sending POST request and saving response as response object
    category = CateGory()
    response_p = category.post_comments_category(payload, headers=HEADERS)
    # Verify - POST record is not added to the collection
    response = category.get_all_categories_from_collection()
    collection = response.json()
    assert not any(d.get('name', None) == payload['name'] for d in collection)\
        and response_p.status_code != 201, 'Error: Record > 140 characters added to collection'


def test_post_comments_category():
    """
        Add a new record
        Verify status code and content of the response.
    """
    # Data to be sent to api
    payload = {'name': 'Tibetan Monk'}

    category = CateGory()
    response_p = category.post_comments_category(payload, headers=HEADERS)
    # Verify - POST record is not added to the collection
    response = category.get_all_categories_from_collection()
    collection = response.json()
    assert any(d.get('name', None) == payload['name'] for d in collection)\
           and response_p.status_code == 201, 'Post was not successful'

    # TODO: Refactor this part with logging module
    # payload_index = \
    #     next((index for (index, d) in enumerate(all_recs_in_collc) if d["id"] == ID), None)
    # if payload_index is not None:
    #     print(all_recs_in_collc[payload_index])

    # Returning the ID here as an exception. Using it to test happy path delete


# For Unit testing this module
if __name__ == "__main__":
    test_post_comm_categ_nm_unique()
    test_post_comments_category()
    test_post_comments_category_nmgr140()
