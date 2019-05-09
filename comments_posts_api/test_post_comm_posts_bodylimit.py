#!/usr/bin/python3
"""
   Test for POST /comments/posts/
    Enforce that:
        A post’s body does not exceed 1000 characters.
"""
from service_layer.post import Post

HEADERS = {'content-type': 'application/json'}


def test_post_comm_posts_bodylimit():
    """
        Verify:
        1]The Status Code of Success is not in the response
        2]Record is not added to the collection
    """

    post = Post()
    # Requires an existing Category id
    cat_id = post.get_category_assoc_wth_post()
    # Payload->pub_date contains a date of tomorrow
    # Payload->tile contains more than 1000 characters
    payload = {
        "title": "testforbigbodygreaterthan1000chars",
        "body": "namedoesnotexceed140characters.iqueacrossallexis" \
                "tingcategoriesinthesystemcategorynameisuniqueacro"
                "ssallexistingcategoriesinthesnot exceed100characte"
                "rsiqueacrossallexistingcategoriesinthesystemcatego"
                "rynameisuniqueacrossallexistingcategoriesinthesnot"
                "exceed 100 characters namedoesnotexceed140characte"
                "rsiqueacrossallexistingcategoriesinthesystemcategor"
                "ynameisuniqueacrossallexisti",
        "pub_date": "2016-06-11T15:56:29.200201",
        "category_id": cat_id,
        "category": "Meditation"
    }

    # sending POST request and saving response as response object
    response = post.post_comments_posts(payload, headers=HEADERS)
    # assert response.status_code != 201, '< 1000 string length not enforced'

    # Verify the POST did not add the record by verifying the
    # absence of the ID in the collection
    collection = post.get_all_posts_from_collection()
    assert not any(d.get('body', None) == payload['body'] for d in collection["items"]) \
        and response.status_code != 201, \
        '< 1000 string length not enforced. Record incorrectly added to the collection'


# For Unit testing this module
if __name__ == "__main__":
    test_post_comm_posts_bodylimit()
