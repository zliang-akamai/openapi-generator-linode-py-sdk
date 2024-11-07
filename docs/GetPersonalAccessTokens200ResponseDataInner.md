# GetPersonalAccessTokens200ResponseDataInner

A Personal Access Token is a token generated manually to access the API without going through an OAuth login.  Personal Access Tokens can have scopes just like OAuth tokens do, and are commonly used to give access to command-line tools like the Linode CLI, or when writing your own integrations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date and time this token was created. | [optional] [readonly] 
**expiry** | **datetime** | When this token will expire.  Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated.  Tokens may be created with &#x60;null&#x60; as their expiry and will never expire unless revoked. | [optional] [readonly] 
**id** | **int** | This token&#39;s unique ID, which can be used to revoke it. | [optional] [readonly] 
**label** | **str** | This token&#39;s label.  This is for display purposes only, but can be used to more easily track what you&#39;re using each token for. | [optional] 
**scopes** | **str** | The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the [Linode CLI](https://github.com/linode/linode-cli), require tokens with access to &#x60;*&#x60;. Tokens with more restrictive scopes are generally more secure. | [optional] [readonly] 
**token** | **str** | The token used to access the API.  When the token is created, the full token is returned here.  Otherwise, only the first 16 characters are returned. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_personal_access_tokens200_response_data_inner import GetPersonalAccessTokens200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersonalAccessTokens200ResponseDataInner from a JSON string
get_personal_access_tokens200_response_data_inner_instance = GetPersonalAccessTokens200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetPersonalAccessTokens200ResponseDataInner.to_json())

# convert the object into a dict
get_personal_access_tokens200_response_data_inner_dict = get_personal_access_tokens200_response_data_inner_instance.to_dict()
# create an instance of GetPersonalAccessTokens200ResponseDataInner from a dict
get_personal_access_tokens200_response_data_inner_from_dict = GetPersonalAccessTokens200ResponseDataInner.from_dict(get_personal_access_tokens200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


