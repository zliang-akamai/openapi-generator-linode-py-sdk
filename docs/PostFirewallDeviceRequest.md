# PostFirewallDeviceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The entity&#39;s ID. | 
**label** | **str** | The entity&#39;s label. | [optional] [readonly] 
**type** | **str** | The entity&#39;s type. | 
**url** | **str** | The API URL path you can use to access this entity. | [optional] [readonly] 

## Example

```python
from openapi_client.models.post_firewall_device_request import PostFirewallDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostFirewallDeviceRequest from a JSON string
post_firewall_device_request_instance = PostFirewallDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PostFirewallDeviceRequest.to_json())

# convert the object into a dict
post_firewall_device_request_dict = post_firewall_device_request_instance.to_dict()
# create an instance of PostFirewallDeviceRequest from a dict
post_firewall_device_request_from_dict = PostFirewallDeviceRequest.from_dict(post_firewall_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


