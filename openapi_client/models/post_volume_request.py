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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PostVolumeRequest(BaseModel):
    """
    PostVolumeRequest
    """ # noqa: E501
    config_id: Optional[StrictInt] = Field(default=None, description="When creating a Volume attached to a Linode, the ID of the Linode Config to include the new Volume in. This Config must belong to the Linode referenced by `linode_id`. Must _not_ be provided if `linode_id` is not sent. If a `linode_id` is sent without a `config_id`, the volume will be attached:    - to the Linode's only config if it only has one config.   - to the Linode's last used config, if possible.  If no config can be selected for attachment, an error will be returned.")
    encryption: Optional[StrictStr] = Field(default='disabled', description="Enables encryption on the volume. Full disk encryption ensures the data stored on a block storage volume drive is secure. It protects against unauthorized access by keeping the data encrypted if the volume drive is removed from the data center, decommissioned, or disposed of.  The platform automatically manages the encryption and decryption process for you. You can use an encrypted volume the same way as you use a non-encrypted volume.  You can enable or disable disk encryption only when creating new block storage volumes. After a volume is created, the encryption setting can't be changed.")
    label: Annotated[str, Field(min_length=1, strict=True, max_length=32)] = Field(description="The Volume's label, which is also used in the `filesystem_path` of the resulting volume.")
    linode_id: Optional[StrictInt] = Field(default=None, description="The Linode this volume should be attached to upon creation. If not given, the volume will be created without an attachment.")
    region: Optional[StrictStr] = Field(default=None, description="The Region to deploy this Volume in. This is only required if a linode_id is not given.")
    size: Optional[StrictInt] = Field(default=20, description="The initial size of this volume, in GB.  Be aware that volumes may only be resized up after creation.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An array of Tags applied to this object.  Tags are for organizational purposes only.")
    __properties: ClassVar[List[str]] = ["config_id", "encryption", "label", "linode_id", "region", "size", "tags"]

    @field_validator('encryption')
    def encryption_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'disabled']):
            raise ValueError("must be one of enum values ('enabled', 'disabled')")
        return value

    @field_validator('label')
    def label_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^[a-zA-Z]((?!--|__)[a-zA-Z0-9-_])+$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z]((?!--|__)[a-zA-Z0-9-_])+$/")
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
        """Create an instance of PostVolumeRequest from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostVolumeRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "config_id": obj.get("config_id"),
            "encryption": obj.get("encryption") if obj.get("encryption") is not None else 'disabled',
            "label": obj.get("label"),
            "linode_id": obj.get("linode_id"),
            "region": obj.get("region"),
            "size": obj.get("size") if obj.get("size") is not None else 20,
            "tags": obj.get("tags")
        })
        return _obj


