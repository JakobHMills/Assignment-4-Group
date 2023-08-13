# Members: Jaeeun Lee, Jakob Mills, Donald Jans Uy
# Date: August 11, 2023
# Assignment 3
# What it does: The hospital management system reads doctor and patient information from .txt files and loads it into the program. 
# Users can then display the list of all doctors/patients or display information for a single doctor/patient by searching for
# their id or name (doctor only). Users can also add and edit a doctor/patient and save it to the .txt file.

class Doctor:
    def __init__(self, doctor_id="", name="", specialization="", working_time="", qualification="", room_number=""):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    # Get doctor id
    def get_doctor_id(self): 
        return self.doctor_id
    
    # Get name
    def get_name(self):
        return self.name
    
    # Get specialization
    def get_specialization(self):
        return self.specialization
    
    # Get working time
    def get_working_time(self):
        return self.working_time
    
    # Get qualification
    def get_qualification(self):
        return self.qualification
    
    # Get room number
    def get_room_number(self):
        return self.room_number
    
    # Set doctor id 
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    # Set name
    def set_name(self, new_name):
        self.name = new_name

    # Set specialization
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    # Set working time
    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    # Set qualification
    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    # Set room number
    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    # Returns a string of doctor properties separated by underscores
    def __str__(self):
        return self.doctor_id + "_" + self.name + "_" + self.specialization + "_" + self.working_time + "_" + self.qualification + "_" + self.room_number
    
class DoctorManager:
    def __init__(self):
        # create empty list of doctors
        self.doctors = []
        # load doctors data from doctors.txt into doctors list
        self.read_doctors_file()
    
    def format_dr_info(self, doctor):
        return doctor.__str__()
    
    def enter_dr_info(self):
        # ask users for doctor info
        id = input("\nEnter the doctor's ID: ")
        name = input("Enter the doctor's name: ")
        specility = input("Enter the doctor's specility: ")
        timing = input("Enter the doctor's timing (e.g., 7am-10pm): ")
        qualification = input("Enter the doctor's qualification: ")
        room_number = input("Enter the doctor's room number: ")
        # return doctor object
        return Doctor(id, name, specility, timing, qualification, room_number)
    
    def read_doctors_file(self):
        # open file doctors.txt
        file = open("doctors.txt")
        # read and skip table header
        file.readline()
        # read first row
        row = file.readline() 
        while(row != ""):
            # split row into list of doctor properties
            split = row.split("_") 
            # create a doctor object using the doctor properties
            doctor = Doctor(split[0],split[1],split[2],split[3],split[4],split[5].strip())
            # add doctor object to the list of doctors
            self.doctors.append(doctor)
            # read next line
            row = file.readline()
        # close file
        file.close
    
    def search_doctor_by_id(self):
        # ask for doctor id from user
        id = input("\nEnter the doctor Id: ")
        # search for doctor id in doctors list
        for doctor in self.doctors:
            if doctor.get_doctor_id() == id:
                # displays doctor information if doctor exists
                self.display_doctor_info(doctor)
                return
        # otherwise displays "Can't find the doctor..."
        print("Can't find the doctor with the same ID on the system")

    def search_doctor_by_name(self):
        # ask for doctor name from user
        name = input("\nEnter the doctor name: ")
        # search for doctor name in doctors list
        for doctor in self.doctors:
            if doctor.get_name() == name:
                # displays doctor information if doctor exists
                self.display_doctor_info(doctor)
                return
        # otherwise displays "Can't find the doctor..."
        print("Can't find the doctor with the same name on the system")

    def display_doctor_info(self, doctor):
        # format string for displaying columns
        format_string = "{:<5} {:<15} {:<15} {:<15} {:<15} {:<15}"
        # display header row
        print(format_string.format("\n"'Id','Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'), '\n')
        # display doctor information
        print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))

    def edit_doctor_info(self):
        # asks user to enter the doctor id
        id = input("\nPlease enter the id of the doctor that you want to edit their information: ")
        # searches the doctors list to find the doctor who has the id
        for doctor in self.doctors:
            if doctor.get_doctor_id() == id:
                # get doctor information from the user and update the information
                doctor.set_name(input("Enter the doctor's name: "))
                doctor.set_specialization(input("Enter the doctor's specility: "))
                doctor.set_working_time(input("Enter the doctor's timing: "))
                doctor.set_qualification(input("Enter the doctor's qualification: "))
                doctor.set_room_number(input("Enter the doctor's room number: "))
                # write the updated doctors list to doctors.txt
                self.write_list_of_doctors_to_file()
                # confirms the doctor has been edited
                print("\nDoctor whose ID", id, "has been edited")
                return
        # if the doctor doesn't exist
        print("Can't find the doctor with the same ID on the system")

    def display_doctors_list(self):
        # format string for displaying columns
        format_string = "{:<5} {:<15} {:<15} {:<15} {:<15} {:<15}"
        # print header row
        print(format_string.format('Id','Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'))
        # display information for all doctors
        for doctor in self.doctors:
            print("")
            print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))

    def write_list_of_doctors_to_file(self):
        # open file to write
        file = open("doctors.txt", "w")
        # write header row
        file.write("id_name_specilist_timing_qualification_roomNb\n")
        # write information for each doctor
        for doctor in self.doctors:
            file.write(self.format_dr_info(doctor)+'\n')
        # close file
        file.close

    def add_dr_to_file(self):
        # create new doctor by asking user for information
        new_doctor = self.enter_dr_info()
        # append new doctor to the doctors list
        self.doctors.append(new_doctor)
        # write list of doctors to file
        self.write_list_of_doctors_to_file()
        # display confirmation message
        print("\nDoctor whose ID is", new_doctor.get_doctor_id(), "has been added")
           
