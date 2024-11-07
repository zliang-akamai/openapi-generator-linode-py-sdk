# GetManagedContacts200ResponseDataInnerPhone

Information about how to reach this Contact by phone.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary** | **str** | This Contact&#39;s primary phone number. | [optional] 
**secondary** | **str** | This Contact&#39;s secondary phone number. | [optional] 

## Example

```python
from openapi_client.models.get_managed_contacts200_response_data_inner_phone import GetManagedContacts200ResponseDataInnerPhone

# TODO update the JSON string below
json = "{}"
# create an instance of GetManagedContacts200ResponseDataInnerPhone from a JSON string
get_managed_contacts200_response_data_inner_phone_instance = GetManagedContacts200ResponseDataInnerPhone.from_json(json)
# print the JSON string representation of the object
print(GetManagedContacts200ResponseDataInnerPhone.to_json())

# convert the object into a dict
get_managed_contacts200_response_data_inner_phone_dict = get_managed_contacts200_response_data_inner_phone_instance.to_dict()
# create an instance of GetManagedContacts200ResponseDataInnerPhone from a dict
get_managed_contacts200_response_data_inner_phone_from_dict = GetManagedContacts200ResponseDataInnerPhone.from_dict(get_managed_contacts200_response_data_inner_phone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


