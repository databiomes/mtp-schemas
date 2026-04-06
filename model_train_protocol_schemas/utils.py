import json
from pathlib import Path
from typing import Optional

from schema_version import SCHEMA_VERSION
from template_version import TEMPLATE_VERSION


def get_schema_version() -> str:
    """
    Gets the schema version bundled with the package.
    """
    return SCHEMA_VERSION


def get_template_version() -> str:
    """
    Gets the template version bundled with the package.
    """
    return TEMPLATE_VERSION


def get_bloom_schema_url():
    """
    Retrieves the schema URL for the current version of the Model Train Protocol.
    """
    version_semantic: str = get_schema_version()
    schema_url = f"https://mtp.schemas.databiomes.com/v{version_semantic[0]}/bloom_{version_semantic.replace('.', '_')}.json"
    return schema_url


def get_template_schema_url():
    """
    Retrieves the schema URL for the current version of the MTP Template.
    """
    version_semantic: str = get_template_version()
    schema_url = f"https://mtp.schemas.databiomes.com/v{version_semantic[0]}/template_{version_semantic.replace('.', '_')}.json"
    return schema_url


def _get_base_path(base_path: Optional[str]) -> Path:
    if base_path is None:
        return Path(__file__).resolve().parents[1]
    return Path(base_path)


def _save_schema(
        schema: dict,
        version: str,
        schema_url: str,
        title: str,
        description: str,
        filename_pattern: str,
        base_path: Optional[str] = None,
) -> str:
    version_underscored: str = version.replace('.', '_')
    schema_dir = _get_base_path(base_path) / "schemas" / f"v{version[0]}"
    schema_dir.mkdir(parents=True, exist_ok=True)

    schema_path = schema_dir / filename_pattern.format(version=version_underscored)

    final_schema = {
        "$schema": "https://json-schema.org/draft/2020-12/schema",
        "$id": schema_url,
        "title": title,
        "description": description,
        **schema,
    }
    with open(schema_path, 'w', encoding='utf-8') as f:
        json.dump(final_schema, f, indent=2, ensure_ascii=False)

    return str(schema_path)
