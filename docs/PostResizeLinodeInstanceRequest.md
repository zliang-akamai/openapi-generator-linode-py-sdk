# PostResizeLinodeInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_auto_disk_resize** | **bool** | Automatically resize disks when resizing a Linode. When resizing down to a smaller plan your Linode&#39;s data must fit within the smaller disk size. | [optional] [default to True]
**migration_type** | **str** | Type of migration used in moving to a new host or Linode type.  &#x60;warm&#x60;: the Linode will not power down until the migration is complete. Warm migrations are not available for DC migrations.  &#x60;cold&#x60;: the Linode will be powered down and migrated. When the migration is complete, the Linode will be powered on. | [optional] [default to 'cold']
**type** | **str** | The ID representing the Linode Type. | 

## Example

```python
from openapi_client.models.post_resize_linode_instance_request import PostResizeLinodeInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostResizeLinodeInstanceRequest from a JSON string
post_resize_linode_instance_request_instance = PostResizeLinodeInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PostResizeLinodeInstanceRequest.to_json())

# convert the object into a dict
post_resize_linode_instance_request_dict = post_resize_linode_instance_request_instance.to_dict()
# create an instance of PostResizeLinodeInstanceRequest from a dict
post_resize_linode_instance_request_from_dict = PostResizeLinodeInstanceRequest.from_dict(post_resize_linode_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


