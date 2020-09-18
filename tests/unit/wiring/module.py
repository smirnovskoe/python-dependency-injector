"""Test module for wiring."""

from typing import Callable

from dependency_injector.wiring import Provide, Provider

from .container import Container
from .service import Service


class TestClass:

    def __init__(self, service: Service = Provide[Container.service]):
        self.service = service


def test_function(service: Service = Provide[Container.service]):
    return service


def test_function_provider(service_provider: Callable[..., Service] = Provider[Container.service]):
    service = service_provider()
    return service


def test_config_value(
        some_value_int: int = Provide[Container.config.a.b.c],
        some_value_str: str = Provide[Container.config.a.b.c],
):
    return some_value_int, some_value_str