# StatsAvailable

A collection of graph data returned for managed stats.

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
from openapi_client.models.stats_available import StatsAvailable

# TODO update the JSON string below
json = "{}"
# create an instance of StatsAvailable from a JSON string
stats_available_instance = StatsAvailable.from_json(json)
# print the JSON string representation of the object
print(StatsAvailable.to_json())

# convert the object into a dict
stats_available_dict = stats_available_instance.to_dict()
# create an instance of StatsAvailable from a dict
stats_available_from_dict = StatsAvailable.from_dict(stats_available_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


