from typing import Type

from mypy.plugin import Plugin

from .plugin import FlaskSQLAlchemyPlugin


__version__ = "0.0.1"


def plugin(version: str) -> Type[Plugin]:
    return FlaskSQLAlchemyPlugin
