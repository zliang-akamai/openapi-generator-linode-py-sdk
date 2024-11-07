# GetDomainZone200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_file** | **List[str]** | The lines of the zone file for the last rendered zone for this domain. | [optional] 

## Example

```python
from openapi_client.models.get_domain_zone200_response import GetDomainZone200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainZone200Response from a JSON string
get_domain_zone200_response_instance = GetDomainZone200Response.from_json(json)
# print the JSON string representation of the object
print(GetDomainZone200Response.to_json())

# convert the object into a dict
get_domain_zone200_response_dict = get_domain_zone200_response_instance.to_dict()
# create an instance of GetDomainZone200Response from a dict
get_domain_zone200_response_from_dict = GetDomainZone200Response.from_dict(get_domain_zone200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


