# GetLkeClusterAcl404ResponseErrorsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** | The field in the request that caused this error. This may be a path, separated by periods in the case of nested fields. In some cases this may come back as null if the error is not specific to any single element of the request. | [optional] 
**reason** | **str** | A string explaining that the cluster does not exist. | [optional] 

## Example

```python
from openapi_client.models.get_lke_cluster_acl404_response_errors_inner import GetLkeClusterAcl404ResponseErrorsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterAcl404ResponseErrorsInner from a JSON string
get_lke_cluster_acl404_response_errors_inner_instance = GetLkeClusterAcl404ResponseErrorsInner.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterAcl404ResponseErrorsInner.to_json())

# convert the object into a dict
get_lke_cluster_acl404_response_errors_inner_dict = get_lke_cluster_acl404_response_errors_inner_instance.to_dict()
# create an instance of GetLkeClusterAcl404ResponseErrorsInner from a dict
get_lke_cluster_acl404_response_errors_inner_from_dict = GetLkeClusterAcl404ResponseErrorsInner.from_dict(get_lke_cluster_acl404_response_errors_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


