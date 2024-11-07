# GetManagedStats200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cpu** | [**List[StatsAvailableCpuInner]**](StatsAvailableCpuInner.md) | CPU usage stats from the last 24 hours. | [optional] 
**disk** | [**List[StatsAvailableCpuInner]**](StatsAvailableCpuInner.md) | Disk usage stats from the last 24 hours. | [optional] 
**net_in** | [**List[StatsAvailableCpuInner]**](StatsAvailableCpuInner.md) | Inbound network traffic stats from the last 24 hours. | [optional] 
**net_out** | [**List[StatsAvailableCpuInner]**](StatsAvailableCpuInner.md) | Outbound network traffic stats from the last 24 hours. | [optional] 
**swap** | [**List[StatsAvailableCpuInner]**](StatsAvailableCpuInner.md) | Swap usage stats from the last 24 hours. | [optional] 

## Example

```python
from openapi_client.models.get_managed_stats200_response_data import GetManagedStats200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedStats200ResponseData from a JSON string
get_managed_stats200_response_data_instance = GetManagedStats200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GetManagedStats200ResponseData.to_json())

# convert the object into a dict
get_managed_stats200_response_data_dict = get_managed_stats200_response_data_instance.to_dict()
# create an instance of GetManagedStats200ResponseData from a dict
get_managed_stats200_response_data_from_dict = GetManagedStats200ResponseData.from_dict(get_managed_stats200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


