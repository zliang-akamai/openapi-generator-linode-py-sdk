# GetTags200ResponseDataInner

A tag that has been applied to an object on your Account. Tags are currently for organizational purposes only.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | A Label used for organization of objects on your Account. | [optional] 

## Example

```python
from openapi_client.models.get_tags200_response_data_inner import GetTags200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTags200ResponseDataInner from a JSON string
get_tags200_response_data_inner_instance = GetTags200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetTags200ResponseDataInner.to_json())

# convert the object into a dict
get_tags200_response_data_inner_dict = get_tags200_response_data_inner_instance.to_dict()
# create an instance of GetTags200ResponseDataInner from a dict
get_tags200_response_data_inner_from_dict = GetTags200ResponseDataInner.from_dict(get_tags200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


