#!/usr/bin/python3
"""
   Test for POST /comments/posts/
    Enforce that:
        A post’s publication date is valid.
        Test for a date > today
"""
from datetime import date, timedelta
from service_layer.post import Post


HEADERS = {'content-type': 'application/json'}


def test_post_comm_posts_pubdatevalid():
    """
        Verify:
        1]The Status Code of Success is not returned
        2]Record is not added to the collection
    """
    post = Post()
    # Requires an existing Category id
    cat_id = post.get_category_assoc_wth_post()
    # A date of tomorrow
    future_date = str(date.today() + timedelta(days=1)) + 'T15:56:29.200201Z'
    # Payload->pub_date contains a date of tomorrow
    payload = {
        "title": "A post’s publication date is valid.",
        "body": "Testing with a date greater than today",
        "pub_date": future_date,
        "category_id": cat_id,
        "category": "Meditation"
    }

    # sending POST request and saving response as response object
    response = post.post_comments_posts(payload, headers=HEADERS)
    assert response.status_code != 201, "Date/time other than today's should not be allowed"

    # Verify the POST did not add the record by verifying the
    # absence of the ID in the collection
    collection = post.get_all_posts_from_collection()
    assert not any(d.get('id', None) == payload['title'] for d in collection["items"]) \
        and response.status_code != 201,\
        "Date/time other than today's should not be allowed. " \
        "Record incorrectly added to collection for an invalid date"


# For Unit testing this module
if __name__ == "__main__":
    test_post_comm_posts_pubdatevalid()
