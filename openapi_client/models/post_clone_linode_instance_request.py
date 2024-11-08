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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.post_clone_linode_instance_request_placement_group import PostCloneLinodeInstanceRequestPlacementGroup
from openapi_client.models.post_linode_instance_request_all_of_metadata import PostLinodeInstanceRequestAllOfMetadata
from typing import Optional, Set
from typing_extensions import Self

class PostCloneLinodeInstanceRequest(BaseModel):
    """
    PostCloneLinodeInstanceRequest
    """ # noqa: E501
    backups_enabled: Optional[StrictBool] = Field(default=None, description="If this field is set to `true`, the created Linode will automatically be enrolled in the Linode Backup service. This will incur an additional charge. Pricing is included in the response from [List types](https://techdocs.akamai.com/linode-api/reference/get-linode-types).  - Can only be included when cloning to a new Linode.")
    configs: Optional[List[StrictInt]] = Field(default=None, description="An array of configuration profile IDs.  - If the `configs` parameter __is not provided__, then __all configuration profiles and their associated disks will be cloned__ from the source Linode. Any disks specified by the `disks` parameter will also be cloned. - __If an empty array is provided__ for the `configs` parameter, then __no configuration profiles (nor their associated disks) will be cloned__ from the source Linode. Any disks specified by the `disks` parameter will still be cloned. - __If a non-empty array is provided__ for the `configs` parameter, then __the configuration profiles specified in the array (and their associated disks) will be cloned__ from the source Linode. Any disks specified by the `disks` parameter will also be cloned.")
    disks: Optional[List[StrictInt]] = Field(default=None, description="An array of disk IDs.  - If the `disks` parameter __is not provided__, then __no extra disks will be cloned__ from the source Linode. All disks associated with the configuration profiles specified by the `configs` parameter will still be cloned. - __If an empty array is provided__ for the `disks` parameter, then __no extra disks will be cloned__ from the source Linode. All disks associated with the configuration profiles specified by the `configs` parameter will still be cloned. - __If a non-empty array is provided__ for the `disks` parameter, then __the disks specified in the array will be cloned__ from the source Linode, in addition to any disks associated with the configuration profiles specified by the `configs` parameter.")
    group: Optional[StrictStr] = Field(default=None, description="A label used to group Linodes for display. Linodes are not required to have a group.")
    label: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=64)]] = Field(default=None, description="The label to assign this Linode when cloning to a new Linode.  - Can only be provided when cloning to a new Linode. - Defaults to `linode`.")
    linode_id: Optional[StrictInt] = Field(default=None, description="If an existing Linode is the target for the clone, the ID of that Linode. The existing Linode must have enough resources to accept the clone.")
    metadata: Optional[PostLinodeInstanceRequestAllOfMetadata] = None
    placement_group: Optional[PostCloneLinodeInstanceRequestPlacementGroup] = None
    private_ip: Optional[StrictBool] = Field(default=None, description="If true, the created Linode will have private networking enabled and assigned a private IPv4 address.  - Can only be provided when cloning to a new Linode.")
    region: Optional[StrictStr] = Field(default=None, description="This is the Region where the Linode will be deployed. To view all available Regions you can deploy to, run [List regions](https://techdocs.akamai.com/linode-api/reference/get-regions).  - Region can only be provided and is required when cloning to a new Linode.")
    type: Optional[StrictStr] = Field(default=None, description="A Linode's Type determines what resources are available to it, including disk space, memory, and virtual cpus. The amounts available to a specific Linode are returned as `specs` on the Linode object.  To view all available Linode Types you can deploy with, run [List types](https://techdocs.akamai.com/linode-api/reference/get-linode-types).  - Type can only be provided and is required when cloning to a new Linode.")
    __properties: ClassVar[List[str]] = ["backups_enabled", "configs", "disks", "group", "label", "linode_id", "metadata", "placement_group", "private_ip", "region", "type"]

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
        """Create an instance of PostCloneLinodeInstanceRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of placement_group
        if self.placement_group:
            _dict['placement_group'] = self.placement_group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostCloneLinodeInstanceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "backups_enabled": obj.get("backups_enabled"),
            "configs": obj.get("configs"),
            "disks": obj.get("disks"),
            "group": obj.get("group"),
            "label": obj.get("label"),
            "linode_id": obj.get("linode_id"),
            "metadata": PostLinodeInstanceRequestAllOfMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "placement_group": PostCloneLinodeInstanceRequestPlacementGroup.from_dict(obj["placement_group"]) if obj.get("placement_group") is not None else None,
            "private_ip": obj.get("private_ip"),
            "region": obj.get("region"),
            "type": obj.get("type")
        })
        return _obj


