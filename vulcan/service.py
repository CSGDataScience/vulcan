"""Vulcan Service Specification
"""
from abc import ABCMeta, abstractmethod, abstractproperty


class VulcanService(metaclass=ABCMeta):
    """VulcanService
    Base class specification of a CSG Signal Provider.

    - init: Provide the (init)ial data necessary to render a clients view.
    - fetch_one: Provide a specific entity.
    - fetch_all: Provide all entities which match a given criteria
    """
    @abstractmethod
    def init(self, context):
        pass

    @abstractmethod
    def fetch_one(self, context):
        pass

    @abstractmethod
    def fetch_all(self, context):
        pass


class VulcanSQLService(VulcanService):
    """VulcanSQLService
    Base class specification of Vulcan SQL Service.
    """
    @property
    @abstractmethod
    def _conn_engine(self):
        pass

    @property
    @abstractmethod
    def _init_query(self):
        pass
