# PostMigrateLinodeInstanceRequestPlacementGroup

Include this to assign this Linode to an existing [placement group](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/) in the data center you're migrating to. These constraints apply:  - If the target Linode is in a placement group, it will be removed from it when migrating. - The target placement group needs to be in the same `region` you're migrating to. - The target placement group needs to have capacity. Run the [Get a region](https://techdocs.akamai.com/linode-api/reference/get-region) operation for the region you want to migrate to, and store the `maximum_linodes_per_pg` value. Run the [Get a placement group](https://techdocs.akamai.com/linode-api/reference/get-placement-group) operation for that same region to review how many Linodes are in that group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The placement group&#39;s ID. You need to provide it for all operations that affect it. | 

## Example

```python
from openapi_client.models.post_migrate_linode_instance_request_placement_group import PostMigrateLinodeInstanceRequestPlacementGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PostMigrateLinodeInstanceRequestPlacementGroup from a JSON string
post_migrate_linode_instance_request_placement_group_instance = PostMigrateLinodeInstanceRequestPlacementGroup.from_json(json)
# print the JSON string representation of the object
print(PostMigrateLinodeInstanceRequestPlacementGroup.to_json())

# convert the object into a dict
post_migrate_linode_instance_request_placement_group_dict = post_migrate_linode_instance_request_placement_group_instance.to_dict()
# create an instance of PostMigrateLinodeInstanceRequestPlacementGroup from a dict
post_migrate_linode_instance_request_placement_group_from_dict = PostMigrateLinodeInstanceRequestPlacementGroup.from_dict(post_migrate_linode_instance_request_placement_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