class Patient:
    def __init__(self, id="", name="", disease="", gender="", age=""):
        self.id = id
        self.name = name
        self.disease = disease
        self.gender = gender
        self.age = age

    def get_id(self):
        return self.id

    def set_id(self, new_id):
        self.id = new_id

    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    def get_disease(self):
        return self.disease

    def set_disease(self, new_disease):
        self.disease = new_disease

    def get_gender(self):
        return self.gender

    def set_gender(self, new_gender):
        self.gender = new_gender

    def get_age(self):
        return self.age

    def set_age(self, new_age):
        self.age = new_age

    def __str__(self):
        return f"{self.id}_{self.name}_{self.disease}_{self.gender}_{self.age}"

class PatientManager:
    def __init__(self):
        # Creates empty list of patients 
        self.patients = [] 
        # Loads Patients data from the text into the list
        self.read_patients_file()

    def format_patient_Info_for_file(self,patients):
        return patients.__str__()

    def enter_patient_info(self):
        # Asks user for patient information 
        id = input("\nEnter patient Id: ")
        name = input("Enter patient name: ")
        disease = input("Enter patient disease: ")
        gender = input("Enter patient gender: ")
        age = input("Enter patient age: ")
        
        patient_obj = Patient(id, name, disease, gender, age)
        # Returns the infomation gained 
        return patient_obj
    
    def read_patients_file(self):
        # Opens the file patients.txt
        with open("patients.txt", "r") as file:
            file.readline()
            for line in file:
                patient_data = line.strip().split("_")
                if len(patient_data) == 5:
                    patient_data = Patient(patient_data[0], patient_data[1], patient_data[2], patient_data[3], patient_data[4])
                    self.patients.append(patient_data)
    
    def search_patient_by_Id(self):
        # Asks for the patient id from the user
        patient_id = input("\nEnter the Patient Id: ")
        for patient_data in self.patients:
             if patient_data.get_id() == patient_id:
                 # Displays the patient info if available 
                 self.display_patient_info(patient_data)
                 return 

        print("Can't find the Patient with the same id on the system")

    def display_patient_info(self, patient_data):
        # format string for displaying columns
        format_string = "{:<5} {:<20} {:<15} {:<15} {:<15}"
        # display header row
        print(format_string.format("\n"'Id','Name', 'Disease', 'Gender', 'Age'), '\n')
        # display doctor information
        print(format_string.format(patient_data.get_id(), patient_data.get_name(), patient_data.get_disease(), patient_data.get_gender(), patient_data.get_age()))
        
    def edit_patient_info_by_id(self):
        target_id = input("\nPlease enter the id of the Patient that you want to edit their information: ")
        for patient in self.patients:
            if patient.get_id() ==target_id:

                patient.set_name(input("Enter new Name: "))
                patient.set_disease(input("Enter new patient disease: "))
                patient.set_gender(input("Enter new patient gender: "))
                patient.set_age(input("Enter new patient age: "))

                self.write_list_of_patients_to_file()

                print("\nPatient whose ID is", target_id ,"has been edited.")
                return
        print("Cannot find the patient with the given ID.")

    def display_patient_list(self):
        format_string = "{:<5} {:<20} {:<15} {:<15} {:<15}"

        print(format_string.format("\n"'Id','Name', 'Disease', 'Gender', 'Age'))
        for patient in self.patients:
            print()        
            print(format_string.format(patient.get_id(), patient.get_name(), patient.get_disease(), patient.get_gender(), patient.get_age()))

    def write_list_of_patients_to_file(self):
        with open('patients.txt', 'w') as file:
            file.write("id_Name_Disease_Gender_Age\n")
            for patient in self.patients:
                file.write(self.format_patient_Info_for_file(patient)+"\n")
        
    def add_patient_to_file(self):
        new_patient = self.enter_patient_info()
        self.patients.append(new_patient)
        print("Adding new patient to the list:", new_patient)
        
        self.write_list_of_patients_to_file()
        print("\nPatient whose ID is", new_patient.get_id(), "has been added")
        return


