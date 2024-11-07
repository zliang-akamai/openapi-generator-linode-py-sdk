# PostRescueLinodeInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**devices** | [**PostRescueLinodeInstanceRequestDevices**](PostRescueLinodeInstanceRequestDevices.md) |  | [optional] 

## Example

```python
from openapi_client.models.post_rescue_linode_instance_request import PostRescueLinodeInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostRescueLinodeInstanceRequest from a JSON string
post_rescue_linode_instance_request_instance = PostRescueLinodeInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PostRescueLinodeInstanceRequest.to_json())

# convert the object into a dict
post_rescue_linode_instance_request_dict = post_rescue_linode_instance_request_instance.to_dict()
# create an instance of PostRescueLinodeInstanceRequest from a dict
post_rescue_linode_instance_request_from_dict = PostRescueLinodeInstanceRequest.from_dict(post_rescue_linode_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


