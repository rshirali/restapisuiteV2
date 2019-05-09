#!/usr/bin/python3
"""
Test for DELETE /comments/posts/{id}
"""
from service_layer.post import Post


def test_delete_comments_post_byid():
    """
    Verify:
    1]Status code for delete
    2] Post was delete from the collection
    """
    post = Post()
    # Select a post to delete
    a_post_id = post.get_arandm_post_from_collection()['id']
    response = post.delete_comments_post_byid(a_post_id)
    # Verify the deleted record does not exit in the collection
    collection = post.get_all_posts_from_collection()
    assert not any(d.get('id', None) == a_post_id for d in collection["items"]) and \
           response.status_code == 204, 'failed to delete the record'


# For Unit testing this module
if __name__ == "__main__":
    test_delete_comments_post_byid()

