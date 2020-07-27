

from typing import Callable

from tensortrade.oms.exchanges.exchange import Exchange, ExchangeOptions
from tensortrade.oms.exchanges import services


_registry = {
    'simulated': None,
}


def get_service(identifier: str) -> Callable:
    """Gets the `ExecutionService` that matches with the identifier.

    Arguments:
        identifier: The identifier for the `ExecutionService`

    Raises:
        KeyError: if identifier is not associated with any `ExecutionService`
    """
    if identifier not in _registry.keys():
        raise KeyError(f'Identifier {identifier} is not associated with any `ExecutionService`.')

    return _registry[identifier]
