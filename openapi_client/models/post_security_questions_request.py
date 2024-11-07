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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.post_security_questions_request_security_questions_inner import PostSecurityQuestionsRequestSecurityQuestionsInner
from typing import Optional, Set
from typing_extensions import Self

class PostSecurityQuestionsRequest(BaseModel):
    """
    Security questions and responses object for POST operation.
    """ # noqa: E501
    security_questions: Optional[List[PostSecurityQuestionsRequestSecurityQuestionsInner]] = Field(default=None, description="Security questions and response objects.")
    __properties: ClassVar[List[str]] = ["security_questions"]

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
        """Create an instance of PostSecurityQuestionsRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in security_questions (list)
        _items = []
        if self.security_questions:
            for _item_security_questions in self.security_questions:
                if _item_security_questions:
                    _items.append(_item_security_questions.to_dict())
            _dict['security_questions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostSecurityQuestionsRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "security_questions": [PostSecurityQuestionsRequestSecurityQuestionsInner.from_dict(_item) for _item in obj["security_questions"]] if obj.get("security_questions") is not None else None
        })
        return _obj


