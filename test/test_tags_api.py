# coding: utf-8

"""
    Linode API

    [Read the API documentation](https://techdocs.akamai.com/linode-api/reference/api).

    The version of the OpenAPI document: 4.189.2
    Contact: support@linode.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.tags_api import TagsApi


class TestTagsApi(unittest.TestCase):
    """TagsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = TagsApi()

    def tearDown(self) -> None:
        pass

    def test_delete_ag(self) -> None:
        """Test case for delete_ag

        Delete a tag
        """
        pass

    def test_get_tagged_objects(self) -> None:
        """Test case for get_tagged_objects

        List tagged objects
        """
        pass

    def test_get_tags(self) -> None:
        """Test case for get_tags

        List tags
        """
        pass

    def test_post_tag(self) -> None:
        """Test case for post_tag

        Create a tag
        """
        pass


if __name__ == '__main__':
    unittest.main()