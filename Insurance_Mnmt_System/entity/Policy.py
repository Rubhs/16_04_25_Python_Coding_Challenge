#entity/Policy.py

class Policy:
  
  def __init__(self,policyId=None, policyName=None, premiumAmount=None):
    self.__policyId = policyId
    self.__policyName = policyName
    self.__premiumAmount = premiumAmount
    
  def get_policyId(self):
    return self.__policyId
  
  def set_policyId(self,policyId):
    self.__policyId=policyId
    
  def get_policyName(self):
    return self.__policyName
  
  def set_policyName(self,policyName):
    self.__policyName=policyName
    
  def get_premiumAmount(self):
    return self.__premiumAmount
  
  def set_premiumAmount(self,premiumAmount):
    self.__premiumAmount=premiumAmount
    
  def __str__(self):
    return f"Policy [policyId={self.__policyId}, policyName={self.__policyName}, premiumAmount={self.__premiumAmount}]"