# AddedPostPayPalPayment200


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**checkout_token** | **str** | The checkout token generated for this Payment. | [optional] [readonly] 
**payment_id** | **str** | The paypal-generated ID for this Payment. Used when authorizing the Payment in PayPal&#39;s interface. | [optional] 

## Example

```python
from openapi_client.models.added_post_pay_pal_payment200 import AddedPostPayPalPayment200

# TODO update the JSON string below
json = "{}"
# create an instance of AddedPostPayPalPayment200 from a JSON string
added_post_pay_pal_payment200_instance = AddedPostPayPalPayment200.from_json(json)
# print the JSON string representation of the object
print(AddedPostPayPalPayment200.to_json())

# convert the object into a dict
added_post_pay_pal_payment200_dict = added_post_pay_pal_payment200_instance.to_dict()
# create an instance of AddedPostPayPalPayment200 from a dict
added_post_pay_pal_payment200_from_dict = AddedPostPayPalPayment200.from_dict(added_post_pay_pal_payment200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