def main():
    welcome_value = [1,2,3]

    while True:
        user_welcome_input = int(input("\nWelcome to Alberta Hospital (AH) Management system\nSelect from the following options, or select 0 to stop:\n1 - Doctors\n2 - Patients\n3 - Exit Program\n>>> "))

        if user_welcome_input not in welcome_value:
            print("\nInvalid input, please indicate a correct integer\n")
        else:
 
            if  user_welcome_input == 1:
                doctor_set_menu = [1,2,3,4,5,6]   #sets the allowed values to be inputed by the user
                while True:
                    doctor_initial_menu = int(input("\nDoctors Menu:\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n>>> "))
                    if doctor_initial_menu not in doctor_set_menu:
                            print("\nInvalid input, please indicate a correct integer\n")
                            doctor_initial_menu = int(input("\n1 - Display Doctors list\n2 - Search for doctor by ID\n3 - Search for doctor by name\n4 - Add doctor\n5 - Edit doctor info\n6 - Back to the Main Menu\n>>> "))
                    else:
                            if doctor_initial_menu == 1:                #calls out class and method to display the list of doctors from the file
                                show_doctor_list = DoctorManager()
                                show_doctor_list.display_doctors_list()

                            elif doctor_initial_menu == 2:            #calls out class and method to search a doctor with the ID as reference from the file
                                doctor_by_id = DoctorManager()
                                doctor_by_id.search_doctor_by_id()

                            elif doctor_initial_menu == 3:                #calls out class and method to search a doctor with the Doctor's name as a reference from the file
                                doctor_by_name = DoctorManager()
                                doctor_by_name.search_doctor_by_name()

                            elif doctor_initial_menu == 4:                #calls out class and method to add a doctor having the same format with the file
                                doctor_add_new = DoctorManager()
                                doctor_add_new.add_dr_to_file()

                            elif doctor_initial_menu == 5:                #calls out class and method to edit doctor details from the file
                                doctor_edit = DoctorManager()
                                doctor_edit.edit_doctor_info()

                            elif doctor_initial_menu == 6:                #breaks the loop and returns user back to the Main Menu.
                                break
        
            elif user_welcome_input == 2:          # Patient Part

                patient_initial_input = [1,2,3,4,5]
                while True:
                    patient_details_input = int(input("\nPatients Menu:\n1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu\n>>> "))
                    if patient_details_input not in patient_initial_input:
                        print("\nInvalid input, please indicate a correct integer\n")
                        patient_details_input = int(input("1 - Display patients list\n2 - Search for patient by ID\n3 - Add patient\n4 - Edit patient info\n5 - Back to the Main Menu"))
                    else:
                        if patient_details_input == 1:
                            show_patient_list = PatientManager()
                            show_patient_list.display_patient_list()
                        
                        elif patient_details_input == 2:
                            patient_by_id = PatientManager()
                            patient_by_id.search_patient_by_Id()

                        elif patient_details_input == 3:
                            patient_add_new = PatientManager()
                            patient_add_new.add_patient_to_file()

                        elif patient_details_input == 4:
                            patient_edit = PatientManager()
                            patient_edit.edit_patient_info_by_id()
                        
                        elif patient_details_input == 5:
                            break

            elif user_welcome_input == 3:
                print("Thanks for using the program. Bye!")
                break
                
main()
            
