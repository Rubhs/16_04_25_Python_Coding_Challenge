#entity/Payment.py

class Payment:
    def __init__(self, paymentId=None, paymentDate=None, paymentAmount=None, client=None):
        self.__paymentId = paymentId
        self.__paymentDate = paymentDate
        self.__paymentAmount = paymentAmount
        self.__client = client  
        
    def get_paymentId(self): 
      return self.__paymentId
    
    def set_paymentId(self, paymentId): 
      self.__paymentId = paymentId

    def get_paymentDate(self): 
      return self.__paymentDate
    
    def set_paymentDate(self, paymentDate): 
      self.__paymentDate = paymentDate

    def get_paymentAmount(self): 
      return self.__paymentAmount
    
    def set_paymentAmount(self, paymentAmount): 
      self.__paymentAmount = paymentAmount

    def get_client(self): 
      return self.__client
    
    def set_client(self, client): 
      self.__client = client
      
    def __str__(self):
      return f"Payment [paymentId={self.__paymentId}, paymentDate={self.__paymentDate}, paymentAmount={self.__paymentAmount}, client={self.__client}]"