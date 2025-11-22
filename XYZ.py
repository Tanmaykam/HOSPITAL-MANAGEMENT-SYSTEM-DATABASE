import mysql.connector

# Database connection class
class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Tanmay@12345",
            database="hospital"
        )
        self.cursor = self.conn.cursor()

    def commit(self):
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


# Create DB object
db = Database()


# CREATE TABLE
def create_table():
    query = """
    CREATE TABLE IF NOT EXISTS patients(
        patient_id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100),
        age INT,
        gender VARCHAR(20),
        disease VARCHAR(200),
        doctor VARCHAR(100),
        phone VARCHAR(15)
    );
    """
    db.cursor.execute(query)
    db.commit()
    print("✔ Table 'patients' ready!")


# ADD PATIENT
def add_patient():
    name = input("Enter Patient Name: ")
    age = int(input("Enter Age: "))
    gender = input("Enter Gender (Male/Female/Other): ")
    disease = input("Enter Disease: ")
    doctor = input("Enter Doctor Name: ")
    phone = input("Enter Phone Number: ")

    query = """
        INSERT INTO patients(name, age, gender, disease, doctor, phone)
        VALUES (%s, %s, %s, %s, %s, %s)
    """
    values = (name, age, gender, disease, doctor, phone)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Patient added successfully!")



def view_patients():
    query = "SELECT * FROM patients"
    db.cursor.execute(query)
    rows = db.cursor.fetchall()

    print("\n------ PATIENT LIST ------")
    for row in rows:
        print(row)
    print("--------------------------\n")



def update_patient():
    patient_id = int(input("Enter Patient ID to update: "))

    print("""
1. Update Name
2. Update Age
3. Update Gender
4. Update Disease
5. Update Doctor
6. Update Phone
""")

    choice = input("Choose field: ")

    if choice == "1":
        column = "name"
        new_value = input("Enter New Name: ")

    elif choice == "2":
        column = "age"
        new_value = int(input("Enter New Age: "))

    elif choice == "3":
        column = "gender"
        new_value = input("Enter New Gender: ")

    elif choice == "4":
        column = "disease"
        new_value = input("Enter New Disease: ")

    elif choice == "5":
        column = "doctor"
        new_value = input("Enter New Doctor Name: ")

    elif choice == "6":
        column = "phone"
        new_value = input("Enter New Phone: ")

    else:
        print("Invalid option!")
        return

    query = f"UPDATE patients SET {column}=%s WHERE patient_id=%s"
    values = (new_value, patient_id)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Patient updated successfully!")



def delete_patient():
    patient_id = int(input("Enter Patient ID to delete: "))

    query = "DELETE FROM patients WHERE patient_id=%s"
    values = (patient_id,)

    db.cursor.execute(query, values)
    db.commit()
    print("✔ Patient deleted successfully!")



def menu():
    create_table()

    while True:
        print("""
========== HOSPITAL MANAGEMENT SYSTEM ==========
1. Add Patient
2. View Patients
3. Update Patient
4. Delete Patient
5. Exit
""")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            update_patient()
        elif choice == "4":
            delete_patient()
        elif choice == "5":
            print("✔ Exiting...")
            db.close()
            break
        else:
            print("❌ Invalid option, try again!")



menu()
