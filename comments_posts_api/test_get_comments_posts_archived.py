#!/usr/bin/python3
"""
Test for GET /comments/posts/archive/{year}/
Test for GET /comments/posts/archive/{year}/{month}
Test for GET /comments/posts/archive/{year}/{month}/{day}/
Returns list of posts for the time period
"""
from service_layer.post import Post


def test_get_comments_posts_arcbyyear():
    """
        Verify status code and content of the response.
    """
    post = Post()
    response = post.get_archived_post(2019)
    assert response.status_code == 200, 'Error retrieving posts'
    # TODO: Perform exhaustive validation of the data returned
    # For example, verifying records outside of the date range
    # were incorrectly returned


def test_get_comments_posts_arch_by_yrmn():
    """
        Verify status code and content of the response.
    """
    post = Post()
    response = post.get_archived_post(2019, mn=5)
    assert response.status_code == 200, 'Error retrieving posts'
    # TODO: Perform exhaustive validation of the data returned
    # For example, verifying records outside the date range
    # were incorrectly returned


def test_get_comments_posts_arch_by_yrmndy():
    """
        Verify status code and content of the response.
    """
    post = Post()
    response = post.get_archived_post(2019, mn=5, dy=5)
    assert response.status_code == 200, 'Error retrieving posts'
    """
    TODO: Perform exhaustive validation of the data returned
    For example, verifying records outside the date range
    were incorrectly returned
    """


# For Unit testing this module
if __name__ == "__main__":
    test_get_comments_posts_arcbyyear()
    test_get_comments_posts_arch_by_yrmn()
    test_get_comments_posts_arch_by_yrmndy()

