# AddedGetChildAccounts200


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetChildAccounts200ResponseDataInner]**](GetChildAccounts200ResponseDataInner.md) |  | [optional] 
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 

## Example

```python
from openapi_client.models.added_get_child_accounts200 import AddedGetChildAccounts200

# TODO update the JSON string below
json = "{}"
# create an instance of AddedGetChildAccounts200 from a JSON string
added_get_child_accounts200_instance = AddedGetChildAccounts200.from_json(json)
# print the JSON string representation of the object
print(AddedGetChildAccounts200.to_json())

# convert the object into a dict
added_get_child_accounts200_dict = added_get_child_accounts200_instance.to_dict()
# create an instance of AddedGetChildAccounts200 from a dict
added_get_child_accounts200_from_dict = AddedGetChildAccounts200.from_dict(added_get_child_accounts200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


