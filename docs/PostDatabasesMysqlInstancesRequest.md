# PostDatabasesMysqlInstancesRequest

Managed MySQL Database request object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_list** | **List[str]** | A list of IP addresses that can access the Managed Database. Each item can be a single IP address or a range in CIDR format.  By default, this is an empty array (&#x60;[]&#x60;), which blocks all connections (both public and private) to the Managed Database.  If &#x60;0.0.0.0/0&#x60; is a value in this list, then all IP addresses can access the Managed Database. | [optional] 
**cluster_size** | **int** | The number of Linode Instance nodes deployed to the Managed Database.  Choosing 3 nodes creates a high availability cluster consisting of 1 primary node and 2 replica nodes. | [optional] [default to 1]
**encrypted** | **bool** | Whether the Managed Databases is encrypted. | [optional] [default to False]
**engine** | **str** | The Managed Database engine in engine/version format. | 
**label** | **str** | A unique, user-defined string referring to the Managed Database. | 
**region** | **str** | The [Region](https://techdocs.akamai.com/linode-api/reference/get-regions) ID for the Managed Database. | 
**replication_type** | **str** | The replication method used for the Managed Database.  Defaults to &#x60;none&#x60; for a single cluster and &#x60;semi_synch&#x60; for a high availability cluster.  Must be &#x60;none&#x60; for a single node cluster.  Must be &#x60;asynch&#x60; or &#x60;semi_synch&#x60; for a high availability cluster. | [optional] 
**ssl_connection** | **bool** | Whether to require SSL credentials to establish a connection to the Managed Database.  Run the [Get managed MySQL database credentials](https://techdocs.akamai.com/linode-api/reference/get-databases-mysql-instance-credentials) operation for access information. | [optional] [default to True]
**type** | **str** | The Linode Instance type used by the Managed Database for its nodes. | 

## Example

```python
from openapi_client.models.post_databases_mysql_instances_request import PostDatabasesMysqlInstancesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PostDatabasesMysqlInstancesRequest from a JSON string
post_databases_mysql_instances_request_instance = PostDatabasesMysqlInstancesRequest.from_json(json)
# print the JSON string representation of the object
print(PostDatabasesMysqlInstancesRequest.to_json())

# convert the object into a dict
post_databases_mysql_instances_request_dict = post_databases_mysql_instances_request_instance.to_dict()
# create an instance of PostDatabasesMysqlInstancesRequest from a dict
post_databases_mysql_instances_request_from_dict = PostDatabasesMysqlInstancesRequest.from_dict(post_databases_mysql_instances_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


