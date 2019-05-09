#!/usr/bin/python3
"""
Test GET /comments/posts/
    1] Get all post
    2] Get post by post id
"""
import random
from service_layer.post import Post


def test_get_comments_all_posts():
    """
    Verify status code and content of the response.
    """
    post = Post()
    payload = {'page': 1, bool: 'false', 'per_page': 10}  # Default setting
    response = post.get_comments_all_posts(payload)
    collection = response.json()
    # Verifying a record (randomly) from the collection returned
    random_index = (random.randrange(len(collection['items'])))
    id_of_random_index = collection['items'][random_index]['id']
    assert any(d.get('id', None) == id_of_random_index for d in collection["items"]) \
        and response.status_code == 200, 'A record was not returned'


def test_get_comments_post_byid():
    """
    Verify status code and content of the response.
    """
    post = Post()
    post_id = post.get_arandm_post_from_collection()['id']
    response = post.get_comments_posts_byid(post_id)
    comment_record = response.json()
    # Verify the ID matches the id from the record
    assert comment_record.get('id', None) == post_id \
        and response.status_code == 200, 'Failed to retrieve the post record from the collection'


# For Unit testing this module
if __name__ == "__main__":
    test_get_comments_all_posts()
    test_get_comments_all_posts()
