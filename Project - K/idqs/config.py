"""Application configuration loaded from environment variables."""

from dataclasses import dataclass, field
import os


@dataclass(frozen=True)
class Settings:
    """Runtime settings resolved when the application starts.

    Default factories ensure values loaded by ``load_dotenv()`` are observed,
    rather than reading the environment when this module is merely imported.
    """

    embedding_model: str = field(
        default_factory=lambda: os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-mpnet-base-v2")
    )
    llm_repository: str = field(default_factory=lambda: os.getenv("LLM_REPOSITORY", "google/flan-t5-large"))
    chunk_size: int = field(default_factory=lambda: int(os.getenv("CHUNK_SIZE", "1000")))
    chunk_overlap: int = field(default_factory=lambda: int(os.getenv("CHUNK_OVERLAP", "200")))
    retriever_k: int = field(default_factory=lambda: int(os.getenv("RETRIEVER_K", "4")))
    huggingface_token: str | None = field(default_factory=lambda: os.getenv("HUGGINGFACEHUB_API_TOKEN"))
