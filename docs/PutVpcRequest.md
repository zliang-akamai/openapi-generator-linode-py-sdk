# PutVpcRequest

A VPC Update request object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | A written description to help distinguish the VPC. | [optional] [default to '']
**label** | **str** | The VPC&#39;s label, for display purposes only.  - Needs to be unique among the Account&#39;s VPCs. - Can only contain ASCII letters, numbers, and hyphens (&#x60;-&#x60;). You can&#39;t use two consecutive hyphens (&#x60;--&#x60;). | [optional] 

## Example

```python
from openapi_client.models.put_vpc_request import PutVpcRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutVpcRequest from a JSON string
put_vpc_request_instance = PutVpcRequest.from_json(json)
# print the JSON string representation of the object
print(PutVpcRequest.to_json())

# convert the object into a dict
put_vpc_request_dict = put_vpc_request_instance.to_dict()
# create an instance of PutVpcRequest from a dict
put_vpc_request_from_dict = PutVpcRequest.from_dict(put_vpc_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


