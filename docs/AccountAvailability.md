# AccountAvailability

Account Service Availability object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **List[str]** | A list of services _available_ to your account in the &#x60;region&#x60;. | [optional] [readonly] 
**region** | **str** | The Akamai cloud computing data center (region), represented by a slug value. You can view a full list of regions and their associated slugs with the [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions) operation. | [optional] [readonly] 
**unavailable** | **List[str]** | A list of services _unavailable_ to your account in the &#x60;region&#x60;. | [optional] [readonly] 

## Example

```python
from openapi_client.models.account_availability import AccountAvailability

# TODO update the JSON string below
json = "{}"
# create an instance of AccountAvailability from a JSON string
account_availability_instance = AccountAvailability.from_json(json)
# print the JSON string representation of the object
print(AccountAvailability.to_json())

# convert the object into a dict
account_availability_dict = account_availability_instance.to_dict()
# create an instance of AccountAvailability from a dict
account_availability_from_dict = AccountAvailability.from_dict(account_availability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


