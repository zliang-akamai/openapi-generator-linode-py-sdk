# PostResetDiskPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The new root password for the OS installed on this Disk. The password must meet the complexity strength validation requirements for a strong password. | 

## Example

```python
from openapi_client.models.post_reset_disk_password_request import PostResetDiskPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostResetDiskPasswordRequest from a JSON string
post_reset_disk_password_request_instance = PostResetDiskPasswordRequest.from_json(json)
# print the JSON string representation of the object
print(PostResetDiskPasswordRequest.to_json())

# convert the object into a dict
post_reset_disk_password_request_dict = post_reset_disk_password_request_instance.to_dict()
# create an instance of PostResetDiskPasswordRequest from a dict
post_reset_disk_password_request_from_dict = PostResetDiskPasswordRequest.from_dict(post_reset_disk_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


