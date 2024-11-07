# PaypalData

PayPal information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address associated with your PayPal account. | [optional] [readonly] 
**paypal_id** | **str** | PayPal Merchant ID associated with your PayPal account. | [optional] [readonly] 

## Example

```python
from openapi_client.models.paypal_data import PaypalData

# TODO update the JSON string below
json = "{}"
# create an instance of PaypalData from a JSON string
paypal_data_instance = PaypalData.from_json(json)
# print the JSON string representation of the object
print(PaypalData.to_json())

# convert the object into a dict
paypal_data_dict = paypal_data_instance.to_dict()
# create an instance of PaypalData from a dict
paypal_data_from_dict = PaypalData.from_dict(paypal_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


