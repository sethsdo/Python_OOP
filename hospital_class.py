#Hospital

#patient class
class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed_number = None
    def __repr__(self):
        return '{}, {}, {}, {}'.format(self.id, self.name, self.allergies, self.bed_number)

class Hospital(object):
    def __init__(self, hospital_name, compacity):
        self.patients = []
        self.hospital_name = hospital_name
        self.compacity = compacity

    def Admit(self, petient, bedNum):
        if len(self.patients) < self.compacity: 
            self.patients.append(petient)
            #adds bednum to spicific  petient object
            petient.bed_number = bedNum
            print "Addmission complete"
            print self.patients
            return self
        else:
            print "compacity reached"
            return self

    def Discharge(self, removal_key):
        for i in self.patients:
            if i.id == removal_key:
                self.patients.remove(i)
                i.bed_number = None
    
    def Hospital_info(self):
        print self.hospital_name
        print self.compacity
        return self

#petient objects         
petient1 = Patient(1,"Donald","penuts, rasins, cheese")
petient2 = Patient(1,"Donald","penuts, rasins, cheese")
petient3 = Patient(1,"Donald","penuts, rasins, cheese")
petient4 = Patient(1,"Donald","penuts, rasins, cheese")
petient5 = Patient(1,"Donald","penuts, rasins, cheese")
admit = Hospital("North ST CEN", 5)
admit.Admit(petient1, 23).Hospital_info()
