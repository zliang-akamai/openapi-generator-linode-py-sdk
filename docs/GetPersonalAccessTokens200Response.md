# GetPersonalAccessTokens200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetPersonalAccessTokens200ResponseDataInner]**](GetPersonalAccessTokens200ResponseDataInner.md) |  | [optional] 
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_personal_access_tokens200_response import GetPersonalAccessTokens200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersonalAccessTokens200Response from a JSON string
get_personal_access_tokens200_response_instance = GetPersonalAccessTokens200Response.from_json(json)
# print the JSON string representation of the object
print(GetPersonalAccessTokens200Response.to_json())

# convert the object into a dict
get_personal_access_tokens200_response_dict = get_personal_access_tokens200_response_instance.to_dict()
# create an instance of GetPersonalAccessTokens200Response from a dict
get_personal_access_tokens200_response_from_dict = GetPersonalAccessTokens200Response.from_dict(get_personal_access_tokens200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


