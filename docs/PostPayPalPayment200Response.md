# PostPayPalPayment200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_token** | **str** | The checkout token generated for this Payment. | [optional] [readonly] 
**payment_id** | **str** | The paypal-generated ID for this Payment. Used when authorizing the Payment in PayPal&#39;s interface. | [optional] 

## Example

```python
from openapi_client.models.post_pay_pal_payment200_response import PostPayPalPayment200Response

# TODO update the JSON string below
json = "{}"
# create an instance of PostPayPalPayment200Response from a JSON string
post_pay_pal_payment200_response_instance = PostPayPalPayment200Response.from_json(json)
# print the JSON string representation of the object
print(PostPayPalPayment200Response.to_json())

# convert the object into a dict
post_pay_pal_payment200_response_dict = post_pay_pal_payment200_response_instance.to_dict()
# create an instance of PostPayPalPayment200Response from a dict
post_pay_pal_payment200_response_from_dict = PostPayPalPayment200Response.from_dict(post_pay_pal_payment200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


