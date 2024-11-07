# GetPaymentMethods200ResponseDataInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_type** | **str** | The type of credit card. | [optional] [readonly] 
**expiry** | **str** | The expiration month and year of the credit card. | [optional] [readonly] 
**last_four** | **str** | The last four digits of the credit card number. | [optional] [readonly] 
**email** | **str** | The email address associated with your PayPal account. | [optional] [readonly] 
**paypal_id** | **str** | PayPal Merchant ID associated with your PayPal account. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_payment_methods200_response_data_inner_data import GetPaymentMethods200ResponseDataInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethods200ResponseDataInnerData from a JSON string
get_payment_methods200_response_data_inner_data_instance = GetPaymentMethods200ResponseDataInnerData.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethods200ResponseDataInnerData.to_json())

# convert the object into a dict
get_payment_methods200_response_data_inner_data_dict = get_payment_methods200_response_data_inner_data_instance.to_dict()
# create an instance of GetPaymentMethods200ResponseDataInnerData from a dict
get_payment_methods200_response_data_inner_data_from_dict = GetPaymentMethods200ResponseDataInnerData.from_dict(get_payment_methods200_response_data_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


