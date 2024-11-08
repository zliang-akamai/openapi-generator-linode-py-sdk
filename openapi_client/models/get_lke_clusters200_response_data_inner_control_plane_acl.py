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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_lke_clusters200_response_data_inner_control_plane_acl_addresses import GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses
from typing import Optional, Set
from typing_extensions import Self

class GetLkeClusters200ResponseDataInnerControlPlaneAcl(BaseModel):
    """
    When a cluster is equipped with an ACL, the apiserver and dashboard endpoints get mapped to a NodeBalancer address where all traffic is protected through a Cloud Firewall. This object supports required keys `enabled` and `addresses`. Also supports the optional key `revision-id`. If omitted, at discretion of the platform, the cluster may or may not be equipped with ACL support. The Default Policy shall be set to ALLOW (i.e., access controls are disabled). If set to `{}`, default elements are set. __NOTE: Control Plane ACLs may not currently be available to all users.__
    """ # noqa: E501
    addresses: Optional[GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses] = None
    enabled: Optional[StrictBool] = Field(default=None, description="Defines Default Policy.  A value of true results in a default policy of DENY.  A value of false results in a default policy of ALLOW (i.e., access controls are disabled). Defaults to `true`. Creating a cluster with ACL (or upgrading a cluster to use ACL for LKE) is an __irreversible__ change: once upgraded, access controls can only be toggled through this property.")
    revision_id: Optional[StrictStr] = Field(default=None, description="Enables clients to track events related to ACL update requests and enforcements. Optional field. If omitted, defaults to a randomly generated string.", alias="revision-id")
    __properties: ClassVar[List[str]] = ["addresses", "enabled", "revision-id"]

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
        """Create an instance of GetLkeClusters200ResponseDataInnerControlPlaneAcl from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of addresses
        if self.addresses:
            _dict['addresses'] = self.addresses.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLkeClusters200ResponseDataInnerControlPlaneAcl from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "addresses": GetLkeClusters200ResponseDataInnerControlPlaneAclAddresses.from_dict(obj["addresses"]) if obj.get("addresses") is not None else None,
            "enabled": obj.get("enabled"),
            "revision-id": obj.get("revision-id")
        })
        return _obj


