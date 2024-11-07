# Linode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**LinodeAlerts**](LinodeAlerts.md) |  | [optional] 
**backups** | [**LinodeBackups**](LinodeBackups.md) |  | [optional] 
**capabilities** | **List[str]** | A list of capabilities this compute instance supports. | [optional] [readonly] 
**created** | **datetime** | When this Linode was created. | [optional] [readonly] 
**disk_encryption** | **str** | Indicates the local disk encryption setting for this Linode. If the Linode is part of an LKE cluster, the value is &#x60;null&#x60;. | [optional] [readonly] [default to 'enabled']
**group** | **str** | The group label for this Linode. | [optional] 
**has_user_data** | **bool** | Whether this compute instance was provisioned with &#x60;user_data&#x60; provided via the Metadata service. See the [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) description for more information on Metadata. | [optional] [readonly] 
**host_uuid** | **str** | The Linode&#39;s host machine, as a UUID. | [optional] [readonly] 
**hypervisor** | **str** | The virtualization software powering this Linode. | [optional] [readonly] 
**id** | **int** | This Linode&#39;s ID which must be provided for all operations impacting this Linode. | [optional] [readonly] 
**image** | **str** | An Image ID to deploy the Linode Disk from.  Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation with authentication to view all available Images. Official Linode Images start with &#x60;linode/&#x60;, while your Account&#39;s Images start with &#x60;private/&#x60;. Creating a disk from a Private Image requires &#x60;read_only&#x60; or &#x60;read_write&#x60; permissions for that Image. Run the [Update a user&#39;s grants](https://techdocs.akamai.com/linode-api/reference/put-user-grants) operation to adjust permissions for an Account Image. | [optional] 
**ipv4** | **List[str]** | This Linode&#39;s IPv4 Addresses. Each Linode is assigned a single public IPv4 address upon creation, and may get a single private IPv4 address if needed. You may need to [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to get additional IPv4 addresses.  IPv4 addresses may be reassigned between your Linodes, or shared with other Linodes. See the [networking](https://techdocs.akamai.com/linode-api/reference/post-firewalls) operations for details. | [optional] [readonly] 
**ipv6** | **str** | This Linode&#39;s IPv6 SLAAC address. This address is specific to a Linode, and may not be shared. If the Linode has not been assigned an IPv6 address, the return value will be &#x60;null&#x60;. | [optional] [readonly] 
**label** | **str** | Provides a name for the Linode. If not provided, the API generates one for it.  Linode labels have the following constraints:  - It needs to begin and end with an alphanumeric character. - It can only consist of alphanumeric characters, hyphens (&#x60;-&#x60;), underscores (&#x60;_&#x60;) or periods (&#x60;.&#x60;). - Cannot have two hyphens (&#x60;--&#x60;), underscores (&#x60;__&#x60;) or periods (&#x60;..&#x60;) in a row. | [optional] 
**lke_cluster_id** | **int** | The ID of the Kubernetes cluster if the Linode is part of cluster. | [optional] [readonly] 
**placement_group** | [**LinodePlacementGroup**](LinodePlacementGroup.md) |  | [optional] 
**region** | **str** | The [region](https://techdocs.akamai.com/linode-api/reference/get-regions) where the Linode deployed. A Linode&#39;s region can only be changed by initiating a [cross data center migration](https://techdocs.akamai.com/linode-api/reference/post-migrate-linode-instance). | [optional] [readonly] 
**specs** | [**LinodeSpecs**](LinodeSpecs.md) |  | [optional] 
**status** | **str** | A brief description of the compute instance&#39;s current state. This value can change without direct action from you. For example, when a compute instance goes into maintenance mode, its status is &#x60;stopped&#x60;. Status is generally self-explanatory, based on its name.  - &#x60;busy&#x60; indicates you&#39;ve assigned the compute instance to a [placement group](https://techdocs.akamai.com/cloud-computing/docs/work-with-placement-groups), but the compute instance is currently booting. Once the boot completes, the API completes the assignment and updates the compute instance&#39;s &#x60;status&#x60; accordingly. - &#x60;provisioning&#x60; indicates that the API is applying operating system or Marketplace applications on the compute instance. - &#x60;billing_suspension&#x60; indicates that payment is past due on the compute instance, so we&#39;ve suspended its use. | [optional] [readonly] 
**tags** | **List[str]** | Tags to help you organize your content. | [optional] 
**type** | **str** | This is the [Linode type](https://techdocs.akamai.com/linode-api/reference/get-linode-types) that this Linode was deployed with. To change a Linode&#39;s type, use [Resize a Linode](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance). | [optional] [readonly] 
**updated** | **datetime** | When this Linode was last updated. | [optional] [readonly] 
**watchdog_enabled** | **bool** | The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and reboots it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie gives up if there have been more than 5 boot jobs issued within 15 minutes. | [optional] 

## Example

```python
from openapi_client.models.linode import Linode

# TODO update the JSON string below
json = "{}"
# create an instance of Linode from a JSON string
linode_instance = Linode.from_json(json)
# print the JSON string representation of the object
print(Linode.to_json())

# convert the object into a dict
linode_dict = linode_instance.to_dict()
# create an instance of Linode from a dict
linode_from_dict = Linode.from_dict(linode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


