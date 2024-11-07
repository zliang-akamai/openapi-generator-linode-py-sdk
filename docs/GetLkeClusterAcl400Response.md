# GetLkeClusterAcl400Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | [**List[GetLkeClusterAcl400ResponseErrorsInner]**](GetLkeClusterAcl400ResponseErrorsInner.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_acl400_response import GetLkeClusterAcl400Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterAcl400Response from a JSON string
get_lke_cluster_acl400_response_instance = GetLkeClusterAcl400Response.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterAcl400Response.to_json())

# convert the object into a dict
get_lke_cluster_acl400_response_dict = get_lke_cluster_acl400_response_instance.to_dict()
# create an instance of GetLkeClusterAcl400Response from a dict
get_lke_cluster_acl400_response_from_dict = GetLkeClusterAcl400Response.from_dict(get_lke_cluster_acl400_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


