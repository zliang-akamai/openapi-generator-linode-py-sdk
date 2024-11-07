# PutVpcSubnetRequest

A VPC Subnet Update request object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The VPC Subnet&#39;s label, for display purposes only.  - Must be unique among the VPC&#39;s Subnets. - Can only contain ASCII letters, numbers, and hyphens (&#x60;-&#x60;). You can&#39;t use two consecutive hyphens (&#x60;--&#x60;). | [optional] 

## Example

```python
from openapi_client.models.put_vpc_subnet_request import PutVpcSubnetRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutVpcSubnetRequest from a JSON string
put_vpc_subnet_request_instance = PutVpcSubnetRequest.from_json(json)
# print the JSON string representation of the object
print(PutVpcSubnetRequest.to_json())

# convert the object into a dict
put_vpc_subnet_request_dict = put_vpc_subnet_request_instance.to_dict()
# create an instance of PutVpcSubnetRequest from a dict
put_vpc_subnet_request_from_dict = PutVpcSubnetRequest.from_dict(put_vpc_subnet_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


