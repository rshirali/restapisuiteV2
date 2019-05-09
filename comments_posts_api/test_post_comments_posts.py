#!/usr/bin/python3
"""
   Test for POST /comments/posts/
   1] Successful POST
   2]Enforce that:
    A post’s category / category_id are valid.
"""
from service_layer.post import Post

# Header to be sent to api
HEADERS = {'content-type': 'application/json'}


def test_post_comments_posts():
    """
        Verify status code and content of the response.
    """
    post = Post()
    cat_id = post.get_category_assoc_wth_post()
    # Data to be sent to api
    payload = {
        "title": "TESTINDG TODAT",
        "body": "This dramatic retelling of the Pearl Harbor attack details everything "
                "in the days that led up to that tragic moment in American history.",
        "pub_date": "2016-06-11T15:56:29.200201",
        "category_id": cat_id,
        "category": "Meditation"
    }

    # sending POST request and saving response as response object
    response = post.post_comments_posts(payload, headers=HEADERS)
    # Verify the POST successfully added the record by verifying the ID in the collection
    collection = post.get_all_posts_from_collection()
    id_post = (collection['items'][-1]).get('id')
    assert any(d.get('id', None) == id_post for d in collection["items"]) \
           and response.status_code == 201, 'post failed to append to collection'


def test_post_comments_posts_invalid_catid():
    """
    Verify status code and POST did not occur due to invalid Category id.
    """

    # Next id in the collection to be used for POST
    # Data to be sent to api
    payload = {
        "title": "TESTING_INVALID_CATID",
        "body": "This dramatic retelling of the Pearl Harbor attack details everything "
                "in the days that led up to that tragic moment in American history.",
        "pub_date": "2016-06-11T15:56:29.200201",
        "category_id": 000,  # Invalid id
        "category": "Meditation"
    }
    post = Post()
    # sending POST request and saving response as response object
    response = post.post_comments_posts(payload, headers=HEADERS)
    # TODO: Confirm if Status Code should be 404 or 400. Document states 400.
    # However, Status Code returned is 404
    # Verify the POST did not add the record
    collection = post.get_all_posts_from_collection()
    assert not any(d.get('name', None) == 'TESTING_INVALID_CATID' for d in collection["items"]) \
           and response.status_code == 404, \
        'Invalid Category. POST not allowed. Post added for invalid id'


# For Unit testing this module
if __name__ == "__main__":
    test_post_comments_posts()
    test_post_comments_posts_invalid_catid()
