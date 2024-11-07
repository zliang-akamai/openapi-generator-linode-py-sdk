# GetLkeClusterApiEndpoints200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** | A Kubernetes API server endpoint for this cluster. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_lke_cluster_api_endpoints200_response_data_inner import GetLkeClusterApiEndpoints200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeClusterApiEndpoints200ResponseDataInner from a JSON string
get_lke_cluster_api_endpoints200_response_data_inner_instance = GetLkeClusterApiEndpoints200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetLkeClusterApiEndpoints200ResponseDataInner.to_json())

# convert the object into a dict
get_lke_cluster_api_endpoints200_response_data_inner_dict = get_lke_cluster_api_endpoints200_response_data_inner_instance.to_dict()
# create an instance of GetLkeClusterApiEndpoints200ResponseDataInner from a dict
get_lke_cluster_api_endpoints200_response_data_inner_from_dict = GetLkeClusterApiEndpoints200ResponseDataInner.from_dict(get_lke_cluster_api_endpoints200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


