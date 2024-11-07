# GetLkeClusterPools200ResponseDataInnerAutoscaler

When enabled, the number of nodes autoscales within the defined minimum and maximum values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Whether autoscaling is enabled for this Node Pool. Defaults to &#x60;false&#x60;. | [optional] 
**max** | **int** | The maximum number of nodes to autoscale to. Defaults to the Node Pool&#39;s &#x60;count&#x60;. | [optional] 
**min** | **int** | The minimum number of nodes to autoscale to. Defaults to the Node Pool&#39;s &#x60;count&#x60;. | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_pools200_response_data_inner_autoscaler import GetLkeClusterPools200ResponseDataInnerAutoscaler

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterPools200ResponseDataInnerAutoscaler from a JSON string
get_lke_cluster_pools200_response_data_inner_autoscaler_instance = GetLkeClusterPools200ResponseDataInnerAutoscaler.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterPools200ResponseDataInnerAutoscaler.to_json())

# convert the object into a dict
get_lke_cluster_pools200_response_data_inner_autoscaler_dict = get_lke_cluster_pools200_response_data_inner_autoscaler_instance.to_dict()
# create an instance of GetLkeClusterPools200ResponseDataInnerAutoscaler from a dict
get_lke_cluster_pools200_response_data_inner_autoscaler_from_dict = GetLkeClusterPools200ResponseDataInnerAutoscaler.from_dict(get_lke_cluster_pools200_response_data_inner_autoscaler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


