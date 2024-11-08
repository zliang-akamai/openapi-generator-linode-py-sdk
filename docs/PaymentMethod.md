# PaymentMethod

Payment Method Response Object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created** | **datetime** | When the Payment Method was added to the Account. | [optional] [readonly] 
**data** | [**GetPaymentMethods200ResponseDataInnerData**](GetPaymentMethods200ResponseDataInnerData.md) |  | [optional] 
**id** | **int** | The unique ID of this Payment Method. | [optional] 
**is_default** | **bool** | Whether this Payment Method is the default method for automatically processing service charges. | [optional] 
**type** | **str** | The type of Payment Method. | [optional] 

## Example

```python
from openapi_client.models.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print(PaymentMethod.to_json())

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_from_dict = PaymentMethod.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


