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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.get_lke_clusters200_response_data_inner_control_plane import GetLkeClusters200ResponseDataInnerControlPlane
from openapi_client.models.post_lke_cluster_request_node_pools_inner import PostLkeClusterRequestNodePoolsInner
from typing import Optional, Set
from typing_extensions import Self

class PostLkeClusterRequest(BaseModel):
    """
    PostLkeClusterRequest
    """ # noqa: E501
    control_plane: Optional[GetLkeClusters200ResponseDataInnerControlPlane] = None
    k8s_version: StrictStr = Field(description="The desired Kubernetes version for this Kubernetes cluster in the format of &lt;major&gt;.&lt;minor&gt;, and the latest supported patch version will be deployed.")
    label: Annotated[str, Field(min_length=1, strict=True, max_length=32)] = Field(description="This Kubernetes cluster's unique label for display purposes only. Labels have the following constraints:    - UTF-8 characters will be returned by the API using escape sequences of their Unicode code points. For example, the Japanese character _か_ is 3 bytes in UTF-8 (`0xE382AB`). Its Unicode code point is 2 bytes (`0x30AB`). APIv4 supports this character and the API will return it as the escape sequence using six 1 byte characters which represent 2 bytes of Unicode code point (`\"\\u30ab\"`).    - 4 byte UTF-8 characters are not supported.    - If the label is entirely composed of UTF-8 characters, the API response will return the code points using up to 193 1 byte characters.")
    node_pools: List[PostLkeClusterRequestNodePoolsInner]
    region: StrictStr = Field(description="This Kubernetes cluster's location.")
    tags: Optional[List[StrictStr]] = Field(default=None, description="An array of tags applied to the Kubernetes cluster. Tags are for organizational purposes only.")
    __properties: ClassVar[List[str]] = ["control_plane", "k8s_version", "label", "node_pools", "region", "tags"]

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
        """Create an instance of PostLkeClusterRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of control_plane
        if self.control_plane:
            _dict['control_plane'] = self.control_plane.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in node_pools (list)
        _items = []
        if self.node_pools:
            for _item_node_pools in self.node_pools:
                if _item_node_pools:
                    _items.append(_item_node_pools.to_dict())
            _dict['node_pools'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostLkeClusterRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "control_plane": GetLkeClusters200ResponseDataInnerControlPlane.from_dict(obj["control_plane"]) if obj.get("control_plane") is not None else None,
            "k8s_version": obj.get("k8s_version"),
            "label": obj.get("label"),
            "node_pools": [PostLkeClusterRequestNodePoolsInner.from_dict(_item) for _item in obj["node_pools"]] if obj.get("node_pools") is not None else None,
            "region": obj.get("region"),
            "tags": obj.get("tags")
        })
        return _obj


