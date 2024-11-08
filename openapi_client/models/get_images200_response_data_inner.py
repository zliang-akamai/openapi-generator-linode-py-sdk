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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.get_images200_response_data_inner_regions_inner import GetImages200ResponseDataInnerRegionsInner
from typing import Optional, Set
from typing_extensions import Self

class GetImages200ResponseDataInner(BaseModel):
    """
    Image object.
    """ # noqa: E501
    capabilities: Optional[List[StrictStr]] = Field(default=None, description="A list of the possible capabilities of this image.  - `cloud-init`. The image supports the cloud-init multi-distribution method with our [Metadata service](https://www.linode.com/docs/products/compute/compute-instances/guides/metadata/#troubleshoot-metadata-and-cloud-init). This only applies to public images.  - `distributed-sites`. Whether the image can be used in distributed compute regions. Compared to a core compute region, distributed compute regions offer limited functionality, but they're globally distributed. Your image can be geographically closer to you, potentially letting you deploy it quicker. See [Regions and images](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-images) for complete details.")
    created: Optional[datetime] = Field(default=None, description="When this image was created.")
    created_by: Optional[StrictStr] = Field(default=None, description="The name of the user who created this image, or `linode` for public images.")
    deprecated: Optional[StrictBool] = Field(default=None, description="Whether this image is deprecated. Only public images can be deprecated.")
    description: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=65000)]] = Field(default=None, description="A detailed description of this image.")
    eol: Optional[datetime] = Field(default=None, description="The date of the public image's planned removal from service. This is `null` for private images.")
    expiry: Optional[datetime] = Field(default=None, description="Only images created automatically from a deleted compute instance (type=automatic) expire. This is `null` for private images.")
    id: Optional[StrictStr] = Field(default=None, description="The unique identifier for each image.")
    is_public: Optional[StrictBool] = Field(default=None, description="Revealed as `true` if the image is a public distribution image. Private, account-specific images are listed as `false`.")
    label: Optional[StrictStr] = Field(default=None, description="A short description of the image.")
    regions: Optional[List[GetImages200ResponseDataInnerRegionsInner]] = Field(default=None, description="Details on the regions where this image is stored. See [Regions and images](https://techdocs.akamai.com/cloud-computing/docs/images#regions-and-images) for full details on support for `regions`.")
    size: Optional[StrictInt] = Field(default=None, description="The minimum size in MB this image needs to deploy.")
    status: Optional[StrictStr] = Field(default=None, description="The current status of the image. Possible values are `available`, `creating`, and `pending_upload`.  > 📘 > > The `+order_by` and `+order` operators are not available when [filtering](https://techdocs.akamai.com/linode-api/reference/filtering-and-sorting) on this key.")
    tags: Optional[Annotated[List[Annotated[str, Field(min_length=3, strict=True, max_length=100)]], Field(min_length=0, max_length=500)]] = Field(default=None, description="Tags used for organizational purposes. A tag can be from 3 to 100 characters long, and an image can have a maximum of 500 total tags.")
    total_size: Optional[StrictInt] = Field(default=None, description="The total size in bytes of all instances of this image, in all `regions`.  > 📘 > > This object is empty for existing images. It's intended for use with future functionality.")
    type: Optional[StrictStr] = Field(default=None, description="How the image was created. Create a `manual` image at any time. An `automatic` image is created automatically from a deleted compute instance.")
    updated: Optional[datetime] = Field(default=None, description="When this image was last updated.")
    vendor: Optional[StrictStr] = Field(default=None, description="The upstream distribution vendor. This is `null` for private images.")
    __properties: ClassVar[List[str]] = ["capabilities", "created", "created_by", "deprecated", "description", "eol", "expiry", "id", "is_public", "label", "regions", "size", "status", "tags", "total_size", "type", "updated", "vendor"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['creating', 'pending_upload', 'available']):
            raise ValueError("must be one of enum values ('creating', 'pending_upload', 'available')")
        return value

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['manual', 'automatic']):
            raise ValueError("must be one of enum values ('manual', 'automatic')")
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
        """Create an instance of GetImages200ResponseDataInner from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "capabilities",
            "created",
            "created_by",
            "deprecated",
            "eol",
            "expiry",
            "id",
            "is_public",
            "regions",
            "size",
            "status",
            "total_size",
            "type",
            "updated",
            "vendor",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in regions (list)
        _items = []
        if self.regions:
            for _item_regions in self.regions:
                if _item_regions:
                    _items.append(_item_regions.to_dict())
            _dict['regions'] = _items
        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if eol (nullable) is None
        # and model_fields_set contains the field
        if self.eol is None and "eol" in self.model_fields_set:
            _dict['eol'] = None

        # set to None if expiry (nullable) is None
        # and model_fields_set contains the field
        if self.expiry is None and "expiry" in self.model_fields_set:
            _dict['expiry'] = None

        # set to None if vendor (nullable) is None
        # and model_fields_set contains the field
        if self.vendor is None and "vendor" in self.model_fields_set:
            _dict['vendor'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetImages200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "capabilities": obj.get("capabilities"),
            "created": obj.get("created"),
            "created_by": obj.get("created_by"),
            "deprecated": obj.get("deprecated"),
            "description": obj.get("description"),
            "eol": obj.get("eol"),
            "expiry": obj.get("expiry"),
            "id": obj.get("id"),
            "is_public": obj.get("is_public"),
            "label": obj.get("label"),
            "regions": [GetImages200ResponseDataInnerRegionsInner.from_dict(_item) for _item in obj["regions"]] if obj.get("regions") is not None else None,
            "size": obj.get("size"),
            "status": obj.get("status"),
            "tags": obj.get("tags"),
            "total_size": obj.get("total_size"),
            "type": obj.get("type"),
            "updated": obj.get("updated"),
            "vendor": obj.get("vendor")
        })
        return _obj


