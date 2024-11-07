# GetLkeClusterAcl200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**acl** | [**GetLkeClusterAcl200ResponseAllOfAcl**](GetLkeClusterAcl200ResponseAllOfAcl.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_acl200_response import GetLkeClusterAcl200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterAcl200Response from a JSON string
get_lke_cluster_acl200_response_instance = GetLkeClusterAcl200Response.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterAcl200Response.to_json())

# convert the object into a dict
get_lke_cluster_acl200_response_dict = get_lke_cluster_acl200_response_instance.to_dict()
# create an instance of GetLkeClusterAcl200Response from a dict
get_lke_cluster_acl200_response_from_dict = GetLkeClusterAcl200Response.from_dict(get_lke_cluster_acl200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


