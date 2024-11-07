# GetLkeClusterPools200ResponseDataInnerTaintsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**effect** | **str** | The Kubernetes taint effect. For &#x60;NoSchedule&#x60;, &#x60;PreferNoSchedule&#x60; and &#x60;NoExecute&#x60; descriptions, see [Kubernetes Taints and Tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/). | [optional] 
**key** | **str** | The Kubernetes taint key. | [optional] 
**value** | **str** | The Kubernetes taint value. | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_pools200_response_data_inner_taints_inner import GetLkeClusterPools200ResponseDataInnerTaintsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterPools200ResponseDataInnerTaintsInner from a JSON string
get_lke_cluster_pools200_response_data_inner_taints_inner_instance = GetLkeClusterPools200ResponseDataInnerTaintsInner.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterPools200ResponseDataInnerTaintsInner.to_json())

# convert the object into a dict
get_lke_cluster_pools200_response_data_inner_taints_inner_dict = get_lke_cluster_pools200_response_data_inner_taints_inner_instance.to_dict()
# create an instance of GetLkeClusterPools200ResponseDataInnerTaintsInner from a dict
get_lke_cluster_pools200_response_data_inner_taints_inner_from_dict = GetLkeClusterPools200ResponseDataInnerTaintsInner.from_dict(get_lke_cluster_pools200_response_data_inner_taints_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


