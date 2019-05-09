#!/usr/bin/python3
"""
Test for PUT /comments/posts/{id}
"""

from service_layer.post import Post


def test_put_comments_post_byid():
    """
    Verify status code and content of the response.
    """
    post = Post()
    cat_id = post.get_category_assoc_wth_post()
    post_id = post.get_arandm_post_from_collection()['id']
    # Data to be sent to api
    payload = {
        "id": post_id,
        "title": "Tora Tora Tora",
        "body": "This dramatic retelling of the Pearl Harbor attack details everything "
                "in the days that led up to that tragic moment in American history.",
        "pub_date": "2016-06-11T15:56:29.200201",
        "category_id": cat_id,
        "category": "Meditation"
    }
    headers = {'content-type': 'application/json'}
    # sending POST request and saving response as response object
    response = post.put_comments_post_byid(post_id=post_id, payload=payload, headers=headers)

    # Verify the PUT successfully updated the record by verifying the ID and the Title
    collection = post.get_all_posts_from_collection()
    assert any(d.get('id', None) == post_id and
               d.get('title', None) == 'Tora Tora Tora' for d in collection["items"]) \
           and response.status_code == 204


# For Unit testing this module
if __name__ == "__main__":
    test_put_comments_post_byid()
