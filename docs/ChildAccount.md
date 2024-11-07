# ChildAccount

Child account object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_since** | **datetime** | The activation date and time for the child account. | [optional] [readonly] 
**address_1** | **str** | First line of this child account&#39;s billing address. | [optional] 
**address_2** | **str** | Second line of this child account&#39;s billing address, if applicable. | [optional] 
**balance** | **float** | This child account&#39;s balance, in US dollars. | [optional] [readonly] 
**balance_uninvoiced** | **float** | This child account&#39;s current estimated invoice in US dollars. This is not your final invoice balance. Transfer charges are not included in the estimate. | [optional] [readonly] 
**billing_source** | **str** | The source of service charges for this account, as determined by its relationship with Akamai. The API returns a value of &#x60;external&#x60; to describe a child account in a parent-child account environment. | [optional] [readonly] 
**capabilities** | **List[str]** | A list of the capabilities the child account supports. | [optional] [readonly] 
**city** | **str** | The city for this child account&#39;s billing address. | [optional] 
**company** | **str** | The company name for the owner of this child account. It can&#39;t include any of these characters: &#x60;&lt;&#x60; &#x60;&gt;&#x60; &#x60;(&#x60; &#x60;)&#x60; &#x60;\&quot;&#x60; &#x60;&#x3D;&#x60;. You can&#39;t change this value yourself. We use it to create the proxy users that a parent account uses to access a child account. Talk to your account team if you need to change this value. | [optional] 
**country** | **str** | The two-letter ISO 3166 country code for this child account&#39;s billing address. | [optional] 
**credit_card** | [**GetChildAccounts200ResponseDataInnerCreditCard**](GetChildAccounts200ResponseDataInnerCreditCard.md) |  | [optional] 
**email** | **str** | The email address of the owner of this child account. | [optional] 
**euuid** | **str** | An external, unique identifier that Akamai assigned to the child account. | [optional] [readonly] 
**first_name** | **str** | The first name of the owner of this child account. It can&#39;t include any of these characters: &#x60;&lt;&#x60; &#x60;&gt;&#x60; &#x60;(&#x60; &#x60;)&#x60; &#x60;\&quot;&#x60; &#x60;&#x3D;&#x60;. | [optional] 
**last_name** | **str** | The last name of the owner of this child account. It can&#39;t include any of these characters: &#x60;&lt;&#x60; &#x60;&gt;&#x60; &#x60;(&#x60; &#x60;)&#x60; &#x60;\&quot;&#x60; &#x60;&#x3D;&#x60;. | [optional] 
**phone** | **str** | The phone number for the owner of this child account. | [optional] 
**state** | **str** | The state or province for the billing address (&#x60;address_1&#x60; and &#x60;address_2, if applicable&#x60;). If in the United States (US) or Canada (CA), this is the two-letter ISO 3166 State or Province code.  __Note__. If this is a US military address, use state abbreviations (AA, AE, AP). | [optional] 
**tax_id** | **str** | The tax identification number for this child account. Use this for tax calculations in some countries. If you live in a country that doesn&#39;t collect taxes, ensure this is an empty string (&#x60;\&quot;\&quot;&#x60;). | [optional] 
**zip** | **str** | The zip code of this Account&#39;s billing address. The following restrictions apply:  - Can only contain ASCII letters, numbers, and hyphens (&#x60;-&#x60;). - Can&#39;t contain more than 9 letter or number characters. | [optional] 

## Example

```python
from openapi_client.models.child_account import ChildAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ChildAccount from a JSON string
child_account_instance = ChildAccount.from_json(json)
# print the JSON string representation of the object
print(ChildAccount.to_json())

# convert the object into a dict
child_account_dict = child_account_instance.to_dict()
# create an instance of ChildAccount from a dict
child_account_from_dict = ChildAccount.from_dict(child_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


