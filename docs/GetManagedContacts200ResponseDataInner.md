# GetManagedContacts200ResponseDataInner

Information about someone Linode's special forces may contact in case an issue is detected with a manager service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The address to email this Contact to alert them of issues. | [optional] 
**group** | **str** | A grouping for this Contact. This is for display purposes only. | [optional] 
**id** | **int** | This Contact&#39;s unique ID. | [optional] [readonly] 
**name** | **str** | The name of this Contact. | [optional] 
**phone** | [**GetManagedContacts200ResponseDataInnerPhone**](GetManagedContacts200ResponseDataInnerPhone.md) |  | [optional] 
**updated** | **datetime** | When this Contact was last updated. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_managed_contacts200_response_data_inner import GetManagedContacts200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedContacts200ResponseDataInner from a JSON string
get_managed_contacts200_response_data_inner_instance = GetManagedContacts200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetManagedContacts200ResponseDataInner.to_json())

# convert the object into a dict
get_managed_contacts200_response_data_inner_dict = get_managed_contacts200_response_data_inner_instance.to_dict()
# create an instance of GetManagedContacts200ResponseDataInner from a dict
get_managed_contacts200_response_data_inner_from_dict = GetManagedContacts200ResponseDataInner.from_dict(get_managed_contacts200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


