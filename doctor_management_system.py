class Doctor:
    def __init__(self, doctor_id="", name="", specialization="", working_time="", qualification="", room_number=""):
        self.doctor_id = doctor_id
        self.name = name
        self.specialization = specialization
        self.working_time = working_time
        self.qualification = qualification
        self.room_number = room_number

    def get_doctor_id(self): 
        return self.doctor_id
    
    def get_name(self):
        return self.name
    
    def get_specialization(self):
        return self.specialization
    
    def get_working_time(self):
        return self.working_time
    
    def get_qualification(self):
        return self.qualification
    
    def get_room_number(self):
        return self.room_number
    
    def set_doctor_id(self, new_id):
        self.doctor_id = new_id

    def set_name(self, new_name):
        self.name = new_name

    def set_specialization(self, new_specialization):
        self.specialization = new_specialization

    def set_working_time(self, new_working_time):
        self.working_time = new_working_time

    def set_qualification(self, new_qualification):
        self.qualification = new_qualification

    def set_room_number(self, new_room_number):
        self.room_number = new_room_number

    def __str__(self):
        return str(self.doctor_id) + "_" + self.name + "_" + self.specialization + "_" + self.working_time + "_" + self.qualification + "_" + str(self.room_number)
    
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
        id = input("Enter the doctor's ID: ")
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
            doctor = Doctor(split[0],split[1],split[2],split[3],split[4],split[5].strip()) #doctor object
            # add doctor object to the list of doctors
            self.doctors.append(doctor)
            # read next line
            row = file.readline()
        # close file
        file.close
    
    def search_doctor_by_id(self):
        # ask for doctor id from user
        id = input("Enter the doctor Id: ")
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
        name = input("Enter the doctor name: ")
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
        print(format_string.format('Id','Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'), '\n')
        # display doctor information
        print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()), "\n")

    def edit_doctor_info(self):
        # asks user to enter the doctor id
        id = input("Please enter the id of the doctor that you want to edit their information: ")
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
        print(format_string.format('Id','Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'), '\n')
        # display information for all doctors
        for doctor in self.doctors:
            print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()), "\n")

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