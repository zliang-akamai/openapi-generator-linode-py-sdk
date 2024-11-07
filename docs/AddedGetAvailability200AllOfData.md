# AddedGetAvailability200AllOfData

Account Service Availability object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **List[str]** | A list of services _available_ to your account in the &#x60;region&#x60;. | [optional] [readonly] 
**region** | **str** | The Akamai cloud computing data center (region), represented by a slug value. You can view a full list of regions and their associated slugs with the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation. | [optional] [readonly] 
**unavailable** | **List[str]** | A list of services _unavailable_ to your account in the &#x60;region&#x60;. | [optional] [readonly] 

## Example

```python
from openapi_client.models.added_get_availability200_all_of_data import AddedGetAvailability200AllOfData

# TODO update the JSON string below
json = "{}"
# create an instance of AddedGetAvailability200AllOfData from a JSON string
added_get_availability200_all_of_data_instance = AddedGetAvailability200AllOfData.from_json(json)
# print the JSON string representation of the object
print(AddedGetAvailability200AllOfData.to_json())

# convert the object into a dict
added_get_availability200_all_of_data_dict = added_get_availability200_all_of_data_instance.to_dict()
# create an instance of AddedGetAvailability200AllOfData from a dict
added_get_availability200_all_of_data_from_dict = AddedGetAvailability200AllOfData.from_dict(added_get_availability200_all_of_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


