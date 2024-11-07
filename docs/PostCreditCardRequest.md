# PostCreditCardRequest

An object representing the credit card information you have on file with Linode to make Payments against your Account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_number** | **str** | Your credit card number. No spaces or hyphens (&#x60;-&#x60;) allowed. | 
**cvv** | **str** | CVV (Card Verification Value) of the credit card, typically found on the back of the card. | 
**expiry_month** | **int** | A value from 1-12 representing the expiration month of your credit card.    - 1 &#x3D; January   - 2 &#x3D; February   - 3 &#x3D; March   - Etc. | 
**expiry_year** | **int** | A four-digit integer representing the expiration year of your credit card.  The combination of &#x60;expiry_month&#x60; and &#x60;expiry_year&#x60; must result in a month/year combination of the current month or in the future. An expiration date set in the past is invalid. | 

## Example

```python
from openapi_client.models.post_credit_card_request import PostCreditCardRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCreditCardRequest from a JSON string
post_credit_card_request_instance = PostCreditCardRequest.from_json(json)
# print the JSON string representation of the object
print(PostCreditCardRequest.to_json())

# convert the object into a dict
post_credit_card_request_dict = post_credit_card_request_instance.to_dict()
# create an instance of PostCreditCardRequest from a dict
post_credit_card_request_from_dict = PostCreditCardRequest.from_dict(post_credit_card_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


