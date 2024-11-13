# This is direct configuration for the project
# Next step is converting to a pydantic config class

import os
from pathlib import Path
from typing import Optional
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings class for application settings and secrets management
    Official documentation on pydantic settings management:
    - https://pydantic-docs.helpmanual.io/usage/settings/
    """

    # Mandatory Config

    # Optional Config
    APP_NAME: str = "data_science_project_example"
    TEST_DB_NAME: Optional[str] = None
    TEST_DB_USER: Optional[str] = None
    TEST_DB_PASSWORD: Optional[str] = None
    TEST_DB_PORT: Optional[str] = None
    TEST_DB_HOST: Optional[str] = None
    TEST_DB_SERVICE: Optional[str] = None

    # Application Path
    APP_PATH: Path = Path(os.path.abspath("."))

    # Path for optional app configurations
    CONFIG_PATH: str = os.path.join(APP_PATH, "app", "config")
    STATIC_PATH: str = os.path.join(APP_PATH, "app", "static")
    DATA_PATH: str = os.path.join(APP_PATH, "data")

    # Logger, see logger module
    VERBOSITY: str = "DEBUG"
    LOG_PATH: Path = APP_PATH / "logs"

    # DVC
    DVC_PARAMS_YAML: Path = Path("params.yaml")
