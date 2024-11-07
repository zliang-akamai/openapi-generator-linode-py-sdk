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

from openapi_client.models.added_get_enrolled_beta_programs200 import AddedGetEnrolledBetaPrograms200

class TestAddedGetEnrolledBetaPrograms200(unittest.TestCase):
    """AddedGetEnrolledBetaPrograms200 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AddedGetEnrolledBetaPrograms200:
        """Test AddedGetEnrolledBetaPrograms200
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AddedGetEnrolledBetaPrograms200`
        """
        model = AddedGetEnrolledBetaPrograms200()
        if include_optional:
            return AddedGetEnrolledBetaPrograms200(
                page = 1,
                pages = 1,
                results = 1,
                data = [
                    openapi_client.models.added_get_enrolled_beta_programs_200_all_of_data.added_get_enrolled_beta_programs_200_allOf_data(
                        description = 'This is an open public beta for an example feature.', 
                        ended = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        enrolled = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        id = 'example_open', 
                        label = 'Example Open Beta', 
                        started = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), )
                    ]
            )
        else:
            return AddedGetEnrolledBetaPrograms200(
        )
        """

    def testAddedGetEnrolledBetaPrograms200(self):
        """Test AddedGetEnrolledBetaPrograms200"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
