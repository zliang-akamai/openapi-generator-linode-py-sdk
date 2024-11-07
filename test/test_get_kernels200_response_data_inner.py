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

from openapi_client.models.get_kernels200_response_data_inner import GetKernels200ResponseDataInner

class TestGetKernels200ResponseDataInner(unittest.TestCase):
    """GetKernels200ResponseDataInner unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GetKernels200ResponseDataInner:
        """Test GetKernels200ResponseDataInner
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GetKernels200ResponseDataInner`
        """
        model = GetKernels200ResponseDataInner()
        if include_optional:
            return GetKernels200ResponseDataInner(
                architecture = 'x86_64',
                built = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                deprecated = False,
                id = 'linode/latest-64bit',
                kvm = True,
                label = 'Latest 64 bit (4.15.7-x86_64-linode102)',
                pvops = False,
                version = '4.15.7'
            )
        else:
            return GetKernels200ResponseDataInner(
        )
        """

    def testGetKernels200ResponseDataInner(self):
        """Test GetKernels200ResponseDataInner"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
