#dao/IPolicyService.py

from abc import ABC, abstractmethod
from typing import List
from entity.Policy import Policy

class IPolicyService(ABC):

    @abstractmethod
    def createPolicy(self, policy: Policy) -> bool:
        pass

    @abstractmethod
    def getPolicy(self, policyId) -> Policy:
        pass

    @abstractmethod
    def getAllPolicies(self) -> List[Policy]:
        pass

    @abstractmethod
    def updatePolicy(self, policy: Policy) -> bool:
        pass

    @abstractmethod
    def deletePolicy(self, policyId) -> bool:
        pass
