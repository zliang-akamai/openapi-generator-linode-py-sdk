# PostPaymentMethodRequest

Payment Method Request Object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostCreditCardRequest**](PostCreditCardRequest.md) |  | 
**is_default** | **bool** | Whether this Payment Method is the default method for automatically processing service charges. | 
**type** | **str** | The type of Payment Method.  Alternative Payment Methods including Google Pay and PayPal can be added using the Cloud Manager. See the [Manage Payment Methods](https://www.linode.com/docs/products/platform/billing/guides/payment-methods/) guide for details and instructions. | 

## Example

```python
from openapi_client.models.post_payment_method_request import PostPaymentMethodRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPaymentMethodRequest from a JSON string
post_payment_method_request_instance = PostPaymentMethodRequest.from_json(json)
# print the JSON string representation of the object
print(PostPaymentMethodRequest.to_json())

# convert the object into a dict
post_payment_method_request_dict = post_payment_method_request_instance.to_dict()
# create an instance of PostPaymentMethodRequest from a dict
post_payment_method_request_from_dict = PostPaymentMethodRequest.from_dict(post_payment_method_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


