# PostAllocateIpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**linode_id** | **int** | The ID of a Linode you have access to that this address will be allocated to. | 
**public** | **bool** | Whether to create a public or private IPv4 address. | 
**type** | **str** | The type of address you are requesting. Only IPv4 addresses may be allocated through this operation. | 

## Example

```python
from openapi_client.models.post_allocate_ip_request import PostAllocateIpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAllocateIpRequest from a JSON string
post_allocate_ip_request_instance = PostAllocateIpRequest.from_json(json)
# print the JSON string representation of the object
print(PostAllocateIpRequest.to_json())

# convert the object into a dict
post_allocate_ip_request_dict = post_allocate_ip_request_instance.to_dict()
# create an instance of PostAllocateIpRequest from a dict
post_allocate_ip_request_from_dict = PostAllocateIpRequest.from_dict(post_allocate_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


