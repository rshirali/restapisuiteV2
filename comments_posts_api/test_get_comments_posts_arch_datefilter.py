#!/usr/bin/python3
"""
    Test for GET /comments/posts/archive/{year}/{month}/{day}/
    Enforce that:
        Date filters only allow users to pass valid yyyy, mm, dd:
        yyyy > 1992
        1 <= mm <= 12
        1 <= dd <= 31 (or as appropriate by month)
    NOTE: Can only verify against the Successful code of 200.
          I do not have information on specific codes for invalid dates
# TODO: Perform exhaustive testing on combinations of dates for month and day including leap year.
"""
from service_layer.post import Post


def test_get_comments_posts_arch_datefilter_yyyy():
    """
        Verify status code and content of the response.
    """
    # Invalid year
    yr = 1991

    post = Post()
    response = post.get_archived_post(yr)
    assert response.status_code != 200, 'yyyy > 1992 requirement not enforced'


def test_get_comments_posts_arch_datefilter_mm():
    """
        Verify status code and content of the response.
    """

    yr = 2019
    mn = 13  # Invalid month (1 <= mm <= 12)

    post = Post()
    response = post.get_archived_post(yr, mn)
    assert response.status_code != 200, 'Invalid month'


def test_get_comments_posts_arch_datefilter_day():
    """
        Verify status code and content of the response.
    """

    yr = 2019
    mn = 2
    dy = 32  # Invalid day (1 <= dd <= 31)
    post = Post()
    response = post.get_archived_post(yr, mn, dy)
    print(response.status_code)
    assert response.status_code != 200, 'invalid day'


# For Unit testing this module
if __name__ == "__main__":
    test_get_comments_posts_arch_datefilter_yyyy()
    test_get_comments_posts_arch_datefilter_mm()
    test_get_comments_posts_arch_datefilter_day()

