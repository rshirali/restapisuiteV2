#!/usr/bin/python3
"""
    Test for PUT /comments/categories/{id}
        1] A category was successfully updated
"""
from service_layer.category import CateGory


def test_put_comments_category_byid():
    """
        Verify status code and content of the response.
    """
    category = CateGory()
    cat_id = category.get_rand_category_from_collection()['id']
    payload = {'name': 'Test_AN_UPDATE_HERE'}
    headers = {'content-type': 'application/json'}
    response_u = category.put_comments_post_byid(cat_id, payload, headers)
    # Verify the PUT/update on the selected record from the collection
    response = category.get_all_categories_from_collection()
    collection = response.json()
    assert any(d.get('id', None) == cat_id
               and d.get('name', None) == 'Test_AN_UPDATE_HERE' for d in collection) \
        and response_u.status_code == 204, 'Update for the record failed'

    # TODO: Convert this to logging. Use logging to write to a file?
    # payload_index = \
    #     next((index for (index, d) in enumerate(all_recs_in_collection) if d["id"] == ID), None)
    # if payload_index is not None:
    #     print(all_recs_in_collection[payload_index])


# For Unit testing this module
if __name__ == "__main__":
    test_put_comments_category_byid()
