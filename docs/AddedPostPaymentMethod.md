# AddedPostPaymentMethod

Payment Method Request Object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**PostCreditCardRequest**](PostCreditCardRequest.md) |  | 
**is_default** | **bool** | Whether this Payment Method is the default method for automatically processing service charges. | 
**type** | **str** | The type of Payment Method.  Alternative Payment Methods including Google Pay and PayPal can be added using the Cloud Manager. See the [Manage Payment Methods](https://www.linode.com/docs/products/platform/billing/guides/payment-methods/) guide for details and instructions. | 

## Example

```python
from openapi_client.models.added_post_payment_method import AddedPostPaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of AddedPostPaymentMethod from a JSON string
added_post_payment_method_instance = AddedPostPaymentMethod.from_json(json)
# print the JSON string representation of the object
print(AddedPostPaymentMethod.to_json())

# convert the object into a dict
added_post_payment_method_dict = added_post_payment_method_instance.to_dict()
# create an instance of AddedPostPaymentMethod from a dict
added_post_payment_method_from_dict = AddedPostPaymentMethod.from_dict(added_post_payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


