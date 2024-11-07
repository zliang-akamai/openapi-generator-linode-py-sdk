# PostCloneLinodeInstanceRequestPlacementGroup

Include this to assign this Linode to an existing [placement group](https://www.linode.com/docs/products/compute/compute-instances/guides/placement-groups/). Consider these points when cloning:  - If the Linode you're cloning exists in a placement group, the API won't automatically add the cloned instance to the same placement group. You need to specify a placement group to add the clone to. - The target placement group needs to be in the same `region` set for this Linode. - The placement group needs to have capacity. Run the [Get a region](https://techdocs.akamai.com/linode-api/reference/get-region) operation and store the `maximum_linodes_per_pg` value to know the Linode limit per placement group. You can then run the [Get a placement group](https://techdocs.akamai.com/linode-api/reference/get-placement-group) operation to review the Linodes in that group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The placement group&#39;s ID. You need to provide it for all operations that affect it. | 

## Example

```python
from openapi_client.models.post_clone_linode_instance_request_placement_group import PostCloneLinodeInstanceRequestPlacementGroup

# TODO update the JSON string below
json = "{}"
# create an instance of PostCloneLinodeInstanceRequestPlacementGroup from a JSON string
post_clone_linode_instance_request_placement_group_instance = PostCloneLinodeInstanceRequestPlacementGroup.from_json(json)
# print the JSON string representation of the object
print(PostCloneLinodeInstanceRequestPlacementGroup.to_json())

# convert the object into a dict
post_clone_linode_instance_request_placement_group_dict = post_clone_linode_instance_request_placement_group_instance.to_dict()
# create an instance of PostCloneLinodeInstanceRequestPlacementGroup from a dict
post_clone_linode_instance_request_placement_group_from_dict = PostCloneLinodeInstanceRequestPlacementGroup.from_dict(post_clone_linode_instance_request_placement_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

