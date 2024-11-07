# PostVpcRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subnets** | [**List[GetVpcs200ResponseAllOfDataInnerSubnetsInner]**](GetVpcs200ResponseAllOfDataInnerSubnetsInner.md) | A list of subnets associated with the VPC. | [optional] 
**created** | **datetime** | The date-time of VPC creation. | [optional] [readonly] 
**description** | **str** | A written description to help distinguish the VPC. | [optional] [default to '']
**id** | **int** | The unique ID of the VPC. | [optional] [readonly] 
**label** | **str** | The VPC&#39;s label, for display purposes only.  - Needs to be unique among the Account&#39;s VPCs. - Can only contain ASCII letters, numbers, and hyphens (&#x60;-&#x60;). You can&#39;t use two consecutive hyphens (&#x60;--&#x60;). | 
**region** | **str** | The Region for the VPC. | 
**updated** | **datetime** | The date-time of the most recent VPC update. | [optional] [readonly] 

## Example

```python
from openapi_client.models.post_vpc_request import PostVpcRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostVpcRequest from a JSON string
post_vpc_request_instance = PostVpcRequest.from_json(json)
# print the JSON string representation of the object
print(PostVpcRequest.to_json())

# convert the object into a dict
post_vpc_request_dict = post_vpc_request_instance.to_dict()
# create an instance of PostVpcRequest from a dict
post_vpc_request_from_dict = PostVpcRequest.from_dict(post_vpc_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


