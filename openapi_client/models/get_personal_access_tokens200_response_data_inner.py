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
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class GetPersonalAccessTokens200ResponseDataInner(BaseModel):
    """
    A Personal Access Token is a token generated manually to access the API without going through an OAuth login.  Personal Access Tokens can have scopes just like OAuth tokens do, and are commonly used to give access to command-line tools like the Linode CLI, or when writing your own integrations.
    """ # noqa: E501
    created: Optional[datetime] = Field(default=None, description="The date and time this token was created.")
    expiry: Optional[datetime] = Field(default=None, description="When this token will expire.  Personal Access Tokens cannot be renewed, so after this time the token will be completely unusable and a new token will need to be generated.  Tokens may be created with `null` as their expiry and will never expire unless revoked.")
    id: Optional[StrictInt] = Field(default=None, description="This token's unique ID, which can be used to revoke it.")
    label: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="This token's label.  This is for display purposes only, but can be used to more easily track what you're using each token for.")
    scopes: Optional[StrictStr] = Field(default=None, description="The scopes this token was created with. These define what parts of the Account the token can be used to access. Many command-line tools, such as the [Linode CLI](https://github.com/linode/linode-cli), require tokens with access to `*`. Tokens with more restrictive scopes are generally more secure.")
    token: Optional[StrictStr] = Field(default=None, description="The token used to access the API.  When the token is created, the full token is returned here.  Otherwise, only the first 16 characters are returned.")
    __properties: ClassVar[List[str]] = ["created", "expiry", "id", "label", "scopes", "token"]

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
        """Create an instance of GetPersonalAccessTokens200ResponseDataInner from a JSON string"""
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
            "expiry",
            "id",
            "scopes",
            "token",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetPersonalAccessTokens200ResponseDataInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "created": obj.get("created"),
            "expiry": obj.get("expiry"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "scopes": obj.get("scopes"),
            "token": obj.get("token")
        })
        return _obj


