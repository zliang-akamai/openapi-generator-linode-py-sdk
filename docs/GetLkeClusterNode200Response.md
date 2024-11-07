# GetLkeClusterNode200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The Node&#39;s ID. | [optional] [readonly] 
**instance_id** | **int** | The Linode&#39;s ID. If no Linode is currently provisioned for this Node, this is &#x60;null&#x60;. | [optional] 
**status** | **str** | The creation status of this Node. This status is distinct from this Node&#39;s readiness as a Kubernetes Node Object as determined by the command &#x60;kubectl get nodes&#x60;.  &#x60;not_ready&#x60; indicates that the Linode is still being created.  &#x60;ready&#x60; indicates that the Linode has successfully been created and is running Kubernetes software. | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_node200_response import GetLkeClusterNode200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterNode200Response from a JSON string
get_lke_cluster_node200_response_instance = GetLkeClusterNode200Response.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterNode200Response.to_json())

# convert the object into a dict
get_lke_cluster_node200_response_dict = get_lke_cluster_node200_response_instance.to_dict()
# create an instance of GetLkeClusterNode200Response from a dict
get_lke_cluster_node200_response_from_dict = GetLkeClusterNode200Response.from_dict(get_lke_cluster_node200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


