# PostMutateLinodeInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_auto_disk_resize** | **bool** | Automatically resize disks when resizing a Linode. When resizing down to a smaller plan your Linode&#39;s data must fit within the smaller disk size. | [optional] [default to True]

## Example

```python
from openapi_client.models.post_mutate_linode_instance_request import PostMutateLinodeInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostMutateLinodeInstanceRequest from a JSON string
post_mutate_linode_instance_request_instance = PostMutateLinodeInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PostMutateLinodeInstanceRequest.to_json())

# convert the object into a dict
post_mutate_linode_instance_request_dict = post_mutate_linode_instance_request_instance.to_dict()
# create an instance of PostMutateLinodeInstanceRequest from a dict
post_mutate_linode_instance_request_from_dict = PostMutateLinodeInstanceRequest.from_dict(post_mutate_linode_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


