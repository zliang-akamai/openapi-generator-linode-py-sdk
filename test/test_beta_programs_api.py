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

from openapi_client.api.beta_programs_api import BetaProgramsApi


class TestBetaProgramsApi(unittest.TestCase):
    """BetaProgramsApi unit test stubs"""

    def setUp(self) -> None:
        self.api = BetaProgramsApi()

    def tearDown(self) -> None:
        pass

    def test_get_beta_program(self) -> None:
        """Test case for get_beta_program

        Get a Beta program
        """
        pass

    def test_get_beta_programs(self) -> None:
        """Test case for get_beta_programs

        List Beta programs
        """
        pass


if __name__ == '__main__':
    unittest.main()
