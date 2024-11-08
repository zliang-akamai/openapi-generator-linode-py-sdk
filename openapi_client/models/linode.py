# coding: utf-8

"""
    Linode API

    [Read the API documentation](https://techdocs.akamai.com/linode-api/reference/api).

    The version of the OpenAPI document: 4.189.2
    Contact: support@linode.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.linode_alerts import LinodeAlerts
from openapi_client.models.linode_backups import LinodeBackups
from openapi_client.models.linode_placement_group import LinodePlacementGroup
from openapi_client.models.linode_specs import LinodeSpecs
from typing import Optional, Set
from typing_extensions import Self

class Linode(BaseModel):
    """
    Linode
    """ # noqa: E501
    alerts: Optional[LinodeAlerts] = None
    backups: Optional[LinodeBackups] = None
    capabilities: Optional[List[StrictStr]] = Field(default=None, description="A list of capabilities this compute instance supports.")
    created: Optional[datetime] = Field(default=None, description="When this Linode was created.")
    disk_encryption: Optional[StrictStr] = Field(default='enabled', description="Indicates the local disk encryption setting for this Linode. If the Linode is part of an LKE cluster, the value is `null`.")
    group: Optional[StrictStr] = Field(default=None, description="The group label for this Linode.")
    has_user_data: Optional[StrictBool] = Field(default=None, description="Whether this compute instance was provisioned with `user_data` provided via the Metadata service. See the [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance) description for more information on Metadata.")
    host_uuid: Optional[StrictStr] = Field(default=None, description="The Linode's host machine, as a UUID.")
    hypervisor: Optional[StrictStr] = Field(default=None, description="The virtualization software powering this Linode.")
    id: Optional[StrictInt] = Field(default=None, description="This Linode's ID which must be provided for all operations impacting this Linode.")
    image: Optional[StrictStr] = Field(default=None, description="An Image ID to deploy the Linode Disk from.  Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation with authentication to view all available Images. Official Linode Images start with `linode/`, while your Account's Images start with `private/`. Creating a disk from a Private Image requires `read_only` or `read_write` permissions for that Image. Run the [Update a user's grants](https://techdocs.akamai.com/linode-api/reference/put-user-grants) operation to adjust permissions for an Account Image.")
    ipv4: Optional[List[StrictStr]] = Field(default=None, description="This Linode's IPv4 Addresses. Each Linode is assigned a single public IPv4 address upon creation, and may get a single private IPv4 address if needed. You may need to [Open a support ticket](https://techdocs.akamai.com/linode-api/reference/post-ticket) to get additional IPv4 addresses.  IPv4 addresses may be reassigned between your Linodes, or shared with other Linodes. See the [networking](https://techdocs.akamai.com/linode-api/reference/post-firewalls) operations for details.")
    ipv6: Optional[StrictStr] = Field(default=None, description="This Linode's IPv6 SLAAC address. This address is specific to a Linode, and may not be shared. If the Linode has not been assigned an IPv6 address, the return value will be `null`.")
    label: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=64)]] = Field(default=None, description="Provides a name for the Linode. If not provided, the API generates one for it.  Linode labels have the following constraints:  - It needs to begin and end with an alphanumeric character. - It can only consist of alphanumeric characters, hyphens (`-`), underscores (`_`) or periods (`.`). - Cannot have two hyphens (`--`), underscores (`__`) or periods (`..`) in a row.")
    lke_cluster_id: Optional[StrictInt] = Field(default=None, description="The ID of the Kubernetes cluster if the Linode is part of cluster.")
    placement_group: Optional[LinodePlacementGroup] = None
    region: Optional[StrictStr] = Field(default=None, description="The [region](https://techdocs.akamai.com/linode-api/reference/get-regions) where the Linode deployed. A Linode's region can only be changed by initiating a [cross data center migration](https://techdocs.akamai.com/linode-api/reference/post-migrate-linode-instance).")
    specs: Optional[LinodeSpecs] = None
    status: Optional[StrictStr] = Field(default=None, description="A brief description of the compute instance's current state. This value can change without direct action from you. For example, when a compute instance goes into maintenance mode, its status is `stopped`. Status is generally self-explanatory, based on its name.  - `busy` indicates you've assigned the compute instance to a [placement group](https://techdocs.akamai.com/cloud-computing/docs/work-with-placement-groups), but the compute instance is currently booting. Once the boot completes, the API completes the assignment and updates the compute instance's `status` accordingly. - `provisioning` indicates that the API is applying operating system or Marketplace applications on the compute instance. - `billing_suspension` indicates that payment is past due on the compute instance, so we've suspended its use.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="Tags to help you organize your content.")
    type: Optional[StrictStr] = Field(default=None, description="This is the [Linode type](https://techdocs.akamai.com/linode-api/reference/get-linode-types) that this Linode was deployed with. To change a Linode's type, use [Resize a Linode](https://techdocs.akamai.com/linode-api/reference/post-resize-linode-instance).")
    updated: Optional[datetime] = Field(default=None, description="When this Linode was last updated.")
    watchdog_enabled: Optional[StrictBool] = Field(default=None, description="The watchdog, named Lassie, is a Shutdown Watchdog that monitors your Linode and reboots it if it powers off unexpectedly. It works by issuing a boot job when your Linode powers off without a shutdown job being responsible. To prevent a loop, Lassie gives up if there have been more than 5 boot jobs issued within 15 minutes.")
    __properties: ClassVar[List[str]] = ["alerts", "backups", "capabilities", "created", "disk_encryption", "group", "has_user_data", "host_uuid", "hypervisor", "id", "image", "ipv4", "ipv6", "label", "lke_cluster_id", "placement_group", "region", "specs", "status", "tags", "type", "updated", "watchdog_enabled"]

    @field_validator('disk_encryption')
    def disk_encryption_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'disabled']):
            raise ValueError("must be one of enum values ('enabled', 'disabled')")
        return value

    @field_validator('hypervisor')
    def hypervisor_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kvm']):
            raise ValueError("must be one of enum values ('kvm')")
        return value

    @field_validator('label')
    def label_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z]((?!--|__|\.\.)[a-zA-Z0-9-_.])+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]((?!--|__|\.\.)[a-zA-Z0-9-_.])+$/")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['running', 'offline', 'booting', 'busy', 'rebooting', 'shutting_down', 'provisioning', 'deleting', 'migrating', 'rebuilding', 'cloning', 'restoring', 'stopped', 'billing_suspension']):
            raise ValueError("must be one of enum values ('running', 'offline', 'booting', 'busy', 'rebooting', 'shutting_down', 'provisioning', 'deleting', 'migrating', 'rebuilding', 'cloning', 'restoring', 'stopped', 'billing_suspension')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of Linode from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "capabilities",
            "created",
            "disk_encryption",
            "has_user_data",
            "host_uuid",
            "hypervisor",
            "id",
            "ipv4",
            "ipv6",
            "lke_cluster_id",
            "region",
            "status",
            "type",
            "updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of alerts
        if self.alerts:
            _dict['alerts'] = self.alerts.to_dict()
        # override the default output from pydantic by calling `to_dict()` of backups
        if self.backups:
            _dict['backups'] = self.backups.to_dict()
        # override the default output from pydantic by calling `to_dict()` of placement_group
        if self.placement_group:
            _dict['placement_group'] = self.placement_group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of specs
        if self.specs:
            _dict['specs'] = self.specs.to_dict()
        # set to None if disk_encryption (nullable) is None
        # and model_fields_set contains the field
        if self.disk_encryption is None and "disk_encryption" in self.model_fields_set:
            _dict['disk_encryption'] = None

        # set to None if ipv6 (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6 is None and "ipv6" in self.model_fields_set:
            _dict['ipv6'] = None

        # set to None if lke_cluster_id (nullable) is None
        # and model_fields_set contains the field
        if self.lke_cluster_id is None and "lke_cluster_id" in self.model_fields_set:
            _dict['lke_cluster_id'] = None

        # set to None if placement_group (nullable) is None
        # and model_fields_set contains the field
        if self.placement_group is None and "placement_group" in self.model_fields_set:
            _dict['placement_group'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Linode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "alerts": LinodeAlerts.from_dict(obj["alerts"]) if obj.get("alerts") is not None else None,
            "backups": LinodeBackups.from_dict(obj["backups"]) if obj.get("backups") is not None else None,
            "capabilities": obj.get("capabilities"),
            "created": obj.get("created"),
            "disk_encryption": obj.get("disk_encryption") if obj.get("disk_encryption") is not None else 'enabled',
            "group": obj.get("group"),
            "has_user_data": obj.get("has_user_data"),
            "host_uuid": obj.get("host_uuid"),
            "hypervisor": obj.get("hypervisor"),
            "id": obj.get("id"),
            "image": obj.get("image"),
            "ipv4": obj.get("ipv4"),
            "ipv6": obj.get("ipv6"),
            "label": obj.get("label"),
            "lke_cluster_id": obj.get("lke_cluster_id"),
            "placement_group": LinodePlacementGroup.from_dict(obj["placement_group"]) if obj.get("placement_group") is not None else None,
            "region": obj.get("region"),
            "specs": LinodeSpecs.from_dict(obj["specs"]) if obj.get("specs") is not None else None,
            "status": obj.get("status"),
            "tags": obj.get("tags"),
            "type": obj.get("type"),
            "updated": obj.get("updated"),
            "watchdog_enabled": obj.get("watchdog_enabled")
        })
        return _obj


