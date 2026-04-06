"""
This script updates the JSON schema files used for validating model training configurations.
"""
from typing import Optional

from model_train_protocol_schemas.structures.template import Template
from model_train_protocol_schemas.utils import get_template_version, get_template_schema_url, _save_schema


def generate_template_schema(base_path: Optional[str] = None) -> str:
    """
    Generates and saves the JSON Schema for the Model Train Protocol Template to
    schemas/v{major}/template_{version}.json.

    This schema can be used by other languages (Go, JavaScript, etc.) to validate
    and understand the structure of the template JSON files.

    :param base_path: Base path for the schemas directory. If None, uses the repo root.
    :return: The path to the saved schema file.
    """
    schema = Template.model_json_schema(
        mode='serialization',
        by_alias=True
    )

    return _save_schema(
        schema=schema,
        version=get_template_version(),
        schema_url=get_template_schema_url(),
        title="Model Train Protocol Template Schema",
        description="JSON Schema for Model Train Protocol (MTP) template files",
        filename_pattern="template_{version}.json",
        base_path=base_path,
    )


if __name__ == "__main__":
    print("Generating template schema...")
    template_path = generate_template_schema()
    print(f"Template schema saved to: {template_path}")
