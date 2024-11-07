# GooglePayData

Google Pay information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | The type of credit card. | [optional] [readonly] 
**expiry** | **str** | The expiration month and year of the credit card. | [optional] [readonly] 
**last_four** | **str** | The last four digits of the credit card number. | [optional] [readonly] 

## Example

```python
from openapi_client.models.google_pay_data import GooglePayData

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePayData from a JSON string
google_pay_data_instance = GooglePayData.from_json(json)
# print the JSON string representation of the object
print(GooglePayData.to_json())

# convert the object into a dict
google_pay_data_dict = google_pay_data_instance.to_dict()
# create an instance of GooglePayData from a dict
google_pay_data_from_dict = GooglePayData.from_dict(google_pay_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


