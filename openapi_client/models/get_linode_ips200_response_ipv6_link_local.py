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
from typing import Optional, Set
from typing_extensions import Self

class GetLinodeIps200ResponseIpv6LinkLocal(BaseModel):
    """
    A link-local IPv6 address that exists in Linode's system.
    """ # noqa: E501
    address: Optional[StrictStr] = Field(default=None, description="The IPv6 link-local address.")
    gateway: Optional[StrictStr] = Field(default=None, description="The default gateway for this address.")
    linode_id: Optional[StrictInt] = Field(default=None, description="The ID of the Linode this address currently belongs to.")
    prefix: Optional[StrictInt] = Field(default=None, description="The network prefix.")
    public: Optional[StrictBool] = Field(default=None, description="Whether this is a public or private IP address.")
    rdns: Optional[StrictStr] = Field(default=None, description="The reverse DNS assigned to this address.")
    region: Optional[StrictStr] = Field(default=None, description="The Region this address resides in.")
    subnet_mask: Optional[StrictStr] = Field(default=None, description="The subnet mask.")
    type: Optional[StrictStr] = Field(default=None, description="The type of address this is.")
    __properties: ClassVar[List[str]] = ["address", "gateway", "linode_id", "prefix", "public", "rdns", "region", "subnet_mask", "type"]

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
        """Create an instance of GetLinodeIps200ResponseIpv6LinkLocal from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLinodeIps200ResponseIpv6LinkLocal from a dict"""
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
            "type": obj.get("type")
        })
        return _obj


