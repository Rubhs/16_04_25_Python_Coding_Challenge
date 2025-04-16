#dao/InsuranceServiceImpl.py

import pyodbc
from dao.IPolicyService import IPolicyService
from entity.Policy import Policy
from utility.DBConnection import DBConnection
from myexceptions.PolicyNotFoundException import PolicyNotFoundException

class InsuranceServiceImpl(IPolicyService):

    def createPolicy(self, policy: Policy) -> bool:
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            query = "INSERT INTO Policy (policyName, premiumAmount) VALUES (?, ?)"
            cursor.execute(query, (policy.get_policyName(), policy.get_premiumAmount()))
            conn.commit()
            return True
        except Exception as e:
            print("Error creating policy:", e)
            return False

    def getPolicy(self, policyId) -> Policy:
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            query = "SELECT * FROM Policy WHERE policyId = ?"
            cursor.execute(query, (policyId,))
            row = cursor.fetchone()
            if row:
                return Policy(row[0], row[1], row[2])
            else:
                raise PolicyNotFoundException(f"Policy with ID {policyId} not found.")
        except Exception as e:
            print("Error retrieving policy:", e)
            return None

    def getAllPolicies(self):
        policies = []
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            query = "SELECT * FROM Policy"
            cursor.execute(query)
            rows = cursor.fetchall()
            for row in rows:
                policies.append(Policy(row[0], row[1], row[2]))
        except Exception as e:
            print("Error fetching all policies:", e)
        return policies

    def updatePolicy(self, policy):
        
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            query = "UPDATE Policy SET policyName = ?, premiumAmount = ? WHERE policyId = ?"
            cursor.execute(query, (policy.get_policyName(), policy.get_premiumAmount(), policy.get_policyId()))
            
            if cursor.rowcount == 0:
                raise PolicyNotFoundException(f"Policy with ID {policy.get_policyId()} not found.")
            
            conn.commit()
            return True
        except PolicyNotFoundException as pne:
            print(f"Error: {pne}")
            return False
        except Exception as e:
            print("Error updating policy:", e)
            return False

    def deletePolicy(self, policyId) -> bool:
        try:
            conn = DBConnection.getConnection()
            cursor = conn.cursor()
            query = "DELETE FROM Policy WHERE policyId = ?"
            cursor.execute(query, (policyId,))
            conn.commit()
            if cursor.rowcount == 0:
                raise PolicyNotFoundException(f"Policy with ID {policyId} does not exist.")
            return True
        except Exception as e:
            print("Error deleting policy:", e)
            return False