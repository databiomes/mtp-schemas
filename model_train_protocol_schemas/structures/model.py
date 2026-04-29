"""
Pydantic models for Model Manifest JSON structure.
"""

from datetime import datetime
from typing import List, Dict, Optional

from pydantic import BaseModel, Field, ConfigDict


class ModelFile(BaseModel):
    """Represents a file associated with the model."""
    path: str = Field(..., description="Path relative to the model's root directory.")
    checksum: str = Field(..., description="Checksum to verify integrity (e.g., sha256:...).")


class TrainingInfo(BaseModel):
    """Reference to training related artifacts."""
    reference: str = Field(..., description="Reference to training artifacts (e.g., Bloom ID).")


class Model(BaseModel):
    """Manifest representing a trained model, its identifying information, and associated artifacts."""
    id: str = Field(..., description="Globally unique identifier for the model.")
    name: str = Field(..., description="The name of the model.")
    description: Optional[str] = Field(None, description="Detailed description of the model, its purpose, and capabilities.")
    created_time: datetime = Field(..., description="The date and time when the model was created (ISO 8601 format).")
    files: List[ModelFile] = Field(..., min_length=1, description="List of files associated with the model, including paths and checksums for integrity verification.")
    training: Optional[TrainingInfo] = Field(None, description="References to training-related artifacts, such as the training dataset or process.")
    labels: Optional[Dict[str, str]] = Field(None, description="User-defined key-value pairs for organizing and categorizing the model.")

    model_config = ConfigDict(
        populate_by_name=True,
    )
