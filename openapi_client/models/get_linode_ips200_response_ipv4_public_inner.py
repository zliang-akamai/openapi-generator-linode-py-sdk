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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_linode_ips200_response_ipv4_public_inner_vpc_nat11 import GetLinodeIps200ResponseIpv4PublicInnerVpcNat11
from typing import Optional, Set
from typing_extensions import Self

class GetLinodeIps200ResponseIpv4PublicInner(BaseModel):
    """
    An IP address that exists in Linode's system, either IPv4 or IPv6.
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="The IP address.")
    gateway: Optional[StrictStr] = Field(default=None, description="The default gateway for this address.")
    linode_id: Optional[StrictInt] = Field(default=None, description="The ID of the Linode this address currently belongs to. For IPv4 addresses, this is by default the Linode that this address was assigned to on creation, and these addresses my be moved using the [Assign IPv4s to Linodes](https://techdocs.akamai.com/linode-api/reference/post-assign-ipv4s) operation. For SLAAC and link-local addresses, this value may not be changed.")
    prefix: Optional[StrictInt] = Field(default=None, description="The number of bits set in the subnet mask.")
    public: Optional[StrictBool] = Field(default=None, description="Whether this is a public or private IP address.")
    rdns: Optional[StrictStr] = Field(default=None, description="The reverse DNS assigned to this address. For public IPv4 addresses, this will be set to a default value provided by Linode if not explicitly set.")
    region: Optional[StrictStr] = Field(default=None, description="The Region this IP address resides in.")
    subnet_mask: Optional[StrictStr] = Field(default=None, description="The mask that separates host bits from network bits for this address.")
    type: Optional[StrictStr] = Field(default=None, description="The type of address this is.")
    vpc_nat_1_1: Optional[GetLinodeIps200ResponseIpv4PublicInnerVpcNat11] = None
    __properties: ClassVar[List[str]] = ["address", "gateway", "linode_id", "prefix", "public", "rdns", "region", "subnet_mask", "type", "vpc_nat_1_1"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ipv4', 'ipv6', 'ipv6/pool', 'ipv6/range']):
            raise ValueError("must be one of enum values ('ipv4', 'ipv6', 'ipv6/pool', 'ipv6/range')")
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
        """Create an instance of GetLinodeIps200ResponseIpv4PublicInner from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "address",
            "gateway",
            "linode_id",
            "prefix",
            "public",
            "region",
            "subnet_mask",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of vpc_nat_1_1
        if self.vpc_nat_1_1:
            _dict['vpc_nat_1_1'] = self.vpc_nat_1_1.to_dict()
        # set to None if gateway (nullable) is None
        # and model_fields_set contains the field
        if self.gateway is None and "gateway" in self.model_fields_set:
            _dict['gateway'] = None

        # set to None if rdns (nullable) is None
        # and model_fields_set contains the field
        if self.rdns is None and "rdns" in self.model_fields_set:
            _dict['rdns'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLinodeIps200ResponseIpv4PublicInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "address": obj.get("address"),
            "gateway": obj.get("gateway"),
            "linode_id": obj.get("linode_id"),
            "prefix": obj.get("prefix"),
            "public": obj.get("public"),
            "rdns": obj.get("rdns"),
            "region": obj.get("region"),
            "subnet_mask": obj.get("subnet_mask"),
            "type": obj.get("type"),
            "vpc_nat_1_1": GetLinodeIps200ResponseIpv4PublicInnerVpcNat11.from_dict(obj["vpc_nat_1_1"]) if obj.get("vpc_nat_1_1") is not None else None
        })
        return _obj

