# GetLkeClusterKubeconfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubeconfig** | **str** | The Base64-encoded Kubeconfig file for this Cluster. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_lke_cluster_kubeconfig200_response import GetLkeClusterKubeconfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterKubeconfig200Response from a JSON string
get_lke_cluster_kubeconfig200_response_instance = GetLkeClusterKubeconfig200Response.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterKubeconfig200Response.to_json())

# convert the object into a dict
get_lke_cluster_kubeconfig200_response_dict = get_lke_cluster_kubeconfig200_response_instance.to_dict()
# create an instance of GetLkeClusterKubeconfig200Response from a dict
get_lke_cluster_kubeconfig200_response_from_dict = GetLkeClusterKubeconfig200Response.from_dict(get_lke_cluster_kubeconfig200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


