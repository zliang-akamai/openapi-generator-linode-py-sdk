# GetAccountDefaultResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[GetAccountDefaultResponseErrorsInner]**](GetAccountDefaultResponseErrorsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_account_default_response import GetAccountDefaultResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountDefaultResponse from a JSON string
get_account_default_response_instance = GetAccountDefaultResponse.from_json(json)
# print the JSON string representation of the object
print(GetAccountDefaultResponse.to_json())

# convert the object into a dict
get_account_default_response_dict = get_account_default_response_instance.to_dict()
# create an instance of GetAccountDefaultResponse from a dict
get_account_default_response_from_dict = GetAccountDefaultResponse.from_dict(get_account_default_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


