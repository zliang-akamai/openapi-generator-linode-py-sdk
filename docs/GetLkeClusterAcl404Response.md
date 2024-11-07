# GetLkeClusterAcl404Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[GetLkeClusterAcl404ResponseErrorsInner]**](GetLkeClusterAcl404ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_acl404_response import GetLkeClusterAcl404Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterAcl404Response from a JSON string
get_lke_cluster_acl404_response_instance = GetLkeClusterAcl404Response.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterAcl404Response.to_json())

# convert the object into a dict
get_lke_cluster_acl404_response_dict = get_lke_cluster_acl404_response_instance.to_dict()
# create an instance of GetLkeClusterAcl404Response from a dict
get_lke_cluster_acl404_response_from_dict = GetLkeClusterAcl404Response.from_dict(get_lke_cluster_acl404_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


