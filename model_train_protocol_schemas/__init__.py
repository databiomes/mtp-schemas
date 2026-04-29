"""
Model Train Protocol Schemas (mtp-schemas)

This package contains the JSON Schemas and corresponding Pydantic models for the
Model Train Protocol (MTP), including Protocol (Bloom), Template, and Model definitions.
"""

from model_train_protocol_schemas.structures.protocol import Protocol
from model_train_protocol_schemas.structures.template import Template
from model_train_protocol_schemas.structures.model import Model

from model_train_protocol_schemas.utils import (
    get_bloom_version,
    get_template_version,
    get_model_version,
    get_bloom_schema_url,
    get_template_schema_url,
    get_model_schema_url,
    get_example_bloom_file,
    get_example_template_file,
    get_example_model_file,
    parse_bloom_version,
    parse_template_version,
    parse_model_version,
)

__all__ = [
    # Data Structures
    "Protocol",
    "Template",
    "Model",
    
    # Versioning
    "get_bloom_version",
    "get_template_version",
    "get_model_version",
    
    # Schema URLs
    "get_bloom_schema_url",
    "get_template_schema_url",
    "get_model_schema_url",
    
    # Utilities
    "get_example_bloom_file",
    "get_example_template_file",
    "get_example_model_file",
    "parse_bloom_version",
    "parse_template_version",
    "parse_model_version",
]
