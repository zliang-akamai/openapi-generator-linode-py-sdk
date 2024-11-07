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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class OauthClient(BaseModel):
    """
    A third-party application registered to Linode that users may log into with their Linode account through our authentication server at [login.linode.com](https://login.linode.com).  Using an OAuth Client, a third-party developer may be given access to some, or all, of a User's account for the purposes of their application.
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="The OAuth Client ID.  This is used to identify the client, and is a publicly known value (it is not a secret).")
    label: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=512)]] = Field(default=None, description="The name of this application.  This will be presented to users when they are asked to grant it access to their Account.")
    public: Optional[StrictBool] = Field(default=False, description="If this is a public or private OAuth Client.  Public clients have a slightly different authentication workflow than private clients.  See the [OAuth spec](https://oauth.net/2/) for more details.")
    redirect_uri: Optional[StrictStr] = Field(default=None, description="The location a successful log in from [login.linode.com](https://login.linode.com) should be redirected to for this client.  The receiver of this redirect should be ready to accept an OAuth exchange code and finish the OAuth exchange.")
    secret: Optional[StrictStr] = Field(default=None, description="The OAuth Client secret, used in the OAuth exchange.  This is returned as `<REDACTED>` except when an OAuth Client is created or its secret is reset.  This is a secret, and should not be shared or disclosed publicly.")
    status: Optional[StrictStr] = Field(default=None, description="The status of this application.  `active` by default.")
    thumbnail_url: Optional[StrictStr] = Field(default=None, description="The URL where this client's thumbnail may be viewed, or `null` if this client does not have a thumbnail set.")
    __properties: ClassVar[List[str]] = ["id", "label", "public", "redirect_uri", "secret", "status", "thumbnail_url"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['active', 'disabled', 'suspended']):
            raise ValueError("must be one of enum values ('active', 'disabled', 'suspended')")
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
        """Create an instance of OauthClient from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "id",
            "secret",
            "status",
            "thumbnail_url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if thumbnail_url (nullable) is None
        # and model_fields_set contains the field
        if self.thumbnail_url is None and "thumbnail_url" in self.model_fields_set:
            _dict['thumbnail_url'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OauthClient from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "label": obj.get("label"),
            "public": obj.get("public") if obj.get("public") is not None else False,
            "redirect_uri": obj.get("redirect_uri"),
            "secret": obj.get("secret"),
            "status": obj.get("status"),
            "thumbnail_url": obj.get("thumbnail_url")
        })
        return _obj

