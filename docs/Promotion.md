# Promotion

Promotions generally offer a set amount of credit that can be used toward your Linode services, and the promotion expires after a specified date. As well, a monthly cap on the promotional offer is set.  Simply put, a promotion offers a certain amount of credit  month, until either the expiration date is passed, or until the total promotional credit is used, whichever comes first.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credit_monthly_cap** | **str** | The amount available to spend per month. | [optional] 
**credit_remaining** | **str** | The total amount of credit left for this promotion. | [optional] 
**description** | **str** | A detailed description of this promotion. | [optional] 
**expire_dt** | **str** | When this promotion&#39;s credits expire. | [optional] 
**image_url** | **str** | The location of an image for this promotion. | [optional] 
**service_type** | **str** | The service to which this promotion applies. | [optional] 
**summary** | **str** | Short details of this promotion. | [optional] 
**this_month_credit_remaining** | **str** | The amount of credit left for this month for this promotion. | [optional] 

## Example

```python
from openapi_client.models.promotion import Promotion

# TODO update the JSON string below
json = "{}"
# create an instance of Promotion from a JSON string
promotion_instance = Promotion.from_json(json)
# print the JSON string representation of the object
print(Promotion.to_json())

# convert the object into a dict
promotion_dict = promotion_instance.to_dict()
# create an instance of Promotion from a dict
promotion_from_dict = Promotion.from_dict(promotion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


