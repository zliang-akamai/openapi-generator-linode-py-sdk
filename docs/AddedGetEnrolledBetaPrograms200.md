# AddedGetEnrolledBetaPrograms200


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 
**data** | [**List[AddedGetEnrolledBetaPrograms200AllOfData]**](AddedGetEnrolledBetaPrograms200AllOfData.md) |  | [optional] 

## Example

```python
from openapi_client.models.added_get_enrolled_beta_programs200 import AddedGetEnrolledBetaPrograms200

# TODO update the JSON string below
json = "{}"
# create an instance of AddedGetEnrolledBetaPrograms200 from a JSON string
added_get_enrolled_beta_programs200_instance = AddedGetEnrolledBetaPrograms200.from_json(json)
# print the JSON string representation of the object
print(AddedGetEnrolledBetaPrograms200.to_json())

# convert the object into a dict
added_get_enrolled_beta_programs200_dict = added_get_enrolled_beta_programs200_instance.to_dict()
# create an instance of AddedGetEnrolledBetaPrograms200 from a dict
added_get_enrolled_beta_programs200_from_dict = AddedGetEnrolledBetaPrograms200.from_dict(added_get_enrolled_beta_programs200_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


