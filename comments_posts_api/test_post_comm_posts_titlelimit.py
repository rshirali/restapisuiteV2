#!/usr/bin/python3
"""
   Test for POST /comments/posts/
    Enforce that:
    A post’s title does not exceed 100 characters
"""
from service_layer.post import Post

HEADERS = {'content-type': 'application/json'}


def test_post_comm_posts_titlelimit():
    """
        Verify:
        1]The Status Code of Success is not in the response
        2]Record is not added to the collection.  A post title does not exceed 100 characters
    """
    post = Post()
    # Requires an existing Category id
    cat_id = post.get_category_assoc_wth_post()
    # Data to be sent to api
    payload = {
        "title": "iqueacrossallexistingcategoriesinthesystemcategor"
                 "ynameisuniqueacrossallexistingcategoriesinthesnot "
                 "exceed 100 characters",
        "body": "This dramatic retelling of the Pearl Harbor attack details everything "
                "in the days that led up to that tragic moment in American history.",
        "pub_date": "2016-06-11T15:56:29.200201",
        "category_id": cat_id,
        "category": "Meditation"
    }
    # sending POST request and saving response as response object
    response = post.post_comments_posts(payload, headers=HEADERS)
    # Verify the POST did not add the record by verifying the
    # absence of the ID in the collection
    collection = post.get_all_posts_from_collection()
    assert not any(d.get('title', None) == payload['title'] for d in collection["items"]) \
        and response.status_code != 201, \
        'Title string limit > 100. Record incorrectly added to collection'


# For Unit testing this module
if __name__ == "__main__":
    test_post_comm_posts_titlelimit()
