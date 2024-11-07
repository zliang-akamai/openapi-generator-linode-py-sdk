# PaypalExecute

An object representing an execution of Payment to PayPal to capture the funds and credit your Linode Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_id** | **str** | The PayerID returned by PayPal during the transaction authorization process. | 
**payment_id** | **str** | The PaymentID returned from [Stage a PayPal payment](https://techdocs.akamai.com/linode-api/reference/post-pay-pal-payment) that has been approved with PayPal. | 

## Example

```python
from openapi_client.models.paypal_execute import PaypalExecute

# TODO update the JSON string below
json = "{}"
# create an instance of PaypalExecute from a JSON string
paypal_execute_instance = PaypalExecute.from_json(json)
# print the JSON string representation of the object
print(PaypalExecute.to_json())

# convert the object into a dict
paypal_execute_dict = paypal_execute_instance.to_dict()
# create an instance of PaypalExecute from a dict
paypal_execute_from_dict = PaypalExecute.from_dict(paypal_execute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


