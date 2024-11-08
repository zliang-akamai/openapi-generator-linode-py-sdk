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
from openapi_client.models.get_node_balancer_configs200_response_data_inner_nodes_status import GetNodeBalancerConfigs200ResponseDataInnerNodesStatus
from openapi_client.models.post_rebuild_node_balancer_config_request_all_of_nodes_inner import PostRebuildNodeBalancerConfigRequestAllOfNodesInner
from typing import Optional, Set
from typing_extensions import Self

class PostRebuildNodeBalancerConfigRequest(BaseModel):
    """
    PostRebuildNodeBalancerConfigRequest
    """ # noqa: E501
    algorithm: Optional[StrictStr] = Field(default='roundrobin', description="What algorithm this NodeBalancer should use for routing traffic to backends.")
    check: Optional[StrictStr] = Field(default='none', description="The type of check to perform against backends to ensure they are serving requests. This is used to determine if backends are up or down.  - If `none` no check is performed. - `connection` requires only a connection to the backend to succeed. - `http` and `http_body` rely on the backend serving HTTP, and that the response returned matches what is expected.")
    check_attempts: Optional[Annotated[int, Field(le=30, strict=True, ge=1)]] = Field(default=3, description="How many times to attempt a check before considering a backend to be down.")
    check_body: Optional[StrictStr] = Field(default=None, description="This value must be present in the response body of the check in order for it to pass. If this value is not present in the response body of a check request, the backend is considered to be down.")
    check_interval: Optional[StrictInt] = Field(default=31, description="How often, in seconds, to check that backends are up and serving requests.  Must be greater than `check_timeout`.")
    check_passive: Optional[StrictBool] = Field(default=True, description="If true, any response from this backend with a `5xx` status code will be enough for it to be considered unhealthy and taken out of rotation.")
    check_path: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The URL path to check on each backend. If the backend does not respond to this request it is considered to be down.")
    check_timeout: Optional[Annotated[int, Field(le=30, strict=True, ge=1)]] = Field(default=30, description="How long, in seconds, to wait for a check attempt before considering it failed.  Must be less than `check_interval`.")
    cipher_suite: Optional[StrictStr] = Field(default='recommended', description="What ciphers to use for SSL connections served by this NodeBalancer.  - `legacy` is considered insecure and should only be used if necessary.")
    id: Optional[StrictInt] = Field(default=None, description="This config's unique ID.")
    nodebalancer_id: Optional[StrictInt] = Field(default=None, description="The ID for the NodeBalancer this config belongs to.")
    nodes_status: Optional[GetNodeBalancerConfigs200ResponseDataInnerNodesStatus] = None
    port: Optional[Annotated[int, Field(le=65535, strict=True, ge=1)]] = Field(default=80, description="The port this Config is for. These values must be unique across configs on a single NodeBalancer (you can't have two configs for port 80, for example).  While some ports imply some protocols, no enforcement is done and you may configure your NodeBalancer however is useful to you. For example, while port 443 is generally used for HTTPS, you do not need SSL configured to have a NodeBalancer listening on port 443.")
    protocol: Optional[StrictStr] = Field(default='http', description="The protocol this port is configured to serve.  - The `http` and `tcp` protocols do not support `ssl_cert` and `ssl_key`.  - The `https` protocol is mutually required with `ssl_cert` and `ssl_key`.  Review our guide on [Available Protocols](https://www.linode.com/docs/products/networking/nodebalancers/guides/protocols/) for information on protocol features.")
    proxy_protocol: Optional[StrictStr] = Field(default='none', description="ProxyProtocol is a TCP extension that sends initial TCP connection information such as source/destination IPs and ports to backend devices. This information would be lost otherwise. Backend devices must be configured to work with ProxyProtocol if enabled.  - If omitted, or set to `none`, the NodeBalancer doesn't send any auxiliary data over TCP connections. This is the default. - If set to `v1`, the human-readable header format (Version 1) is used. Requires `tcp` protocol. - If set to `v2`, the binary header format (Version 2) is used. Requires `tcp` protocol.")
    ssl_cert: Optional[StrictStr] = Field(default=None, description=" The PEM-formatted public SSL certificate (or the combined PEM-formatted SSL certificate and Certificate Authority chain) that should be served on this NodeBalancerConfig's port.  Line breaks must be represented as `\\n` in the string for requests (but not when using the Linode CLI).  [Diffie-Hellman Parameters](https://www.linode.com/docs/products/networking/nodebalancers/guides/ssl-termination/#diffie-hellman-parameters) can be included in this value to enable forward secrecy.  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, `<REDACTED>` will be printed where the field appears.  The read-only `ssl_commonname` and `ssl_fingerprint` fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig.")
    ssl_commonname: Optional[StrictStr] = Field(default=None, description="The read-only common name automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig.")
    ssl_fingerprint: Optional[StrictStr] = Field(default=None, description="The read-only SHA1-encoded fingerprint automatically derived from the SSL certificate assigned to this NodeBalancerConfig. Please refer to this field to verify that the appropriate certificate is assigned to your NodeBalancerConfig.")
    ssl_key: Optional[StrictStr] = Field(default=None, description="The PEM-formatted private key for the SSL certificate set in the `ssl_cert` field.  Line breaks must be represented as `\\n` in the string for requests (but not when using the Linode CLI).  The contents of this field will not be shown in any responses that display the NodeBalancerConfig. Instead, `<REDACTED>` will be printed where the field appears.  The read-only `ssl_commonname` and `ssl_fingerprint` fields in a NodeBalancerConfig response are automatically derived from your certificate. Please refer to these fields to verify that the appropriate certificate was assigned to your NodeBalancerConfig.")
    stickiness: Optional[StrictStr] = Field(default='none', description="Controls how session stickiness is handled on this port.  - If set to `none` connections will always be assigned a backend based on the algorithm configured. - If set to `table` sessions from the same remote address will be routed to the same backend. - For HTTP or HTTPS clients, `http_cookie` allows sessions to be routed to the same backend based on a cookie set by the NodeBalancer.")
    nodes: List[PostRebuildNodeBalancerConfigRequestAllOfNodesInner] = Field(description="The NodeBalancer Nodes that serve this Config.  Some considerations for Nodes when rebuilding a config:    - Current Nodes excluded from the request body will be deleted from the Config.   - Current Nodes (identified by their Node ID) will be updated.   - New Nodes (included without a Node ID) will be created.")
    __properties: ClassVar[List[str]] = ["algorithm", "check", "check_attempts", "check_body", "check_interval", "check_passive", "check_path", "check_timeout", "cipher_suite", "id", "nodebalancer_id", "nodes_status", "port", "protocol", "proxy_protocol", "ssl_cert", "ssl_commonname", "ssl_fingerprint", "ssl_key", "stickiness", "nodes"]

    @field_validator('algorithm')
    def algorithm_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['roundrobin', 'leastconn', 'source']):
            raise ValueError("must be one of enum values ('roundrobin', 'leastconn', 'source')")
        return value

    @field_validator('check')
    def check_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'connection', 'http', 'http_body']):
            raise ValueError("must be one of enum values ('none', 'connection', 'http', 'http_body')")
        return value

    @field_validator('check_path')
    def check_path_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^[a-zA-Z0-9\/\-%?&=.]*$", value):
            raise ValueError(r"must validate the regular expression /^[a-zA-Z0-9\/\-%?&=.]*$/")
        return value

    @field_validator('cipher_suite')
    def cipher_suite_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['recommended', 'legacy']):
            raise ValueError("must be one of enum values ('recommended', 'legacy')")
        return value

    @field_validator('protocol')
    def protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['http', 'https', 'tcp']):
            raise ValueError("must be one of enum values ('http', 'https', 'tcp')")
        return value

    @field_validator('proxy_protocol')
    def proxy_protocol_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'v1', 'v2']):
            raise ValueError("must be one of enum values ('none', 'v1', 'v2')")
        return value

    @field_validator('stickiness')
    def stickiness_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['none', 'table', 'http_cookie']):
            raise ValueError("must be one of enum values ('none', 'table', 'http_cookie')")
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
        """Create an instance of PostRebuildNodeBalancerConfigRequest from a JSON string"""
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
            "nodebalancer_id",
            "ssl_commonname",
            "ssl_fingerprint",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of nodes_status
        if self.nodes_status:
            _dict['nodes_status'] = self.nodes_status.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in nodes (list)
        _items = []
        if self.nodes:
            for _item_nodes in self.nodes:
                if _item_nodes:
                    _items.append(_item_nodes.to_dict())
            _dict['nodes'] = _items
        # set to None if ssl_cert (nullable) is None
        # and model_fields_set contains the field
        if self.ssl_cert is None and "ssl_cert" in self.model_fields_set:
            _dict['ssl_cert'] = None

        # set to None if ssl_key (nullable) is None
        # and model_fields_set contains the field
        if self.ssl_key is None and "ssl_key" in self.model_fields_set:
            _dict['ssl_key'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PostRebuildNodeBalancerConfigRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "algorithm": obj.get("algorithm") if obj.get("algorithm") is not None else 'roundrobin',
            "check": obj.get("check") if obj.get("check") is not None else 'none',
            "check_attempts": obj.get("check_attempts") if obj.get("check_attempts") is not None else 3,
            "check_body": obj.get("check_body"),
            "check_interval": obj.get("check_interval") if obj.get("check_interval") is not None else 31,
            "check_passive": obj.get("check_passive") if obj.get("check_passive") is not None else True,
            "check_path": obj.get("check_path"),
            "check_timeout": obj.get("check_timeout") if obj.get("check_timeout") is not None else 30,
            "cipher_suite": obj.get("cipher_suite") if obj.get("cipher_suite") is not None else 'recommended',
            "id": obj.get("id"),
            "nodebalancer_id": obj.get("nodebalancer_id"),
            "nodes_status": GetNodeBalancerConfigs200ResponseDataInnerNodesStatus.from_dict(obj["nodes_status"]) if obj.get("nodes_status") is not None else None,
            "port": obj.get("port") if obj.get("port") is not None else 80,
            "protocol": obj.get("protocol") if obj.get("protocol") is not None else 'http',
            "proxy_protocol": obj.get("proxy_protocol") if obj.get("proxy_protocol") is not None else 'none',
            "ssl_cert": obj.get("ssl_cert"),
            "ssl_commonname": obj.get("ssl_commonname"),
            "ssl_fingerprint": obj.get("ssl_fingerprint"),
            "ssl_key": obj.get("ssl_key"),
            "stickiness": obj.get("stickiness") if obj.get("stickiness") is not None else 'none',
            "nodes": [PostRebuildNodeBalancerConfigRequestAllOfNodesInner.from_dict(_item) for _item in obj["nodes"]] if obj.get("nodes") is not None else None
        })
        return _obj


