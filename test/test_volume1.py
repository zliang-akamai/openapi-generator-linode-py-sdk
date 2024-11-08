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

from openapi_client.models.volume1 import Volume1

class TestVolume1(unittest.TestCase):
    """Volume1 unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Volume1:
        """Test Volume1
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Volume1`
        """
        model = Volume1()
        if include_optional:
            return Volume1(
                created = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                encryption = 'enabled',
                filesystem_path = '/dev/disk/by-id/scsi-0Linode_Volume_my-volume',
                hardware_type = 'nvme',
                id = 12345,
                label = 'my-volume',
                linode_id = 12346,
                linode_label = 'linode123',
                region = 'us-east',
                size = 30,
                status = 'active',
                tags = ["example tag","another example"],
                updated = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return Volume1(
        )
        """

    def testVolume1(self):
        """Test Volume1"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
