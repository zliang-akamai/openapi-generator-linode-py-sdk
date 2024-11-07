# GetTaggedObjects200ResponseDataInnerData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**LinodeAlerts**](LinodeAlerts.md) |  | [optional] 
**backups** | [**LinodeBackups**](LinodeBackups.md) |  | [optional] 
**capabilities** | **List[str]** | A list of capabilities this compute instance supports. | [optional] [readonly] 
**created** | **datetime** | When this NodeBalancer was created. | [optional] [readonly] 
**disk_encryption** | **str** | Indicates the local disk encryption setting for this Linode. If the Linode is part of an LKE cluster, the value is &#x60;null&#x60;. | [optional] [readonly] [default to 'enabled']
**group** | **str** | The group this Domain belongs to.  This is for display purposes only. | [optional] 
**has_user_data** | **bool** | Whether this compute instance was provisioned with &#x60;user_data&#x60; provided via the Metadata service. See the [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) description for more information on Metadata. | [optional] [readonly] 
**host_uuid** | **str** | The Linode&#39;s host machine, as a UUID. | [optional] [readonly] 
**hypervisor** | **str** | The virtualization software powering this Linode. | [optional] [readonly] 
**id** | **int** | This NodeBalancer&#39;s unique ID. | [optional] [readonly] 
**image** | **str** | An Image ID to deploy the Linode Disk from.  Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation with authentication to view all available Images. Official Linode Images start with &#x60;linode/&#x60;, while your Account&#39;s Images start with &#x60;private/&#x60;. Creating a disk from a Private Image requires &#x60;read_only&#x60; or &#x60;read_write&#x60; permissions for that Image. Run the [Update a user&#39;s grants](https://techdocs.akamai.com/linode-api/reference/put-user-grants) operation to adjust permissions for an Account Image. | [optional] 
**ipv4** | **str** | This NodeBalancer&#39;s public IPv4 address. | [optional] [readonly] 
**ipv6** | **str** | This NodeBalancer&#39;s public IPv6 address. | [optional] [readonly] 
**label** | **str** | This NodeBalancer&#39;s label. These must be unique on your Account. | [optional] 
**lke_cluster_id** | **int** | The ID of the Kubernetes cluster if the Linode is part of cluster. | [optional] [readonly] 
**placement_group** | [**Linode1PlacementGroup**](Linode1PlacementGroup.md) |  | [optional] 
**region** | **str** | The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region. | [optional] [readonly] 
**specs** | [**LinodeSpecs**](LinodeSpecs.md) |  | [optional] 
**status** | **str** | The current status of the volume.  Can be one of:    - &#x60;creating&#x60;. The volume is being created and is not yet available for use.   - &#x60;active&#x60;. The volume is online and available for use.   - &#x60;resizing&#x60;. The volume is in the process of upgrading its current capacity.   - &#x60;key_rotating&#x60;. The volume is in the process of rotating encryption keys. Requests to resize, delete, or clone a volume fails during encryption key rotation. | [optional] [readonly] 
**tags** | **List[str]** | An array of Tags applied to this object.  Tags are for organizational purposes only. | [optional] 
**type** | **str** | This is the [Linode type](https://techdocs.akamai.com/linode-api/reference/get-linode-types) that this Linode was deployed with. To change a Linode&#39;s type, use [Resize a Linode](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance). | [optional] [readonly] 
**updated** | **datetime** | When this NodeBalancer was last updated. | [optional] [readonly] 
**watchdog_enabled** | **bool** | The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and reboots it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie gives up if there have been more than 5 boot jobs issued within 15 minutes. | [optional] 
**axfr_ips** | **List[str]** | The list of IPs that may perform a zone transfer for this Domain. The total combined length of all data within this array cannot exceed 1000 characters.  __Note__. This is potentially dangerous, and should be set to an empty list unless you intend to use it. | [optional] 
**description** | **str** | A description for this Domain. This is for display purposes only. | [optional] 
**domain** | **str** | The domain this Domain represents. Domain labels cannot be longer than 63 characters and must conform to [RFC1035](https://tools.ietf.org/html/rfc1035). Domains must be unique on Linode&#39;s platform, including across different Linode accounts; there cannot be two Domains representing the same domain. | [optional] 
**expire_sec** | **int** | The amount of time in seconds that may pass before this Domain is no longer authoritative.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 1209600. | [optional] [default to 0]
**master_ips** | **List[str]** | The IP addresses representing the master DNS for this Domain. At least one value is required for &#x60;type&#x60; slave Domains. The total combined length of all data within this array cannot exceed 1000 characters. | [optional] 
**refresh_sec** | **int** | The amount of time in seconds before this Domain should be refreshed.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 14400. | [optional] [default to 0]
**retry_sec** | **int** | The interval, in seconds, at which a failed refresh should be retried.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200.  - Any other value is rounded up to the nearest valid value.  - A value of 0 is equivalent to the default value of 14400. | [optional] [default to 0]
**soa_email** | **str** | Start of Authority email address. This is required for &#x60;type&#x60; master Domains. | [optional] 
**ttl_sec** | **int** | \&quot;Time to Live\&quot; - the amount of time in seconds that this Domain&#39;s records may be cached by resolvers or other domain servers.  - Valid values are 0, 30, 120, 300, 3600, 7200, 14400, 28800, 57600, 86400, 172800, 345600, 604800, 1209600, and 2419200. - Any other value is rounded up to the nearest valid value. - A value of 0 is equivalent to the default value of 86400. | [optional] [default to 0]
**encryption** | **str** | Displays if encryption is enabled on this volume. | [optional] [readonly] 
**filesystem_path** | **str** | The full filesystem path for the Volume based on the Volume&#39;s label. Path is /dev/disk/by-id/scsi-0Linode_Volume_ + Volume label. | [optional] [readonly] 
**hardware_type** | **str** | The storage type of this Volume. | [optional] [readonly] 
**linode_id** | **int** | If a Volume is attached to a specific Linode, the ID of that Linode will be displayed here. | [optional] 
**linode_label** | **str** | If a Volume is attached to a specific Linode, the label of that Linode will be displayed here. | [optional] [readonly] 
**size** | **int** | The Volume&#39;s size, in GiB. | [optional] 
**client_conn_throttle** | **int** | Throttle connections per second.  Set to 0 (zero) to disable throttling. | [optional] 
**hostname** | **str** | This NodeBalancer&#39;s hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_. | [optional] [readonly] 
**transfer** | [**NodeBalancerTransfer**](NodeBalancerTransfer.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_tagged_objects200_response_data_inner_data import GetTaggedObjects200ResponseDataInnerData

# TODO update the JSON string below
json = "{}"
# create an instance of GetTaggedObjects200ResponseDataInnerData from a JSON string
get_tagged_objects200_response_data_inner_data_instance = GetTaggedObjects200ResponseDataInnerData.from_json(json)
# print the JSON string representation of the object
print(GetTaggedObjects200ResponseDataInnerData.to_json())

# convert the object into a dict
get_tagged_objects200_response_data_inner_data_dict = get_tagged_objects200_response_data_inner_data_instance.to_dict()
# create an instance of GetTaggedObjects200ResponseDataInnerData from a dict
get_tagged_objects200_response_data_inner_data_from_dict = GetTaggedObjects200ResponseDataInnerData.from_dict(get_tagged_objects200_response_data_inner_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


