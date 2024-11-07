# PostLkeClusterRegenerateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kubeconfig** | **bool** | Whether to delete and regenerate the Kubeconfig file for this Cluster. | [optional] [default to False]
**servicetoken** | **bool** | Whether to delete and regenerate the service access token for this Cluster. | [optional] [default to False]

## Example

```python
from openapi_client.models.post_lke_cluster_regenerate_request import PostLkeClusterRegenerateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostLkeClusterRegenerateRequest from a JSON string
post_lke_cluster_regenerate_request_instance = PostLkeClusterRegenerateRequest.from_json(json)
# print the JSON string representation of the object
print(PostLkeClusterRegenerateRequest.to_json())

# convert the object into a dict
post_lke_cluster_regenerate_request_dict = post_lke_cluster_regenerate_request_instance.to_dict()
# create an instance of PostLkeClusterRegenerateRequest from a dict
post_lke_cluster_regenerate_request_from_dict = PostLkeClusterRegenerateRequest.from_dict(post_lke_cluster_regenerate_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


