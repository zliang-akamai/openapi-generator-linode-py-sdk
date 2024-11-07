# InvoiceItem

An InvoiceItem object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** | The price, in US dollars, of the Invoice Item. Equal to the unit price multiplied by quantity. | [optional] [readonly] 
**var_from** | **datetime** | The date the Invoice Item started, based on month. | [optional] [readonly] 
**label** | **str** | The Invoice Item&#39;s display label. | [optional] [readonly] 
**quantity** | **int** | The quantity of this Item for the specified Invoice. | [optional] [readonly] 
**region** | **str** | The ID of the applicable Region associated with this Invoice Item.  &#x60;null&#x60; if there is no applicable Region. | [optional] [readonly] 
**tax** | **float** | The amount of tax levied on this Item in US Dollars. | [optional] [readonly] 
**to** | **datetime** | The date the Invoice Item ended, based on month. | [optional] [readonly] 
**total** | **float** | The price of this Item after taxes in US Dollars. | [optional] [readonly] 
**type** | **str** | The type of service, ether &#x60;hourly&#x60; or &#x60;misc&#x60;. | [optional] [readonly] 
**unit_price** | **str** | The monthly service fee in US Dollars for this Item. | [optional] [readonly] 

## Example

```python
from openapi_client.models.invoice_item import InvoiceItem

# TODO update the JSON string below
json = "{}"
# create an instance of InvoiceItem from a JSON string
invoice_item_instance = InvoiceItem.from_json(json)
# print the JSON string representation of the object
print(InvoiceItem.to_json())

# convert the object into a dict
invoice_item_dict = invoice_item_instance.to_dict()
# create an instance of InvoiceItem from a dict
invoice_item_from_dict = InvoiceItem.from_dict(invoice_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


