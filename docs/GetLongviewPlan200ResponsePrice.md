# GetLongviewPlan200ResponsePrice

Pricing information about this Subscription tier.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hourly** | **float** | The hourly price, in US dollars, for this Subscription tier. | [optional] [readonly] 
**monthly** | **float** | The maximum monthly price in US Dollars for this Subscription tier. You will never be charged more than this amount per month for this subscription. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_longview_plan200_response_price import GetLongviewPlan200ResponsePrice

# TODO update the JSON string below
json = "{}"
# create an instance of GetLongviewPlan200ResponsePrice from a JSON string
get_longview_plan200_response_price_instance = GetLongviewPlan200ResponsePrice.from_json(json)
# print the JSON string representation of the object
print(GetLongviewPlan200ResponsePrice.to_json())

# convert the object into a dict
get_longview_plan200_response_price_dict = get_longview_plan200_response_price_instance.to_dict()
# create an instance of GetLongviewPlan200ResponsePrice from a dict
get_longview_plan200_response_price_from_dict = GetLongviewPlan200ResponsePrice.from_dict(get_longview_plan200_response_price_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


