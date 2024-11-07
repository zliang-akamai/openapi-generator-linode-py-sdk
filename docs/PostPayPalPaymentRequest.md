# PostPayPalPaymentRequest

An object representing the staging of a Payment via PayPal.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel_url** | **str** | The URL to have PayPal redirect to when Payment is canceled. | 
**redirect_url** | **str** | The URL to have PayPal redirect to when Payment is approved. | 
**usd** | **str** | The payment amount in USD. Minimum accepted value of $5 USD. Maximum accepted value of $500 USD or credit card payment limit; whichever value is highest. PayPal&#39;s maximum transaction limit is $10,000 USD. | 

## Example

```python
from openapi_client.models.post_pay_pal_payment_request import PostPayPalPaymentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostPayPalPaymentRequest from a JSON string
post_pay_pal_payment_request_instance = PostPayPalPaymentRequest.from_json(json)
# print the JSON string representation of the object
print(PostPayPalPaymentRequest.to_json())

# convert the object into a dict
post_pay_pal_payment_request_dict = post_pay_pal_payment_request_instance.to_dict()
# create an instance of PostPayPalPaymentRequest from a dict
post_pay_pal_payment_request_from_dict = PostPayPalPaymentRequest.from_dict(post_pay_pal_payment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


