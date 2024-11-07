# GetPaymentMethods200ResponseDataInner

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
from openapi_client.models.get_payment_methods200_response_data_inner import GetPaymentMethods200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethods200ResponseDataInner from a JSON string
get_payment_methods200_response_data_inner_instance = GetPaymentMethods200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethods200ResponseDataInner.to_json())

# convert the object into a dict
get_payment_methods200_response_data_inner_dict = get_payment_methods200_response_data_inner_instance.to_dict()
# create an instance of GetPaymentMethods200ResponseDataInner from a dict
get_payment_methods200_response_data_inner_from_dict = GetPaymentMethods200ResponseDataInner.from_dict(get_payment_methods200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


