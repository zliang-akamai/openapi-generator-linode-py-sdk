# GetAccountAgreements200Response

Acknowledgment status for agreements on your account. When acknowledging any agreements, set them to `true` and omit any remainders.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eu_model** | **bool** | The acknowledgement status for the [cross-border data transfer](https://www.akamai.com/legal/compliance/privacy-trust-center/cross-border-data-transfer-statement) agreement. | [optional] 
**master_service_agreement** | **bool** | The acknowledgement status for Akamai&#39;s [master service agreement](https://www.linode.com/legal-msa/). | [optional] 
**privacy_policy** | **bool** | The acknowledgement status for Akamai&#39;s [privacy statement](https://www.akamai.com/legal/privacy-statement). | [optional] 

## Example

```python
from openapi_client.models.get_account_agreements200_response import GetAccountAgreements200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAccountAgreements200Response from a JSON string
get_account_agreements200_response_instance = GetAccountAgreements200Response.from_json(json)
# print the JSON string representation of the object
print(GetAccountAgreements200Response.to_json())

# convert the object into a dict
get_account_agreements200_response_dict = get_account_agreements200_response_instance.to_dict()
# create an instance of GetAccountAgreements200Response from a dict
get_account_agreements200_response_from_dict = GetAccountAgreements200Response.from_dict(get_account_agreements200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


