# PostManagedCredentialUsernamePasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | The password to use when accessing the Managed Service. | 
**username** | **str** | The username to use when accessing the Managed Service. | [optional] 

## Example

```python
from openapi_client.models.post_managed_credential_username_password_request import PostManagedCredentialUsernamePasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostManagedCredentialUsernamePasswordRequest from a JSON string
post_managed_credential_username_password_request_instance = PostManagedCredentialUsernamePasswordRequest.from_json(json)
# print the JSON string representation of the object
print(PostManagedCredentialUsernamePasswordRequest.to_json())

# convert the object into a dict
post_managed_credential_username_password_request_dict = post_managed_credential_username_password_request_instance.to_dict()
# create an instance of PostManagedCredentialUsernamePasswordRequest from a dict
post_managed_credential_username_password_request_from_dict = PostManagedCredentialUsernamePasswordRequest.from_dict(post_managed_credential_username_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


