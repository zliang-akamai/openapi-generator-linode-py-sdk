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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.get_linode_ips200_response_ipv4 import GetLinodeIps200ResponseIpv4
from openapi_client.models.get_linode_ips200_response_ipv6 import GetLinodeIps200ResponseIpv6
from typing import Optional, Set
from typing_extensions import Self

class GetLinodeIps200Response(BaseModel):
    """
    GetLinodeIps200Response
    """ # noqa: E501
    ipv4: Optional[GetLinodeIps200ResponseIpv4] = None
    ipv6: Optional[GetLinodeIps200ResponseIpv6] = None
    __properties: ClassVar[List[str]] = ["ipv4", "ipv6"]

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
        """Create an instance of GetLinodeIps200Response from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of ipv4
        if self.ipv4:
            _dict['ipv4'] = self.ipv4.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ipv6
        if self.ipv6:
            _dict['ipv6'] = self.ipv6.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLinodeIps200Response from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipv4": GetLinodeIps200ResponseIpv4.from_dict(obj["ipv4"]) if obj.get("ipv4") is not None else None,
            "ipv6": GetLinodeIps200ResponseIpv6.from_dict(obj["ipv6"]) if obj.get("ipv6") is not None else None
        })
        return _obj


