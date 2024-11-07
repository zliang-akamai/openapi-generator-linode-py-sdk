# GetVolumeTypes200ResponseDataInner

Returns collection of volume types and prices, including any region-specific rates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID representing the volume type. | [optional] [readonly] 
**label** | **str** | The volume type label is for display purposes only. | [optional] [readonly] 
**price** | [**GetVolumeTypes200ResponseDataInnerPrice**](GetVolumeTypes200ResponseDataInnerPrice.md) |  | [optional] 
**region_prices** | [**List[GetLkeTypes200ResponseDataInnerRegionPricesInner]**](GetLkeTypes200ResponseDataInnerRegionPricesInner.md) |  | [optional] 
**transfer** | **int** | The monthly outbound transfer amount, in MB. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_volume_types200_response_data_inner import GetVolumeTypes200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetVolumeTypes200ResponseDataInner from a JSON string
get_volume_types200_response_data_inner_instance = GetVolumeTypes200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetVolumeTypes200ResponseDataInner.to_json())

# convert the object into a dict
get_volume_types200_response_data_inner_dict = get_volume_types200_response_data_inner_instance.to_dict()
# create an instance of GetVolumeTypes200ResponseDataInner from a dict
get_volume_types200_response_data_inner_from_dict = GetVolumeTypes200ResponseDataInner.from_dict(get_volume_types200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


