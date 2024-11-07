# PaginationEnvelope

An envelope for paginated response. When accessing a collection through a GET endpoint, the results are wrapped in this envelope which includes metadata about those results. Results are presented within a `data` array. See [Pagination](https://techdocs.akamai.com/linode-api/reference/pagination) for more information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **int** | The current [page](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**pages** | **int** | The total number of [pages](https://techdocs.akamai.com/linode-api/reference/pagination). | [optional] [readonly] 
**results** | **int** | The total number of results. | [optional] [readonly] 

## Example

```python
from openapi_client.models.pagination_envelope import PaginationEnvelope

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationEnvelope from a JSON string
pagination_envelope_instance = PaginationEnvelope.from_json(json)
# print the JSON string representation of the object
print(PaginationEnvelope.to_json())

# convert the object into a dict
pagination_envelope_dict = pagination_envelope_instance.to_dict()
# create an instance of PaginationEnvelope from a dict
pagination_envelope_from_dict = PaginationEnvelope.from_dict(pagination_envelope_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


