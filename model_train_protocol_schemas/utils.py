import json
from pathlib import Path
from typing import Optional

from packaging.version import Version

from model_train_protocol_schemas.bloom_version import BLOOM_VERSION
from model_train_protocol_schemas.template_version import TEMPLATE_VERSION
from model_train_protocol_schemas.model_version import MODEL_VERSION


def get_bloom_version() -> str:
    """
    Gets the bloom version bundled with the package.
    """
    return BLOOM_VERSION


def get_template_version() -> str:
    """
    Gets the template version bundled with the package.
    """
    return TEMPLATE_VERSION


def get_model_version() -> str:
    """
    Gets the model version bundled with the package.
    """
    return MODEL_VERSION


def parse_bloom_version(d: dict) -> Version:
    """Parse the version from a Bloom file."""
    if "$id" not in d:
        raise ValueError("Bloom file is missing '$id' field.")
    schema_url: str = d["$id"]
    version_str: str = ".".join(schema_url.split("/")[-1].split(".")[0].split("_")[:-3])  # like 1.2.0
    return Version(version_str)


def parse_template_version(d: dict) -> Version:
    """Parse the version from a Bloom file."""
    if "$id" not in d:
        raise ValueError("Template file is missing '$id' field.")
    schema_url: str = d["$id"]
    version_str: str = ".".join(schema_url.split("/")[-1].split(".")[0].split("_")[:-3])  # like 1.2.0
    return Version(version_str)

def parse_model_version(d: dict) -> Version:
    """Parse the version from a Bloom file."""
    if "$id" not in d:
        raise ValueError("Model file is missing '$id' field.")
    schema_url: str = d["$id"]
    version_str: str = ".".join(schema_url.split("/")[-1].split(".")[0].split("_")[:-3])  # like 1.2.0
    return Version(version_str)

def get_example_bloom_file(version: Version) -> dict:
    """
    Retrieves an example Bloom file for the specified version.
    """
    major: str = str(version.major)
    minor: str = str(version.minor)
    patch: str = str(version.micro)
    example_path = Path(__file__).resolve().parent / "examples" / f"bloom_{major}_{minor}_{patch}.json"
    if not example_path.exists():
        raise FileNotFoundError(f"Example Bloom file not found for version {version} at path: {example_path}")
    with open(example_path, 'r', encoding='utf-8') as f:
        bloom_file = json.load(f)
    return bloom_file


def get_example_template_file(version: Version) -> dict:
    """
    Retrieves an example Template file for the specified version.
    """
    major: str = str(version.major)
    minor: str = str(version.minor)
    patch: str = str(version.micro)
    example_path = Path(__file__).resolve().parent / "examples" / f"template_{major}_{minor}_{patch}.json"
    if not example_path.exists():
        raise FileNotFoundError(f"Example Template file not found for version {version} at path: {example_path}")
    with open(example_path, 'r', encoding='utf-8') as f:
        template_file = json.load(f)
    return template_file


def get_example_model_file(version: Version) -> dict:
    """
    Retrieves an example Model file for the specified version.
    """
    major: str = str(version.major)
    minor: str = str(version.minor)
    patch: str = str(version.micro)
    example_path = Path(__file__).resolve().parent / "examples" / f"model_{major}_{minor}_{patch}.json"
    if not example_path.exists():
        raise FileNotFoundError(f"Example Model file not found for version {version} at path: {example_path}")
    with open(example_path, 'r', encoding='utf-8') as f:
        model_file = json.load(f)
    return model_file


def get_bloom_schema_url():
    """
    Retrieves the schema URL for the current version of the Model Train Protocol.
    """
    version_semantic: str = get_bloom_version()
    schema_url = f"https://mtp.schemas.databiomes.com/v{version_semantic[0]}/bloom_{version_semantic.replace('.', '_')}.json"
    return schema_url


def get_template_schema_url():
    """
    Retrieves the schema URL for the current version of the MTP Template.
    """
    version_semantic: str = get_template_version()
    schema_url = f"https://mtp.schemas.databiomes.com/v{version_semantic[0]}/template_{version_semantic.replace('.', '_')}.json"
    return schema_url


def get_model_schema_url():
    """
    Retrieves the schema URL for the current version of the MTP Model.
    """
    version_semantic: str = get_model_version()
    schema_url = f"https://mtp.schemas.databiomes.com/v{version_semantic[0]}/model_{version_semantic.replace('.', '_')}.json"
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
