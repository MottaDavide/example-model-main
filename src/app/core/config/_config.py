# Config object is a global supervisor of the application. It provides any sort
# of configuration and logging.

import logging
import os
from typing import Optional
from pydantic import ValidationError
from ._dvc_params import Params
from app.tool import InternalLogger
from ._settings import Settings

class Config:
    def __init__(self) -> None:
        """Lazy variable 'setting' is set to None"""
        self._settings: Optional[Settings] = None

    @property
    def settings(self) -> Settings:
        """Lazy variable 'settings'."""
        if self._settings is None:
            self._settings = self._settings_from_env()
        return self._settings

    @property
    def params(self) -> Params:
        """Lazy variable 'params'."""
        dvc_params_yaml = self.settings.DVC_PARAMS_YAML
        return Params(dvc_params_yaml)

    @property
    def logger(self) -> logging.Logger:
        """System logger object."""
        logger = InternalLogger(
            self.settings.VERBOSITY, self.settings.LOG_PATH
        ).get_logger()
        return logger

    def set_settings(self, settings: Optional[Settings]) -> None:
        """It sets the setting property with an external one (Settings injection)."""
        self._settings = settings

    def _settings_from_env(
        self, env_file: str = os.environ.get("ENV_FILE", default=".env")
    ) -> Settings:
        """It creates the settings object. env_file is used only if exists."""
        try:
            return Settings(_env_file=env_file, _env_file_encoding="utf-8")  # type: ignore
        except ValidationError as error:
            self.logger.fatal(
                f"Missing Variable in environment (or .env file): {error}"
            )
            raise error


config = Config()
