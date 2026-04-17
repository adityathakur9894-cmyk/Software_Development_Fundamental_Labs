class RequisitionSystem:
    id_counter = 10000
    all_requisitions = []

    def __init__(self):
        RequisitionSystem.id_counter += 1
        self.requisition_id = RequisitionSystem.id_counter
        self.date = ""
        self.staff_id = ""
        self.name = ""
        self.option = []
        self.total_cost = 0
        self.status = "Pending"
        self.ref_number = "Not available"

        RequisitionSystem.all_requisitions.append(self)

    # Task 1 (same as your code)
    def staff_info(self):
        self.date = input("today's date in DD/MM/YYYY: ")
        self.staff_id = input("your staff ID: ")
        self.name = input("Enter your name: ")

    # Task 2 (same logic)
    def requisitions_total(self):
        while True:
            item = input("Enter Item/addons you want buy (or 'Done'): ")
            if item.lower() == 'done':
                break
            try:
                price = float(input(f"Enter price for '{item}': $"))
                self.option.append((item, price))
                self.total_cost += price
            except ValueError:
                print("Invalid price, enter number")

    # Task 3 (same logic)
    def requisition_approval(self):
        if self.total_cost > 0 and self.total_cost < 500:
            self.status = "Approved"
            self.ref_number = self.staff_id.upper() + str(self.requisition_id)[-3:]
        else:
            self.status = "Pending"

    # NEW: manager response
    def respond_requisition(self):
        if self.status == "Pending":
            decision = input(f"Approve requisition {self.requisition_id}? (yes/no): ")
            if decision.lower() == "yes":
                self.status = "Approved"
                self.ref_number = self.staff_id.upper() + str(self.requisition_id)[-3:]
            elif decision.lower() == "no":
                self.status = "Not approved"

    # Task 4 (display all)
    @classmethod
    def display_requisitions(cls):
        print("\n\nPrinting Requisitions:\n")
        for r in cls.all_requisitions:
            print(f"Date: {r.date}")
            print(f"Requisition ID: {r.requisition_id}")
            print(f"Staff ID: {r.staff_id}")
            print(f"Staff Name: {r.name}")
            print(f"Total: ${r.total_cost:.2f}")
            print(f"Status: {r.status}")

            if r.status == "Approved":
                print(f"Approval Reference Number: {r.ref_number}")
            else:
                print("Approval Reference Number: Not available")

            print("-" * 40)

    # Statistics (required)

    def requisition_statistics(cls):
        total = len(cls.all_requisitions)
        approved = sum(1 for r in cls.all_requisitions if r.status == "Approved")
        pending = sum(1 for r in cls.all_requisitions if r.status == "Pending")
        not_approved = sum(1 for r in cls.all_requisitions if r.status == "Not approved")

        print("\nStatistics:")
        print(f"The total number of requisitions submitted: {total}")
        print(f"The total number of approved requisitions: {approved}")
        print(f"The total number of pending requisitions: {pending}")
        print(f"The total number of not approved requisitions: {not_approved}")


# -------- MAIN --------
def main():
    n = int(input("How many requisitions you want to enter: "))

    # create requisitions
    for i in range(n):
        print(f"\nEnter details for requisition {i+1}")
        req = RequisitionSystem()
        req.staff_info()
        req.requisitions_total()
        req.requisition_approval()

    # before manager decision
    RequisitionSystem.display_requisitions()
    RequisitionSystem.requisition_statistics()

    # manager response
    print("\nManager reviewing pending requisitions...\n")
    for r in RequisitionSystem.all_requisitions:
        r.respond_requisition()

    # after manager decision
    RequisitionSystem.display_requisitions()
    RequisitionSystem.requisition_statistics()


if __name__ == "__main__":
    main()