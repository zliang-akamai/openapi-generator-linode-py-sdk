# PostCloneLinodeInstanceRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups_enabled** | **bool** | If this field is set to &#x60;true&#x60;, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. Pricing is included in the response from [List types](https://techdocs.akamai.com/linode-api/reference/get-linode-types).  - Can only be included when cloning to a new Linode. | [optional] 
**configs** | **List[int]** | An array of configuration profile IDs.  - If the &#x60;configs&#x60; parameter __is not provided__, then __all configuration profiles and their associated disks will be cloned__ from the source Linode. Any disks specified by the &#x60;disks&#x60; parameter will also be cloned. - __If an empty array is provided__ for the &#x60;configs&#x60; parameter, then __no configuration profiles (nor their associated disks) will be cloned__ from the source Linode. Any disks specified by the &#x60;disks&#x60; parameter will still be cloned. - __If a non-empty array is provided__ for the &#x60;configs&#x60; parameter, then __the configuration profiles specified in the array (and their associated disks) will be cloned__ from the source Linode. Any disks specified by the &#x60;disks&#x60; parameter will also be cloned. | [optional] 
**disks** | **List[int]** | An array of disk IDs.  - If the &#x60;disks&#x60; parameter __is not provided__, then __no extra disks will be cloned__ from the source Linode. All disks associated with the configuration profiles specified by the &#x60;configs&#x60; parameter will still be cloned. - __If an empty array is provided__ for the &#x60;disks&#x60; parameter, then __no extra disks will be cloned__ from the source Linode. All disks associated with the configuration profiles specified by the &#x60;configs&#x60; parameter will still be cloned. - __If a non-empty array is provided__ for the &#x60;disks&#x60; parameter, then __the disks specified in the array will be cloned__ from the source Linode, in addition to any disks associated with the configuration profiles specified by the &#x60;configs&#x60; parameter. | [optional] 
**group** | **str** | A label used to group Linodes for display. Linodes are not required to have a group. | [optional] 
**label** | **str** | The label to assign this Linode when cloning to a new Linode.  - Can only be provided when cloning to a new Linode. - Defaults to &#x60;linode&#x60;. | [optional] 
**linode_id** | **int** | If an existing Linode is the target for the clone, the ID of that Linode. The existing Linode must have enough resources to accept the clone. | [optional] 
**metadata** | [**PostLinodeInstanceRequestAllOfMetadata**](PostLinodeInstanceRequestAllOfMetadata.md) |  | [optional] 
**placement_group** | [**PostCloneLinodeInstanceRequestPlacementGroup**](PostCloneLinodeInstanceRequestPlacementGroup.md) |  | [optional] 
**private_ip** | **bool** | If true, the created Linode will have private networking enabled and assigned a private IPv4 address.  - Can only be provided when cloning to a new Linode. | [optional] 
**region** | **str** | This is the Region where the Linode will be deployed. To view all available Regions you can deploy to, run [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions).  - Region can only be provided and is required when cloning to a new Linode. | [optional] 
**type** | **str** | A Linode&#39;s Type determines what resources are available to it, including disk space, memory, and virtual cpus. The amounts available to a specific Linode are returned as &#x60;specs&#x60; on the Linode object.  To view all available Linode Types you can deploy with, run [List types](https://techdocs.akamai.com/linode-api/reference/get-linode-types).  - Type can only be provided and is required when cloning to a new Linode. | [optional] 

## Example

```python
from openapi_client.models.post_clone_linode_instance_request import PostCloneLinodeInstanceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostCloneLinodeInstanceRequest from a JSON string
post_clone_linode_instance_request_instance = PostCloneLinodeInstanceRequest.from_json(json)
# print the JSON string representation of the object
print(PostCloneLinodeInstanceRequest.to_json())

# convert the object into a dict
post_clone_linode_instance_request_dict = post_clone_linode_instance_request_instance.to_dict()
# create an instance of PostCloneLinodeInstanceRequest from a dict
post_clone_linode_instance_request_from_dict = PostCloneLinodeInstanceRequest.from_dict(post_clone_linode_instance_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


