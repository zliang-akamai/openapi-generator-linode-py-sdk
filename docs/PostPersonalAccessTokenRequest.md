# PostPersonalAccessTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **datetime** | When this token should be valid until.  If omitted, the new token will be valid until it is manually revoked. | [optional] 
**label** | **str** | This token&#39;s label.  This is for display purposes only, but can be used to more easily track what you&#39;re using each token for. | [optional] 
**scopes** | **str** | The access [scopes](https://techdocs.akamai.com/linode-api/reference/get-started#oauth-reference) to grant to the created token. These cannot be changed after creation, and may not exceed the scopes of the acting token.  If omitted or entered with a wildcard character (&#x60;*&#x60;), the new token will have the same scopes as the acting token.  Multiple scopes are separated by a space character (&#x60; &#x60;).  For example, &#x60;linodes:read_write account:read_only&#x60;. | [optional] 

## Example

```python
from openapi_client.models.post_personal_access_token_request import PostPersonalAccessTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPersonalAccessTokenRequest from a JSON string
post_personal_access_token_request_instance = PostPersonalAccessTokenRequest.from_json(json)
# print the JSON string representation of the object
print(PostPersonalAccessTokenRequest.to_json())

# convert the object into a dict
post_personal_access_token_request_dict = post_personal_access_token_request_instance.to_dict()
# create an instance of PostPersonalAccessTokenRequest from a dict
post_personal_access_token_request_from_dict = PostPersonalAccessTokenRequest.from_dict(post_personal_access_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


