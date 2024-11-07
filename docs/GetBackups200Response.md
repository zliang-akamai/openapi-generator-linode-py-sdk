# GetBackups200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**automatic** | [**List[GetBackups200ResponseAutomaticInner]**](GetBackups200ResponseAutomaticInner.md) |  | [optional] 
**snapshot** | [**GetBackups200ResponseSnapshot**](GetBackups200ResponseSnapshot.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_backups200_response import GetBackups200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetBackups200Response from a JSON string
get_backups200_response_instance = GetBackups200Response.from_json(json)
# print the JSON string representation of the object
print(GetBackups200Response.to_json())

# convert the object into a dict
get_backups200_response_dict = get_backups200_response_instance.to_dict()
# create an instance of GetBackups200Response from a dict
get_backups200_response_from_dict = GetBackups200Response.from_dict(get_backups200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


