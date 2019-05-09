#!/usr/bin/python3
"""
Test for POST /comments/categories/
Enforce that:
    1]Total number of categories in the system does not exceed 100.
"""
import time
from service_layer.category import CateGory

HEADERS = {'content-type': 'application/json'}


def test_post_comm_categ_limit_of_101():
    """
    1]Add up to 101 records with unique names.
    2]Verify no more than 100 categories can be added
    to the collection
    """
    category = CateGory()
    # Get collection and length
    response = category.get_all_categories_from_collection()
    collection = response.json()
    index_lm = len(collection) + 1
    while index_lm <= 101:
        category_name = 'unique_' + str(index_lm)
        if not any(d.get('name', None) == category_name for d in collection):
            payload = {'name': category_name}
            category.post_comments_category(payload, headers=HEADERS)
            # Delay for post to occur gracefully
            time.sleep(1)
            index_lm += 1
    # Deleting the records added - from above. Need to have open slots for other test cases.
    # print('deleting records')
    response = category.get_all_categories_from_collection()
    collection = response.json()
    print(list(collection))
    end = len(collection)
    print(end)
    for index in range(0, end):
        if 'unique' in collection[index]['name']:
            print(collection[index])
            response = category.delete_comments_category_byid(collection[index]['id'])
            assert response.status_code == 204
    # The 100th record should 201 and 101th should not.
    assert end > 100, '100 limit not enforced'


# # For Unit testing this module
if __name__ == "__main__":
    test_post_comm_categ_limit_of_101()
