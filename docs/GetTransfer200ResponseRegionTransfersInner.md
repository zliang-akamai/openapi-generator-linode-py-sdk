# GetTransfer200ResponseRegionTransfersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **int** | The amount of your transfer pool that is billable this billing cycle for this Region. | [optional] [readonly] 
**id** | **str** | The Region ID for this network utilization data. | [optional] 
**quota** | **int** | The amount of network usage allowed this billing cycle for this Region. | [optional] [readonly] 
**used** | **int** | The amount of network usage you have used this billing cycle for this Region. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_transfer200_response_region_transfers_inner import GetTransfer200ResponseRegionTransfersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTransfer200ResponseRegionTransfersInner from a JSON string
get_transfer200_response_region_transfers_inner_instance = GetTransfer200ResponseRegionTransfersInner.from_json(json)
# print the JSON string representation of the object
print(GetTransfer200ResponseRegionTransfersInner.to_json())

# convert the object into a dict
get_transfer200_response_region_transfers_inner_dict = get_transfer200_response_region_transfers_inner_instance.to_dict()
# create an instance of GetTransfer200ResponseRegionTransfersInner from a dict
get_transfer200_response_region_transfers_inner_from_dict = GetTransfer200ResponseRegionTransfersInner.from_dict(get_transfer200_response_region_transfers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


