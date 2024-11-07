# GetLkeVersions200ResponseDataInner

LKE versions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A Kubernetes version number available for deployment to a Kubernetes cluster in the format of &amp;lt;major&amp;gt;.&amp;lt;minor&amp;gt;, and the latest supported patch version. | [optional] 

## Example

```python
from openapi_client.models.get_lke_versions200_response_data_inner import GetLkeVersions200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetLkeVersions200ResponseDataInner from a JSON string
get_lke_versions200_response_data_inner_instance = GetLkeVersions200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetLkeVersions200ResponseDataInner.to_json())

# convert the object into a dict
get_lke_versions200_response_data_inner_dict = get_lke_versions200_response_data_inner_instance.to_dict()
# create an instance of GetLkeVersions200ResponseDataInner from a dict
get_lke_versions200_response_data_inner_from_dict = GetLkeVersions200ResponseDataInner.from_dict(get_lke_versions200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


