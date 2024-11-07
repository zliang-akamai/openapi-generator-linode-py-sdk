# GetPayments200ResponseDataInner

Payment object response.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **datetime** | When the Payment was made. | [optional] [readonly] 
**id** | **int** | The unique ID of the Payment. | [optional] [readonly] 
**usd** | **int** | The amount, in US dollars, of the Payment. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_payments200_response_data_inner import GetPayments200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetPayments200ResponseDataInner from a JSON string
get_payments200_response_data_inner_instance = GetPayments200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetPayments200ResponseDataInner.to_json())

# convert the object into a dict
get_payments200_response_data_inner_dict = get_payments200_response_data_inner_instance.to_dict()
# create an instance of GetPayments200ResponseDataInner from a dict
get_payments200_response_data_inner_from_dict = GetPayments200ResponseDataInner.from_dict(get_payments200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


