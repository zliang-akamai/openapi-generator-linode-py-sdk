# GetAccount200Response

Account object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_promotions** | [**List[GetAccount200ResponseActivePromotionsInner]**](GetAccount200ResponseActivePromotionsInner.md) |  | [optional] [readonly] 
**active_since** | **datetime** | The date and time the account was activated. | [optional] [readonly] 
**address_1** | **str** | First line of this Account&#39;s billing address. | [optional] 
**address_2** | **str** | Second line of this Account&#39;s billing address. | [optional] 
**balance** | **float** | This Account&#39;s balance, in US dollars. | [optional] [readonly] 
**balance_uninvoiced** | **float** | This Account&#39;s current estimated invoice in US dollars. This is not your final invoice balance. Transfer charges are not included in the estimate. | [optional] [readonly] 
**billing_source** | **str** | The source of service charges for this Account, as determined by its relationship with Akamai. Accounts that are associated with Akamai-specific customers return a value of &#x60;akamai&#x60;. All other Accounts return a value of &#x60;linode&#x60;. | [optional] [readonly] 
**capabilities** | **List[str]** | A list of capabilities your account supports. | [optional] [readonly] 
**city** | **str** | The city for this Account&#39;s billing address. | [optional] 
**company** | **str** | The company name associated with this Account.  Must not include any of the following characters: &#x60;&lt;&#x60; &#x60;&gt;&#x60; &#x60;(&#x60; &#x60;)&#x60; &#x60;\&quot;&#x60; &#x60;&#x3D;&#x60; | [optional] 
**country** | **str** | The two-letter ISO 3166 country code of this Account&#39;s billing address. | [optional] 
**credit_card** | [**GetAccount200ResponseCreditCard**](GetAccount200ResponseCreditCard.md) |  | [optional] 
**email** | **str** | The email address of the person associated with this Account. | [optional] 
**euuid** | **str** | An external unique identifier for this account. | [optional] [readonly] 
**first_name** | **str** | The first name of the person associated with this Account.  Must not include any of the following characters: &#x60;&lt;&#x60; &#x60;&gt;&#x60; &#x60;(&#x60; &#x60;)&#x60; &#x60;\&quot;&#x60; &#x60;&#x3D;&#x60; | [optional] 
**last_name** | **str** | The last name of the person associated with this Account.  Must not include any of the following characters: &#x60;&lt;&#x60; &#x60;&gt;&#x60; &#x60;(&#x60; &#x60;)&#x60; &#x60;\&quot;&#x60; &#x60;&#x3D;&#x60; | [optional] 
**phone** | **str** | The phone number associated with this Account. | [optional] 
**state** | **str** | If billing address is in the United States (US) or Canada (CA), only the two-letter ISO 3166 State or Province code are accepted. If entering a US military address, state abbreviations (AA, AE, AP) should be entered. If the address is outside the US or CA, this is the Province associated with the Account&#39;s billing address. | [optional] 
**tax_id** | **str** | The tax identification number associated with this Account, for tax calculations in some countries. If you do not live in a country that collects tax, this should be an empty string (&#x60;\&quot;\&quot;&#x60;). | [optional] 
**zip** | **str** | The zip code of this Account&#39;s billing address. The following restrictions apply:  - Can only contain ASCII letters, numbers, and hyphens (&#x60;-&#x60;). - Must not contain more than 9 letter or number characters. | [optional] 

## Example

```python
from openapi_client.models.get_account200_response import GetAccount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccount200Response from a JSON string
get_account200_response_instance = GetAccount200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccount200Response.to_json())

# convert the object into a dict
get_account200_response_dict = get_account200_response_instance.to_dict()
# create an instance of GetAccount200Response from a dict
get_account200_response_from_dict = GetAccount200Response.from_dict(get_account200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


