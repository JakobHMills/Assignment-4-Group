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
        self.doctors = []
        self.read_doctors_file() # reads a file and creates a list of doctors
    
    def read_doctors_file(self):
        file = open("doctors.txt")
        # read and skip table header
        file.readline()
        # read first row
        row = file.readline() 
        while(row != ""):
            split = row.split("_") 
            doctor = Doctor(split[0],split[1],split[2],split[3],split[4],split[5]) #doctor object
            self.doctors.append(doctor) # adding doctor objects to a list
            row = file.readline()
        file.close

    def display_doctors_list(self):
        format_string = "{:<5} {:<15} {:<15} {:<15} {:<15} {:<15}"
        print(format_string.format('Id','Name', 'Speciality', 'Timing', 'Qualification', 'Room Number'), '\n')
        for doctor in self.doctors:
            print(format_string.format(doctor.get_doctor_id(), doctor.get_name(), doctor.get_specialization(), doctor.get_working_time(), doctor.get_qualification(), doctor.get_room_number()))
    
    def format_dr_info(self, doctor):
        return doctor.__str__()
 

doctormanager1 = DoctorManager()
