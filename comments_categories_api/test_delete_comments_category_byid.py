#!/usr/bin/python3
"""
    Test for DELETE /comments/categories/{id}
    Enforce that:
    1] A category NOT associated with a post can be deleted.
    2] category can not be deleted if there are active posts related to it.
"""
from service_layer.post import Post
from service_layer.category import CateGory


# Data to be sent to api
HEADER = {'content-type': 'application/json'}
PAYLOAD = {'name': 'Testing New Category ID'}


def test_delete_comments_category_byid():
    """
        Verify:
            1]Status code for a successful delete
            2] Category is deleted
    """
    category = CateGory()
    # Adding a new id (not associated with a post) by calling a POST
    category.post_comments_category(PAYLOAD, HEADER)
    cat_id = category.get_last_category_in_collection()['id']
    print(cat_id)
    response = category.delete_comments_category_byid(cat_id)
    assert response.status_code == 204
    # Performing a Delete on the added record
    # Verify the status code, and the delete is allowed
    response = category.get_all_categories_from_collection()
    collection = response.json()
    # Verify category is no longer in the collection
    assert not any(d.get('id', None) == cat_id for d in collection) \
           and response.status_code == 204, 'Delete error occurred'


def test_delete_comments_category_byid_asso_wt_post():
    """
        Verify:
            1]Status code
            2] Category is not deleted
    """
    # Randomly generated id from the existing collection
    post = Post()
    category = CateGory()
    cat_id = post.get_category_assoc_wth_post()
    response = category.delete_comments_category_byid(cat_id)
    # Verify the status code, and the delete was not allowed
    # Do not know the error code for illegal delete. So negating a success code
    response = category.get_all_categories_from_collection()
    collection = response.json()
    assert any(d.get('id', None) == cat_id for d in collection) \
        and response.status_code != 204, 'Category associated with a post was incorrectly deleted'


# For Unit testing this module
if __name__ == "__main__":
    test_delete_comments_category_byid()
    test_delete_comments_category_byid_asso_wt_post()
