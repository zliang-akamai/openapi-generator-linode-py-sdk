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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LinodeSpecs(BaseModel):
    """
    Information about the resources available to this Linode.
    """ # noqa: E501
    disk: Optional[StrictInt] = Field(default=None, description="The amount of storage space, in MB, this Linode has access to. A typical Linode divides this space between a primary disk with an `image` deployed to it, and a swap disk, usually 512 MB. This is the default configuration created when deploying a Linode with an `image` through [Create a Linode](https://techdocs.akamai.com/linode-api/reference/post-linode-instance). While this configuration is suitable for 99% of use cases, if you need finer control over your Linode's disks, see the [List disks](https://techdocs.akamai.com/linode-api/reference/get-linode-disks) operations.")
    gpus: Optional[StrictInt] = Field(default=None, description="The number of GPUs this Linode has access to.")
    memory: Optional[StrictInt] = Field(default=None, description="The amount of RAM, in MB, this Linode has access to.  Typically, a Linode boots with all of its available RAM, but this can be configured in a config profile. See the [List config profiles](https://techdocs.akamai.com/linode-api/reference/get-linode-configs) operation for more information.")
    transfer: Optional[StrictInt] = Field(default=None, description="The amount of network transfer this Linode is allotted each month.")
    vcpus: Optional[StrictInt] = Field(default=None, description="The number of VCPUs this Linode has access to.")
    __properties: ClassVar[List[str]] = ["disk", "gpus", "memory", "transfer", "vcpus"]

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
        """Create an instance of LinodeSpecs from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "disk",
            "gpus",
            "memory",
            "transfer",
            "vcpus",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LinodeSpecs from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "disk": obj.get("disk"),
            "gpus": obj.get("gpus"),
            "memory": obj.get("memory"),
            "transfer": obj.get("transfer"),
            "vcpus": obj.get("vcpus")
        })
        return _obj


