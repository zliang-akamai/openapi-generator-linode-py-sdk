# AddedPostPayment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method_id** | **int** | The ID of the Payment Method to apply to the Payment. | [optional] 
**usd** | **str** | The amount in US Dollars of the Payment.  - Can begin with or without &#x60;$&#x60;. - Commas (&#x60;,&#x60;) are not accepted. - Must end with a decimal expression, such as &#x60;.00&#x60; or &#x60;.99&#x60;. - Minimum: &#x60;$5.00&#x60; or the Account balance, whichever is lower. - Maximum: &#x60;$2000.00&#x60; or the Account balance up to &#x60;$50000.00&#x60;, whichever is greater. | [optional] 

## Example

```python
from openapi_client.models.added_post_payment import AddedPostPayment

# TODO update the JSON string below
json = "{}"
# create an instance of AddedPostPayment from a JSON string
added_post_payment_instance = AddedPostPayment.from_json(json)
# print the JSON string representation of the object
print(AddedPostPayment.to_json())

# convert the object into a dict
added_post_payment_dict = added_post_payment_instance.to_dict()
# create an instance of AddedPostPayment from a dict
added_post_payment_from_dict = AddedPostPayment.from_dict(added_post_payment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


