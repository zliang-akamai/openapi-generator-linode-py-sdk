# PostBootLinodeInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **int** | The Linode Config ID to boot into. | [optional] 

## Example

```python
from openapi_client.models.post_boot_linode_instance_request import PostBootLinodeInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostBootLinodeInstanceRequest from a JSON string
post_boot_linode_instance_request_instance = PostBootLinodeInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PostBootLinodeInstanceRequest.to_json())

# convert the object into a dict
post_boot_linode_instance_request_dict = post_boot_linode_instance_request_instance.to_dict()
# create an instance of PostBootLinodeInstanceRequest from a dict
post_boot_linode_instance_request_from_dict = PostBootLinodeInstanceRequest.from_dict(post_boot_linode_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


