# GetClients200ResponseDataInner

A third-party application registered to Linode that users may log into with their Linode account through our authentication server at [login.linode.com](https://login.linode.com).  Using an OAuth Client, a third-party developer may be given access to some, or all, of a User's account for the purposes of their application.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The OAuth Client ID.  This is used to identify the client, and is a publicly known value (it is not a secret). | [optional] [readonly] 
**label** | **str** | The name of this application.  This will be presented to users when they are asked to grant it access to their Account. | [optional] 
**public** | **bool** | If this is a public or private OAuth Client.  Public clients have a slightly different authentication workflow than private clients.  See the [OAuth spec](https://oauth.net/2/) for more details. | [optional] [default to False]
**redirect_uri** | **str** | The location a successful log in from [login.linode.com](https://login.linode.com) should be redirected to for this client.  The receiver of this redirect should be ready to accept an OAuth exchange code and finish the OAuth exchange. | [optional] 
**secret** | **str** | The OAuth Client secret, used in the OAuth exchange.  This is returned as &#x60;&lt;REDACTED&gt;&#x60; except when an OAuth Client is created or its secret is reset.  This is a secret, and should not be shared or disclosed publicly. | [optional] [readonly] 
**status** | **str** | The status of this application.  &#x60;active&#x60; by default. | [optional] [readonly] 
**thumbnail_url** | **str** | The URL where this client&#39;s thumbnail may be viewed, or &#x60;null&#x60; if this client does not have a thumbnail set. | [optional] [readonly] 

## Example

```python
from openapi_client.models.get_clients200_response_data_inner import GetClients200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetClients200ResponseDataInner from a JSON string
get_clients200_response_data_inner_instance = GetClients200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(GetClients200ResponseDataInner.to_json())

# convert the object into a dict
get_clients200_response_data_inner_dict = get_clients200_response_data_inner_instance.to_dict()
# create an instance of GetClients200ResponseDataInner from a dict
get_clients200_response_data_inner_from_dict = GetClients200ResponseDataInner.from_dict(get_clients200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


