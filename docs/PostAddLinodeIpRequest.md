# PostAddLinodeIpRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**public** | **bool** | Whether to create a public or private IPv4 address. | 
**type** | **str** | The type of address you are allocating. Only IPv4 addresses may be allocated through this operation. | 

## Example

```python
from openapi_client.models.post_add_linode_ip_request import PostAddLinodeIpRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostAddLinodeIpRequest from a JSON string
post_add_linode_ip_request_instance = PostAddLinodeIpRequest.from_json(json)
# print the JSON string representation of the object
print(PostAddLinodeIpRequest.to_json())

# convert the object into a dict
post_add_linode_ip_request_dict = post_add_linode_ip_request_instance.to_dict()
# create an instance of PostAddLinodeIpRequest from a dict
post_add_linode_ip_request_from_dict = PostAddLinodeIpRequest.from_dict(post_add_linode_ip_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


