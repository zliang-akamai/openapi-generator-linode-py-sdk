# PutPlacementGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | A unique name for the placement group. A placement group &#x60;label&#x60; has the following constraints:  - It needs to begin and end with an alphanumeric character. - It can only consist of alphanumeric characters, hyphens (&#x60;-&#x60;), underscores (&#x60;_&#x60;), or periods (&#x60;.&#x60;). | [optional] 

## Example

```python
from openapi_client.models.put_placement_group_request import PutPlacementGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutPlacementGroupRequest from a JSON string
put_placement_group_request_instance = PutPlacementGroupRequest.from_json(json)
# print the JSON string representation of the object
print(PutPlacementGroupRequest.to_json())

# convert the object into a dict
put_placement_group_request_dict = put_placement_group_request_instance.to_dict()
# create an instance of PutPlacementGroupRequest from a dict
put_placement_group_request_from_dict = PutPlacementGroupRequest.from_dict(put_placement_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


