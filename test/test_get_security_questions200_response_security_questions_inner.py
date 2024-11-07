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

from openapi_client.models.get_security_questions200_response_security_questions_inner import GetSecurityQuestions200ResponseSecurityQuestionsInner

class TestGetSecurityQuestions200ResponseSecurityQuestionsInner(unittest.TestCase):
    """GetSecurityQuestions200ResponseSecurityQuestionsInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetSecurityQuestions200ResponseSecurityQuestionsInner:
        """Test GetSecurityQuestions200ResponseSecurityQuestionsInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetSecurityQuestions200ResponseSecurityQuestionsInner`
        """
        model = GetSecurityQuestions200ResponseSecurityQuestionsInner()
        if include_optional:
            return GetSecurityQuestions200ResponseSecurityQuestionsInner(
                id = 1,
                question = 'In what city were you born?',
                response = 'Gotham City'
            )
        else:
            return GetSecurityQuestions200ResponseSecurityQuestionsInner(
        )
        """

    def testGetSecurityQuestions200ResponseSecurityQuestionsInner(self):
        """Test GetSecurityQuestions200ResponseSecurityQuestionsInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
