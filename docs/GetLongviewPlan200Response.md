# GetLongviewPlan200Response

A Longview Subscription represents a tier of Longview service you can subscribe to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clients_included** | **int** | The number of Longview Clients that may be created with this Subscription tier. | [optional] [readonly] 
**id** | **str** | The unique ID of this Subscription tier. | [optional] [readonly] 
**label** | **str** | A display name for this Subscription tier. | [optional] [readonly] 
**price** | [**GetLongviewPlan200ResponsePrice**](GetLongviewPlan200ResponsePrice.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_longview_plan200_response import GetLongviewPlan200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLongviewPlan200Response from a JSON string
get_longview_plan200_response_instance = GetLongviewPlan200Response.from_json(json)
# print the JSON string representation of the object
print(GetLongviewPlan200Response.to_json())

# convert the object into a dict
get_longview_plan200_response_dict = get_longview_plan200_response_instance.to_dict()
# create an instance of GetLongviewPlan200Response from a dict
get_longview_plan200_response_from_dict = GetLongviewPlan200Response.from_dict(get_longview_plan200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


