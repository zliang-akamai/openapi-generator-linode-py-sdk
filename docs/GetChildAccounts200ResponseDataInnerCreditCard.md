# GetChildAccounts200ResponseDataInnerCreditCard

Information for the credit card you've assigned to this child account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry** | **str** | The expiration month and year of the credit card. | [optional] 
**last_four** | **str** | The last four digits of the credit card. | [optional] 

## Example

```python
from openapi_client.models.get_child_accounts200_response_data_inner_credit_card import GetChildAccounts200ResponseDataInnerCreditCard

# TODO update the JSON string below
json = "{}"
# create an instance of GetChildAccounts200ResponseDataInnerCreditCard from a JSON string
get_child_accounts200_response_data_inner_credit_card_instance = GetChildAccounts200ResponseDataInnerCreditCard.from_json(json)
# print the JSON string representation of the object
print(GetChildAccounts200ResponseDataInnerCreditCard.to_json())

# convert the object into a dict
get_child_accounts200_response_data_inner_credit_card_dict = get_child_accounts200_response_data_inner_credit_card_instance.to_dict()
# create an instance of GetChildAccounts200ResponseDataInnerCreditCard from a dict
get_child_accounts200_response_data_inner_credit_card_from_dict = GetChildAccounts200ResponseDataInnerCreditCard.from_dict(get_child_accounts200_response_data_inner_credit_card_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


