# GetAccount200ResponseCreditCard

Credit Card information associated with this Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **str** | The expiration month and year of the credit card. | [optional] 
**last_four** | **str** | The last four digits of the credit card associated with this Account. | [optional] 

## Example

```python
from openapi_client.models.get_account200_response_credit_card import GetAccount200ResponseCreditCard

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccount200ResponseCreditCard from a JSON string
get_account200_response_credit_card_instance = GetAccount200ResponseCreditCard.from_json(json)
# print the JSON string representation of the object
print(GetAccount200ResponseCreditCard.to_json())

# convert the object into a dict
get_account200_response_credit_card_dict = get_account200_response_credit_card_instance.to_dict()
# create an instance of GetAccount200ResponseCreditCard from a dict
get_account200_response_credit_card_from_dict = GetAccount200ResponseCreditCard.from_dict(get_account200_response_credit_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


