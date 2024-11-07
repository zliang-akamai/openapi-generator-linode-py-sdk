# GetVlans200ResponseDataInner

A virtual local area network (VLAN) associated with your Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | The date this VLAN was created. | [optional] [readonly] 
**label** | **str** | The name of this VLAN. | [optional] [readonly] 
**linodes** | **List[int]** | An array of Linode IDs attached to this VLAN. | [optional] [readonly] 
**region** | **str** | This VLAN&#39;s data center region.  __Note__. Currently, a VLAN can only be assigned to a Linode within the same data center region. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_vlans200_response_data_inner import GetVlans200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetVlans200ResponseDataInner from a JSON string
get_vlans200_response_data_inner_instance = GetVlans200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetVlans200ResponseDataInner.to_json())

# convert the object into a dict
get_vlans200_response_data_inner_dict = get_vlans200_response_data_inner_instance.to_dict()
# create an instance of GetVlans200ResponseDataInner from a dict
get_vlans200_response_data_inner_from_dict = GetVlans200ResponseDataInner.from_dict(get_vlans200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


