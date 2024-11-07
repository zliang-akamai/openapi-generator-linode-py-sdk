# GetNotifications200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetNotifications200ResponseDataInner]**](GetNotifications200ResponseDataInner.md) |  | [optional] 
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_notifications200_response import GetNotifications200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetNotifications200Response from a JSON string
get_notifications200_response_instance = GetNotifications200Response.from_json(json)
# print the JSON string representation of the object
print(GetNotifications200Response.to_json())

# convert the object into a dict
get_notifications200_response_dict = get_notifications200_response_instance.to_dict()
# create an instance of GetNotifications200Response from a dict
get_notifications200_response_from_dict = GetNotifications200Response.from_dict(get_notifications200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


