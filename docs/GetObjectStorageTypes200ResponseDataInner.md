# GetObjectStorageTypes200ResponseDataInner

Returns collection of Object Storage types and prices, including any region-specific rates.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID representing the Object Storage type. | [optional] [readonly] 
**label** | **str** | The Object Storage type label is for display purposes only. | [optional] [readonly] 
**price** | [**GetObjectStorageTypes200ResponseDataInnerPrice**](GetObjectStorageTypes200ResponseDataInnerPrice.md) |  | [optional] 
**region_prices** | [**List[GetLkeTypes200ResponseDataInnerRegionPricesInner]**](GetLkeTypes200ResponseDataInnerRegionPricesInner.md) |  | [optional] 
**transfer** | **int** | The monthly outbound transfer amount, in MB. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_object_storage_types200_response_data_inner import GetObjectStorageTypes200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetObjectStorageTypes200ResponseDataInner from a JSON string
get_object_storage_types200_response_data_inner_instance = GetObjectStorageTypes200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetObjectStorageTypes200ResponseDataInner.to_json())

# convert the object into a dict
get_object_storage_types200_response_data_inner_dict = get_object_storage_types200_response_data_inner_instance.to_dict()
# create an instance of GetObjectStorageTypes200ResponseDataInner from a dict
get_object_storage_types200_response_data_inner_from_dict = GetObjectStorageTypes200ResponseDataInner.from_dict(get_object_storage_types200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

