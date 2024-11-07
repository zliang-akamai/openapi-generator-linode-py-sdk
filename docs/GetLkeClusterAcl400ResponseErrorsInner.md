# GetLkeClusterAcl400ResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field in the request that caused this error. This may be a path, separated by periods in the case of nested fields. In some cases this may come back as null if the error is not specific to any single element of the request. | [optional] 
**reason** | **str** | A string explaining that the cluster does not support Control Plane ACL. | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_acl400_response_errors_inner import GetLkeClusterAcl400ResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterAcl400ResponseErrorsInner from a JSON string
get_lke_cluster_acl400_response_errors_inner_instance = GetLkeClusterAcl400ResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterAcl400ResponseErrorsInner.to_json())

# convert the object into a dict
get_lke_cluster_acl400_response_errors_inner_dict = get_lke_cluster_acl400_response_errors_inner_instance.to_dict()
# create an instance of GetLkeClusterAcl400ResponseErrorsInner from a dict
get_lke_cluster_acl400_response_errors_inner_from_dict = GetLkeClusterAcl400ResponseErrorsInner.from_dict(get_lke_cluster_acl400_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


