# AccountSettings

Account Settings object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups_enabled** | **bool** | Account-wide backups default.  If &#x60;true&#x60;, all Linodes created will automatically be enrolled in the Backups service.  If &#x60;false&#x60;, Linodes will not be enrolled by default, but may still be enrolled on creation or later. | [optional] 
**longview_subscription** | **str** | The Longview Pro tier you are currently subscribed to. The value must be a [Longview subscription](https://techdocs.akamai.com/linode-api/reference/get-longview-subscriptions) ID or &#x60;null&#x60; for Longview Free. | [optional] [readonly] 
**managed** | **bool** | Our 24/7 incident response service. This robust, multi-homed monitoring system distributes monitoring checks to ensure that your servers remain online and available at all times. Linode Managed can monitor any service or software stack reachable over TCP or HTTP. Once you add a service to Linode Managed, we&#39;ll monitor it for connectivity, response, and total request time. | [optional] [readonly] 
**network_helper** | **bool** | Enables network helper across all users by default for new Linodes and Linode Configs. | [optional] 
**object_storage** | **str** | A string describing the status of this account&#39;s Object Storage service enrollment. | [optional] [readonly] [default to 'disabled']

## Example

```python
from openapi_client.models.account_settings import AccountSettings

# TODO update the JSON string below
json = "{}"
# create an instance of AccountSettings from a JSON string
account_settings_instance = AccountSettings.from_json(json)
# print the JSON string representation of the object
print(AccountSettings.to_json())

# convert the object into a dict
account_settings_dict = account_settings_instance.to_dict()
# create an instance of AccountSettings from a dict
account_settings_from_dict = AccountSettings.from_dict(account_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


