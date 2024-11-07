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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_linode_ips200_response_ipv6_global_inner import GetLinodeIps200ResponseIpv6GlobalInner
from openapi_client.models.get_linode_ips200_response_ipv6_link_local import GetLinodeIps200ResponseIpv6LinkLocal
from openapi_client.models.get_linode_ips200_response_ipv6_slaac import GetLinodeIps200ResponseIpv6Slaac
from typing import Optional, Set
from typing_extensions import Self

class GetLinodeIps200ResponseIpv6(BaseModel):
    """
    Information about this Linode's IPv6 addresses.
    """ # noqa: E501
    var_global: Optional[List[GetLinodeIps200ResponseIpv6GlobalInner]] = Field(default=None, description="A list of IPv6 range objects assigned to this Linode.", alias="global")
    link_local: Optional[GetLinodeIps200ResponseIpv6LinkLocal] = None
    slaac: Optional[GetLinodeIps200ResponseIpv6Slaac] = None
    __properties: ClassVar[List[str]] = ["global", "link_local", "slaac"]

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
        """Create an instance of GetLinodeIps200ResponseIpv6 from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in var_global (list)
        _items = []
        if self.var_global:
            for _item_var_global in self.var_global:
                if _item_var_global:
                    _items.append(_item_var_global.to_dict())
            _dict['global'] = _items
        # override the default output from pydantic by calling `to_dict()` of link_local
        if self.link_local:
            _dict['link_local'] = self.link_local.to_dict()
        # override the default output from pydantic by calling `to_dict()` of slaac
        if self.slaac:
            _dict['slaac'] = self.slaac.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLinodeIps200ResponseIpv6 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "global": [GetLinodeIps200ResponseIpv6GlobalInner.from_dict(_item) for _item in obj["global"]] if obj.get("global") is not None else None,
            "link_local": GetLinodeIps200ResponseIpv6LinkLocal.from_dict(obj["link_local"]) if obj.get("link_local") is not None else None,
            "slaac": GetLinodeIps200ResponseIpv6Slaac.from_dict(obj["slaac"]) if obj.get("slaac") is not None else None
        })
        return _obj

