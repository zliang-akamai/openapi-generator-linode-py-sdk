# AddedGetMaintenance200


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[GetMaintenance200ResponseDataInner]**](GetMaintenance200ResponseDataInner.md) |  | [optional] 
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 

## Example

```python
from openapi_client.models.added_get_maintenance200 import AddedGetMaintenance200

# TODO update the JSON string below
json = "{}"
# create an instance of AddedGetMaintenance200 from a JSON string
added_get_maintenance200_instance = AddedGetMaintenance200.from_json(json)
# print the JSON string representation of the object
print(AddedGetMaintenance200.to_json())

# convert the object into a dict
added_get_maintenance200_dict = added_get_maintenance200_instance.to_dict()
# create an instance of AddedGetMaintenance200 from a dict
added_get_maintenance200_from_dict = AddedGetMaintenance200.from_dict(added_get_maintenance200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


