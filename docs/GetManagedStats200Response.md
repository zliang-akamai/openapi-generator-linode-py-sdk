# GetManagedStats200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetManagedStats200ResponseData**](GetManagedStats200ResponseData.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_managed_stats200_response import GetManagedStats200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedStats200Response from a JSON string
get_managed_stats200_response_instance = GetManagedStats200Response.from_json(json)
# print the JSON string representation of the object
print(GetManagedStats200Response.to_json())

# convert the object into a dict
get_managed_stats200_response_dict = get_managed_stats200_response_instance.to_dict()
# create an instance of GetManagedStats200Response from a dict
get_managed_stats200_response_from_dict = GetManagedStats200Response.from_dict(get_managed_stats200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


