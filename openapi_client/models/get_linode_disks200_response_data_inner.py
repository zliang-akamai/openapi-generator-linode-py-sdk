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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class GetLinodeDisks200ResponseDataInner(BaseModel):
    """
    GetLinodeDisks200ResponseDataInner
    """ # noqa: E501
    created: Optional[datetime] = Field(default=None, description="When this Disk was created.")
    disk_encryption: Optional[StrictStr] = Field(default='enabled', description="Displays if encryption is enabled on this disk. This setting is based on the `disk_encryption` setting of the Linode.")
    filesystem: Optional[StrictStr] = Field(default=None, description="The file system of the disk. This can be `raw`, which indicates no file system, just a raw binary stream, `swap` for a Linux swap area, `ext3` or `ext4` for the ext3 of ext4 journaling file systems for Linux, respectively, or `initrd` for uncompressed initrd, ext2 with a maximum size of 32 MB.")
    id: Optional[StrictInt] = Field(default=None, description="This disk's ID. You need this value to run other operations that interact with the disk.")
    label: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=48)]] = Field(default=None, description="The name of the disk. This is for display purposes only.")
    size: Optional[StrictInt] = Field(default=None, description="The size of the disk in MB.")
    status: Optional[StrictStr] = Field(default=None, description="The current state of the disk.")
    updated: Optional[datetime] = Field(default=None, description="When this disk was last updated.")
    __properties: ClassVar[List[str]] = ["created", "disk_encryption", "filesystem", "id", "label", "size", "status", "updated"]

    @field_validator('filesystem')
    def filesystem_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['raw', 'swap', 'ext3', 'ext4', 'initrd']):
            raise ValueError("must be one of enum values ('raw', 'swap', 'ext3', 'ext4', 'initrd')")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['ready', 'not ready', 'deleting']):
            raise ValueError("must be one of enum values ('ready', 'not ready', 'deleting')")
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
        """Create an instance of GetLinodeDisks200ResponseDataInner from a JSON string"""
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
            "created",
            "disk_encryption",
            "id",
            "status",
            "updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetLinodeDisks200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "disk_encryption": obj.get("disk_encryption") if obj.get("disk_encryption") is not None else 'enabled',
            "filesystem": obj.get("filesystem"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "size": obj.get("size"),
            "status": obj.get("status"),
            "updated": obj.get("updated")
        })
        return _obj


