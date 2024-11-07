# GetInvoices200ResponseDataInner

Account Invoice object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**billing_source** | **str** | &#x60;akamai&#x60;: This Invoice was generated according to the terms of an agreement between the customer and Akamai.  &#x60;linode&#x60;: This Invoice was generated according to the default terms, prices, and discounts. | [optional] [readonly] 
**var_date** | **datetime** | When this Invoice was generated. | [optional] [readonly] 
**id** | **int** | The Invoice&#39;s unique ID. | [optional] [readonly] 
**label** | **str** | The Invoice&#39;s display label. | [optional] [readonly] 
**subtotal** | **float** | The amount of the Invoice before taxes in US Dollars. | [optional] [readonly] 
**tax** | **float** | The amount of tax levied on the Invoice in US Dollars. | [optional] [readonly] 
**tax_summary** | [**List[GetInvoices200ResponseDataInnerTaxSummaryInner]**](GetInvoices200ResponseDataInnerTaxSummaryInner.md) | The amount of tax broken down into subtotals by source. | [optional] [readonly] 
**total** | **float** | The amount of the Invoice after taxes in US Dollars. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_invoices200_response_data_inner import GetInvoices200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoices200ResponseDataInner from a JSON string
get_invoices200_response_data_inner_instance = GetInvoices200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoices200ResponseDataInner.to_json())

# convert the object into a dict
get_invoices200_response_data_inner_dict = get_invoices200_response_data_inner_instance.to_dict()
# create an instance of GetInvoices200ResponseDataInner from a dict
get_invoices200_response_data_inner_from_dict = GetInvoices200ResponseDataInner.from_dict(get_invoices200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


