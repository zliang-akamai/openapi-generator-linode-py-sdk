# Transfer

An object representing your network utilization for the current month, in Gigabytes.  Certain Regions have separate utilization quotas and rates. For Region-specific network utilization data, see `region_transfers`.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billable** | **int** | The amount of your transfer pool that is billable this billing cycle. | [optional] [readonly] 
**quota** | **int** | The amount of network usage allowed this billing cycle. | [optional] [readonly] 
**region_transfers** | [**List[GetTransfer200ResponseRegionTransfersInner]**](GetTransfer200ResponseRegionTransfersInner.md) |  | [optional] 
**used** | **int** | The amount of network usage you have used this billing cycle. | [optional] [readonly] 

## Example

```python
from openapi_client.models.transfer import Transfer

# TODO update the JSON string below
json = "{}"
# create an instance of Transfer from a JSON string
transfer_instance = Transfer.from_json(json)
# print the JSON string representation of the object
print(Transfer.to_json())

# convert the object into a dict
transfer_dict = transfer_instance.to_dict()
# create an instance of Transfer from a dict
transfer_from_dict = Transfer.from_dict(transfer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


