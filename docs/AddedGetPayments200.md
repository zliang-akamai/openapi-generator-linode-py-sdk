# AddedGetPayments200


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetPayments200ResponseDataInner]**](GetPayments200ResponseDataInner.md) |  | [optional] 
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 

## Example

```python
from openapi_client.models.added_get_payments200 import AddedGetPayments200

# TODO update the JSON string below
json = "{}"
# create an instance of AddedGetPayments200 from a JSON string
added_get_payments200_instance = AddedGetPayments200.from_json(json)
# print the JSON string representation of the object
print(AddedGetPayments200.to_json())

# convert the object into a dict
added_get_payments200_dict = added_get_payments200_instance.to_dict()
# create an instance of AddedGetPayments200 from a dict
added_get_payments200_from_dict = AddedGetPayments200.from_dict(added_get_payments200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


