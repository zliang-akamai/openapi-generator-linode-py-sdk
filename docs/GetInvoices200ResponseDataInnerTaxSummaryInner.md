# GetInvoices200ResponseDataInnerTaxSummaryInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The source of this tax subtotal. | [optional] 
**tax** | **float** | The amount of tax subtotal attributable to this source. | [optional] 

## Example

```python
from openapi_client.models.get_invoices200_response_data_inner_tax_summary_inner import GetInvoices200ResponseDataInnerTaxSummaryInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetInvoices200ResponseDataInnerTaxSummaryInner from a JSON string
get_invoices200_response_data_inner_tax_summary_inner_instance = GetInvoices200ResponseDataInnerTaxSummaryInner.from_json(json)
# print the JSON string representation of the object
print(GetInvoices200ResponseDataInnerTaxSummaryInner.to_json())

# convert the object into a dict
get_invoices200_response_data_inner_tax_summary_inner_dict = get_invoices200_response_data_inner_tax_summary_inner_instance.to_dict()
# create an instance of GetInvoices200ResponseDataInnerTaxSummaryInner from a dict
get_invoices200_response_data_inner_tax_summary_inner_from_dict = GetInvoices200ResponseDataInnerTaxSummaryInner.from_dict(get_invoices200_response_data_inner_tax_summary_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


