# PostManagedCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | This Credential&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The unique label for this Credential. This is for display purposes only. | 
**last_decrypted** | **datetime** | The date this Credential was last decrypted by a member of Linode special forces. | [optional] [readonly] 
**password** | **str** | The password to use when accessing the Managed Service. | 
**username** | **str** | The username to use when accessing the Managed Service. | [optional] 

## Example

```python
from openapi_client.models.post_managed_credential_request import PostManagedCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostManagedCredentialRequest from a JSON string
post_managed_credential_request_instance = PostManagedCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(PostManagedCredentialRequest.to_json())

# convert the object into a dict
post_managed_credential_request_dict = post_managed_credential_request_instance.to_dict()
# create an instance of PostManagedCredentialRequest from a dict
post_managed_credential_request_from_dict = PostManagedCredentialRequest.from_dict(post_managed_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


