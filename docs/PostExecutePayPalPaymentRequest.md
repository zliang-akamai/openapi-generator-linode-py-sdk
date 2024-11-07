# PostExecutePayPalPaymentRequest

An object representing an execution of Payment to PayPal to capture the funds and credit your Linode Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer_id** | **str** | The PayerID returned by PayPal during the transaction authorization process. | 
**payment_id** | **str** | The PaymentID returned from [Stage a PayPal payment](https://techdocs.akamai.com/linode-api/reference/post-pay-pal-payment) that has been approved with PayPal. | 

## Example

```python
from openapi_client.models.post_execute_pay_pal_payment_request import PostExecutePayPalPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostExecutePayPalPaymentRequest from a JSON string
post_execute_pay_pal_payment_request_instance = PostExecutePayPalPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PostExecutePayPalPaymentRequest.to_json())

# convert the object into a dict
post_execute_pay_pal_payment_request_dict = post_execute_pay_pal_payment_request_instance.to_dict()
# create an instance of PostExecutePayPalPaymentRequest from a dict
post_execute_pay_pal_payment_request_from_dict = PostExecutePayPalPaymentRequest.from_dict(post_execute_pay_pal_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


