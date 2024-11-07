# PostResetLinodePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**root_pass** | **str** | The root user&#39;s password on this Linode. Linode passwords must meet a password strength score requirement that is calculated internally by the API. If the strength requirement is not met, you will receive a Password does not meet strength requirement error. | 

## Example

```python
from openapi_client.models.post_reset_linode_password_request import PostResetLinodePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostResetLinodePasswordRequest from a JSON string
post_reset_linode_password_request_instance = PostResetLinodePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(PostResetLinodePasswordRequest.to_json())

# convert the object into a dict
post_reset_linode_password_request_dict = post_reset_linode_password_request_instance.to_dict()
# create an instance of PostResetLinodePasswordRequest from a dict
post_reset_linode_password_request_from_dict = PostResetLinodePasswordRequest.from_dict(post_reset_linode_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


