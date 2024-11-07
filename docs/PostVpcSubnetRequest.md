# PostVpcSubnetRequest

VPC Subnet Create request object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ipv4** | **str** | IPv4 range in CIDR canonical form.  - The range must belong to a private address space as defined in [RFC1918](https://datatracker.ietf.org/doc/html/rfc1918). - Allowed prefix lengths: 1-29. - The range must not overlap with 192.168.128.0/17. - The range must not overlap with other Subnets on the same VPC. | 
**label** | **str** | The VPC Subnet&#39;s label, for display purposes only.  - Must be unique among the VPC&#39;s Subnets. - Can only contain ASCII letters, numbers, and hyphens (&#x60;-&#x60;). You can&#39;t use two consecutive hyphens (&#x60;--&#x60;). | 

## Example

```python
from openapi_client.models.post_vpc_subnet_request import PostVpcSubnetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVpcSubnetRequest from a JSON string
post_vpc_subnet_request_instance = PostVpcSubnetRequest.from_json(json)
# print the JSON string representation of the object
print(PostVpcSubnetRequest.to_json())

# convert the object into a dict
post_vpc_subnet_request_dict = post_vpc_subnet_request_instance.to_dict()
# create an instance of PostVpcSubnetRequest from a dict
post_vpc_subnet_request_from_dict = PostVpcSubnetRequest.from_dict(post_vpc_subnet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


