# GetPlacementGroups200ResponseDataInnerMembersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_compliant** | **bool** | The compliance status of each individual compute instance in the placement group. | [optional] 
**linode_id** | **int** | The unique identifier for a compute instance included in the placement group. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_placement_groups200_response_data_inner_members_inner import GetPlacementGroups200ResponseDataInnerMembersInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlacementGroups200ResponseDataInnerMembersInner from a JSON string
get_placement_groups200_response_data_inner_members_inner_instance = GetPlacementGroups200ResponseDataInnerMembersInner.from_json(json)
# print the JSON string representation of the object
print(GetPlacementGroups200ResponseDataInnerMembersInner.to_json())

# convert the object into a dict
get_placement_groups200_response_data_inner_members_inner_dict = get_placement_groups200_response_data_inner_members_inner_instance.to_dict()
# create an instance of GetPlacementGroups200ResponseDataInnerMembersInner from a dict
get_placement_groups200_response_data_inner_members_inner_from_dict = GetPlacementGroups200ResponseDataInnerMembersInner.from_dict(get_placement_groups200_response_data_inner_members_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


