#main/MainModule.py

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dao.InsuranceServiceImpl import InsuranceServiceImpl
from entity.Policy import Policy
from myexceptions.PolicyNotFoundException import PolicyNotFoundException

def main():
    service = InsuranceServiceImpl()

    while True:
        print("\n===== INSURANCE POLICY MANAGEMENT SYSTEM =====")
        print("1. Create Policy")
        print("2. Get Policy by ID")
        print("3. Get All Policies")
        print("4. Update Policy")
        print("5. Delete Policy")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            if choice == '1':
                name = input("Enter Policy Name: ")
                premium = float(input("Enter Premium Amount: "))
                policy = Policy(policyName=name, premiumAmount=premium)
                if service.createPolicy(policy):
                    print(" Policy created successfully.")
                else:
                    print("xxx Failed to create policy xxx")

            elif choice == '2':
                pid = int(input("Enter Policy ID: "))
                policy = service.getPolicy(pid)
                print("Policy Details:", policy)

            elif choice == '3':
                policies = service.getAllPolicies()
                print("All Policies:")
                for p in policies:
                    print(p)

            elif choice == '4':
                pid = int(input("Enter Policy ID to update: "))
                name = input("Enter new Policy Name: ")
                premium = float(input("Enter new Premium Amount: "))
                policy = Policy(policyId=pid, policyName=name, premiumAmount=premium)
                if service.updatePolicy(policy):
                    print(" Policy updated.")
                else:
                    print("xxx Update failed xxx")

            elif choice == '5':
                pid = int(input("Enter Policy ID to delete: "))
                if service.deletePolicy(pid):
                    print("xxx Policy deleted. xxx")
                else:
                    print("xxx Failed to delete. xxx")

            elif choice == '6':
                print("Exiting...")
                break

            else:
                print("xxx Invalid choice. Please try again. xxx")

        except PolicyNotFoundException as pnf:
            print("!!!",pnf)

        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()