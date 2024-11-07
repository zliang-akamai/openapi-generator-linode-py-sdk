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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.post_linode_instance_request_all_of_metadata import PostLinodeInstanceRequestAllOfMetadata
from typing import Optional, Set
from typing_extensions import Self

class PostRebuildLinodeInstanceRequest(BaseModel):
    """
    PostRebuildLinodeInstanceRequest
    """ # noqa: E501
    authorized_keys: Optional[List[StrictStr]] = Field(default=None, description="A list of public SSH keys that will be automatically appended to the root user's `~/.ssh/authorized_keys` file when deploying from an Image.")
    authorized_users: Optional[List[StrictStr]] = Field(default=None, description="A list of usernames. If the usernames have associated SSH keys, the keys will be appended to the root users `~/.ssh/authorized_keys` file automatically when deploying from an Image.")
    booted: Optional[StrictBool] = Field(default=True, description="This field defaults to `true` if the Linode is created with an Image or from a Backup. If it is deployed from an Image or a Backup and you wish it to remain `offline` after deployment, set this to `false`.")
    disk_encryption: Optional[StrictStr] = Field(default=None, description="Local disk encryption ensures that your data stored on Linodes is secured. Disk encryption protects against unauthorized data access by keeping the data encrypted if the disk is ever removed from the data center, decommissioned, or disposed of. The platform manages the encryption and decryption for you.  By default, encryption is `enabled` on all Linodes. If you opted out of encryption or if the Linode was created prior to local disk encryption support, you can encrypt your data using [Rebuild](https://techdocs.akamai.com/linode-api/reference/post-rebuild-linode-instance).")
    image: StrictStr = Field(description="An Image ID to deploy the Linode Disk from.  Run the [List images](https://techdocs.akamai.com/linode-api/reference/get-images) operation with authentication to view all available Images. Official Linode Images start with `linode/`, while your Account's Images start with `private/`. Creating a disk from a Private Image requires `read_only` or `read_write` permissions for that Image. Run the [Update a user's grants](https://techdocs.akamai.com/linode-api/reference/put-user-grants) operation to adjust permissions for an Account Image.")
    metadata: Optional[PostLinodeInstanceRequestAllOfMetadata] = None
    root_pass: Annotated[str, Field(min_length=7, strict=True, max_length=128)] = Field(description="This sets the root user's password on a newly created Linode Disk when deploying from an Image.  - __Required__ when creating a Linode Disk from an Image, including when using a StackScript.  - Must meet a password strength score requirement that is calculated internally by the API. If the strength requirement is not met, you will receive a `Password does not meet strength requirement` error.")
    stackscript_data: Optional[Dict[str, Any]] = Field(default=None, description="This field is required only if the StackScript being deployed requires input data from the User for successful completion. See [User Defined Fields (UDFs)](https://www.linode.com/docs/products/tools/stackscripts/guides/write-a-custom-script/#declare-user-defined-fields-udfs) for more details.  This field is required to be valid JSON.  Total length cannot exceed 65,535 characters.")
    stackscript_id: Optional[StrictInt] = Field(default=None, description="A StackScript ID that will cause the referenced StackScript to be run during deployment of this Linode. A compatible `image` is required to use a StackScript. To get a list of available StackScript and their permitted Images, run [List StackScripts](https://techdocs.akamai.com/linode-api/reference/get-stack-scripts). This field cannot be used when deploying from a Backup or a Private Image.")
    type: Optional[StrictStr] = Field(default=None, description="The ID of the [Linode type](https://techdocs.akamai.com/linode-api/reference/get-linode-types) to resize to with this request.")
    __properties: ClassVar[List[str]] = ["authorized_keys", "authorized_users", "booted", "disk_encryption", "image", "metadata", "root_pass", "stackscript_data", "stackscript_id", "type"]

    @field_validator('disk_encryption')
    def disk_encryption_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['enabled', 'disabled']):
            raise ValueError("must be one of enum values ('enabled', 'disabled')")
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
        """Create an instance of PostRebuildLinodeInstanceRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of metadata
        if self.metadata:
            _dict['metadata'] = self.metadata.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostRebuildLinodeInstanceRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "authorized_keys": obj.get("authorized_keys"),
            "authorized_users": obj.get("authorized_users"),
            "booted": obj.get("booted") if obj.get("booted") is not None else True,
            "disk_encryption": obj.get("disk_encryption"),
            "image": obj.get("image"),
            "metadata": PostLinodeInstanceRequestAllOfMetadata.from_dict(obj["metadata"]) if obj.get("metadata") is not None else None,
            "root_pass": obj.get("root_pass"),
            "stackscript_data": obj.get("stackscript_data"),
            "stackscript_id": obj.get("stackscript_id"),
            "type": obj.get("type")
        })
        return _obj

