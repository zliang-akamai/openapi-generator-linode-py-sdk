# GooglePay

Google Pay information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | The type of credit card. | [optional] [readonly] 
**expiry** | **str** | The expiration month and year of the credit card. | [optional] [readonly] 
**last_four** | **str** | The last four digits of the credit card number. | [optional] [readonly] 

## Example

```python
from openapi_client.models.google_pay import GooglePay

# TODO update the JSON string below
json = "{}"
# create an instance of GooglePay from a JSON string
google_pay_instance = GooglePay.from_json(json)
# print the JSON string representation of the object
print(GooglePay.to_json())

# convert the object into a dict
google_pay_dict = google_pay_instance.to_dict()
# create an instance of GooglePay from a dict
google_pay_from_dict = GooglePay.from_dict(google_pay_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


