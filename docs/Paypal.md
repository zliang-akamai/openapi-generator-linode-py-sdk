# Paypal

PayPal information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** | The email address associated with your PayPal account. | [optional] [readonly] 
**paypal_id** | **str** | PayPal Merchant ID associated with your PayPal account. | [optional] [readonly] 

## Example

```python
from openapi_client.models.paypal import Paypal

# TODO update the JSON string below
json = "{}"
# create an instance of Paypal from a JSON string
paypal_instance = Paypal.from_json(json)
# print the JSON string representation of the object
print(Paypal.to_json())

# convert the object into a dict
paypal_dict = paypal_instance.to_dict()
# create an instance of Paypal from a dict
paypal_from_dict = Paypal.from_dict(paypal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


