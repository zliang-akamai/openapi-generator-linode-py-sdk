# PostSnapshotRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** | The label for the new snapshot. | 

## Example

```python
from openapi_client.models.post_snapshot_request import PostSnapshotRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostSnapshotRequest from a JSON string
post_snapshot_request_instance = PostSnapshotRequest.from_json(json)
# print the JSON string representation of the object
print(PostSnapshotRequest.to_json())

# convert the object into a dict
post_snapshot_request_dict = post_snapshot_request_instance.to_dict()
# create an instance of PostSnapshotRequest from a dict
post_snapshot_request_from_dict = PostSnapshotRequest.from_dict(post_snapshot_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


