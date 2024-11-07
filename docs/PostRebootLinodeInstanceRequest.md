# PostRebootLinodeInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **int** | The Linode Config ID to reboot into.  If null or omitted, the last booted config will be used.  If there was no last booted config and this Linode only has one config, it will be used.  If a config cannot be determined, an error will be returned. | [optional] 

## Example

```python
from openapi_client.models.post_reboot_linode_instance_request import PostRebootLinodeInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRebootLinodeInstanceRequest from a JSON string
post_reboot_linode_instance_request_instance = PostRebootLinodeInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PostRebootLinodeInstanceRequest.to_json())

# convert the object into a dict
post_reboot_linode_instance_request_dict = post_reboot_linode_instance_request_instance.to_dict()
# create an instance of PostRebootLinodeInstanceRequest from a dict
post_reboot_linode_instance_request_from_dict = PostRebootLinodeInstanceRequest.from_dict(post_reboot_linode_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


