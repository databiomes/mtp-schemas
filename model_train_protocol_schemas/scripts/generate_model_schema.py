from pathlib import Path
from typing import Optional

from model_train_protocol_schemas.structures.model import Model
from model_train_protocol_schemas.utils import get_model_version, get_model_schema_url, _save_schema


def generate_model_schema(base_path: Optional[str | Path] = None) -> str:
    """
    Generates and saves the JSON Schema for the Model Manifest to
    schemas/v{major}/model_{version}.json.

    :param base_path: Base path for the schemas directory. If None, uses the repo root.
    :return: The path to the saved schema file.
    """
    schema = Model.model_json_schema(
        mode='serialization',
        by_alias=True
    )

    return _save_schema(
        schema=schema,
        version=get_model_version(),
        schema_url=get_model_schema_url(),
        title="Model Manifest Schema",
        description="JSON Schema for Model Manifest files",
        filename_pattern="model_{version}.json",
        base_path=base_path,
    )


if __name__ == "__main__":
    print("Generating model schema...")
    repo_root = Path(__file__).resolve().parents[1]
    model_path = generate_model_schema(base_path=repo_root)
    print(f"Model schema saved to: {model_path}")
