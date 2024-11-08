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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class GetObjectStorageBuckets200ResponseDataInner(BaseModel):
    """
    An Object Storage bucket. You should access this through the [S3 API](https://docs.ceph.com/en/latest/radosgw/s3/#api).
    """ # noqa: E501
    cluster: Optional[StrictStr] = Field(default=None, description="The legacy `clusterId` equivalent for the `regionId` where this bucket lives. The API maintains this for backward compatibility.  > 📘 > > - This value and the `regionId` are interchangeable when used in requests. Best practice is to use the `regionId`. > > - This value is empty for newer regions that don't have a legacy `clusterId`.")
    created: Optional[datetime] = Field(default=None, description="When this bucket was created.")
    hostname: Optional[StrictStr] = Field(default=None, description="The hostname where this bucket can be accessed. This hostname can be accessed through a browser if the bucket is made public.")
    label: Optional[StrictStr] = Field(default=None, description="The name of this bucket.")
    objects: Optional[StrictInt] = Field(default=None, description="The number of objects stored in this bucket.")
    region: Optional[StrictStr] = Field(default=None, description="The `id` of the [region](https://techdocs.akamai.com/linode-api/reference/get-regions) where this Object Storage bucket lives.")
    size: Optional[StrictInt] = Field(default=None, description="The size of the bucket in bytes.")
    __properties: ClassVar[List[str]] = ["cluster", "created", "hostname", "label", "objects", "region", "size"]

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
        """Create an instance of GetObjectStorageBuckets200ResponseDataInner from a JSON string"""
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
        """Create an instance of GetObjectStorageBuckets200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "cluster": obj.get("cluster"),
            "created": obj.get("created"),
            "hostname": obj.get("hostname"),
            "label": obj.get("label"),
            "objects": obj.get("objects"),
            "region": obj.get("region"),
            "size": obj.get("size")
        })
        return _obj


