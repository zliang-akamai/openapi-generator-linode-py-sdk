# PostLinodeInstanceRequestAllOfMetadata

An object containing user-defined data relevant to the creation of Linodes.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_data** | **bytearray** | Base64-encoded [cloud-config](https://www.linode.com/docs/products/compute/compute-instances/guides/metadata-cloud-config/) data.  Cannot be modified after provisioning. To update, use either the [Clone a Linode](https://techdocs.akamai.com/linode-api/reference/post-clone-linode-instance) or [Rebuild a Linode](https://techdocs.akamai.com/linode-api/reference/post-rebuild-linode-instance) operations.  Must not be included when cloning to an existing Linode.  Unencoded data must not exceed 65535 bytes, or about 16kb encoded. | [optional] 

## Example

```python
from openapi_client.models.post_linode_instance_request_all_of_metadata import PostLinodeInstanceRequestAllOfMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of PostLinodeInstanceRequestAllOfMetadata from a JSON string
post_linode_instance_request_all_of_metadata_instance = PostLinodeInstanceRequestAllOfMetadata.from_json(json)
# print the JSON string representation of the object
print(PostLinodeInstanceRequestAllOfMetadata.to_json())

# convert the object into a dict
post_linode_instance_request_all_of_metadata_dict = post_linode_instance_request_all_of_metadata_instance.to_dict()
# create an instance of PostLinodeInstanceRequestAllOfMetadata from a dict
post_linode_instance_request_all_of_metadata_from_dict = PostLinodeInstanceRequestAllOfMetadata.from_dict(post_linode_instance_request_all_of_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


