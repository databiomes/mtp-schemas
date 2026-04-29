from pathlib import Path
from typing import Optional

from model_train_protocol_schemas.structures.protocol import Protocol
from model_train_protocol_schemas.utils import get_bloom_version, get_bloom_schema_url, _save_schema


def generate_protocol_schema(base_path: Optional[str | Path] = None) -> str:
    """
    Generates and saves the JSON Schema for the Model Train Protocol to
    schemas/v{major}/bloom_{version}.json.

    This schema can be used by other languages (Go, JavaScript, etc.) to validate
    and understand the structure of the protocol JSON files.

    :param base_path: Base path for the schemas directory. If None, uses the repo root.
    :return: The path to the saved schema file.
    """
    schema = Protocol.model_json_schema(
        mode='serialization',
        by_alias=True
    )

    return _save_schema(
        schema=schema,
        version=get_bloom_version(),
        schema_url=get_bloom_schema_url(),
        title="Model Train Protocol Schema",
        description="JSON Schema for Model Train Protocol (MTP) model files",
        filename_pattern="bloom_{version}.json",
        base_path=base_path,
    )


if __name__ == "__main__":
    print("Generating protocol schema...")
    repo_root = Path(__file__).resolve().parents[1]
    protocol_path = generate_protocol_schema(base_path=repo_root)
    print(f"Protocol schema saved to: {protocol_path}")
