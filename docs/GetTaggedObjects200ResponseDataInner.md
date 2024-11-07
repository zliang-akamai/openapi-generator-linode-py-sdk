# GetTaggedObjects200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetTaggedObjects200ResponseDataInnerData**](GetTaggedObjects200ResponseDataInnerData.md) |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_tagged_objects200_response_data_inner import GetTaggedObjects200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaggedObjects200ResponseDataInner from a JSON string
get_tagged_objects200_response_data_inner_instance = GetTaggedObjects200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetTaggedObjects200ResponseDataInner.to_json())

# convert the object into a dict
get_tagged_objects200_response_data_inner_dict = get_tagged_objects200_response_data_inner_instance.to_dict()
# create an instance of GetTaggedObjects200ResponseDataInner from a dict
get_tagged_objects200_response_data_inner_from_dict = GetTaggedObjects200ResponseDataInner.from_dict(get_tagged_objects200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


