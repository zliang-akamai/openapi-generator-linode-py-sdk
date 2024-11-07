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
from typing import Optional, Set
from typing_extensions import Self

class GetLkeClusterAcl200ResponseAllOfAclAddresses(BaseModel):
    """
    GetLkeClusterAcl200ResponseAllOfAclAddresses
    """ # noqa: E501
    ipv4: Optional[Any] = None
    ipv6: Optional[Any] = None
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
        """Create an instance of GetLkeClusterAcl200ResponseAllOfAclAddresses from a JSON string"""
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
        # set to None if ipv4 (nullable) is None
        # and model_fields_set contains the field
        if self.ipv4 is None and "ipv4" in self.model_fields_set:
            _dict['ipv4'] = None

        # set to None if ipv6 (nullable) is None
        # and model_fields_set contains the field
        if self.ipv6 is None and "ipv6" in self.model_fields_set:
            _dict['ipv6'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLkeClusterAcl200ResponseAllOfAclAddresses from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ipv4": obj.get("ipv4"),
            "ipv6": obj.get("ipv6")
        })
        return _obj


