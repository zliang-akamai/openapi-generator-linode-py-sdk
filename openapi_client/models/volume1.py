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

class Volume1(BaseModel):
    """
    A Block Storage Volume associated with your Account.
    """ # noqa: E501
    created: Optional[datetime] = Field(default=None, description="When this Volume was created.")
    encryption: Optional[StrictStr] = Field(default=None, description="Displays if encryption is enabled on this volume.")
    filesystem_path: Optional[StrictStr] = Field(default=None, description="The full filesystem path for the Volume based on the Volume's label. Path is /dev/disk/by-id/scsi-0Linode_Volume_ + Volume label.")
    hardware_type: Optional[StrictStr] = Field(default=None, description="The storage type of this Volume.")
    id: Optional[StrictInt] = Field(default=None, description="The unique ID of this Volume.")
    label: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=32)]] = Field(default=None, description="The Volume's label is for display purposes only.")
    linode_id: Optional[StrictInt] = Field(default=None, description="If a Volume is attached to a specific Linode, the ID of that Linode will be displayed here.")
    linode_label: Optional[StrictStr] = Field(default=None, description="If a Volume is attached to a specific Linode, the label of that Linode will be displayed here.")
    region: Optional[StrictStr] = Field(default=None, description="The unique ID of this Region.")
    size: Optional[Annotated[int, Field(le=10240, strict=True)]] = Field(default=None, description="The Volume's size, in GiB.")
    status: Optional[StrictStr] = Field(default=None, description="The current status of the volume.  Can be one of:    - `creating`. The volume is being created and is not yet available for use.   - `active`. The volume is online and available for use.   - `resizing`. The volume is in the process of upgrading its current capacity.   - `key_rotating`. The volume is in the process of rotating encryption keys. Requests to resize, delete, or clone a volume fails during encryption key rotation.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An array of Tags applied to this object.  Tags are for organizational purposes only.")
    updated: Optional[datetime] = Field(default=None, description="When this Volume was last updated.")
    __properties: ClassVar[List[str]] = ["created", "encryption", "filesystem_path", "hardware_type", "id", "label", "linode_id", "linode_label", "region", "size", "status", "tags", "updated"]

    @field_validator('encryption')
    def encryption_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'disabled']):
            raise ValueError("must be one of enum values ('enabled', 'disabled')")
        return value

    @field_validator('hardware_type')
    def hardware_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['hdd', 'nvme']):
            raise ValueError("must be one of enum values ('hdd', 'nvme')")
        return value

    @field_validator('label')
    def label_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z]((?!--|__)[a-zA-Z0-9-_])+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]((?!--|__)[a-zA-Z0-9-_])+$/")
        return value

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['creating', 'active', 'resizing', 'key_rotating']):
            raise ValueError("must be one of enum values ('creating', 'active', 'resizing', 'key_rotating')")
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
        """Create an instance of Volume1 from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "created",
            "encryption",
            "filesystem_path",
            "hardware_type",
            "id",
            "linode_label",
            "region",
            "status",
            "updated",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if linode_id (nullable) is None
        # and model_fields_set contains the field
        if self.linode_id is None and "linode_id" in self.model_fields_set:
            _dict['linode_id'] = None

        # set to None if linode_label (nullable) is None
        # and model_fields_set contains the field
        if self.linode_label is None and "linode_label" in self.model_fields_set:
            _dict['linode_label'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Volume1 from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "encryption": obj.get("encryption"),
            "filesystem_path": obj.get("filesystem_path"),
            "hardware_type": obj.get("hardware_type"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "linode_id": obj.get("linode_id"),
            "linode_label": obj.get("linode_label"),
            "region": obj.get("region"),
            "size": obj.get("size"),
            "status": obj.get("status"),
            "tags": obj.get("tags"),
            "updated": obj.get("updated")
        })
        return _obj


