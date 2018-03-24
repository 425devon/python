class Patient(object):
    def __init__(self, id, name, allergies):
        self.id = id
        self.name = name
        self.allergies = allergies
        self.bed = "None"
class Hospital(object):
    def __init__(self, name):
        self.patients = []
        self.name = name
        self.capacity = 10
        self.bednum = [1,2,3,4,5,6,7,8,9,10]
    def admit(self, patient):
        newPatient = {'id':patient.id,'name':patient.name,'allergies':patient.allergies,'bed':self.bednum[0]}
        if len(self.patients) >= self.capacity:
            print "You're out of luck we're full"
            return
        else:
            del self.bednum[0]
            self.patients.append(newPatient)
            print "You've been admited, your bed number is {}".format(newPatient['bed'])
        return self
    def discharge(self,id):
        for i in range(len(self.patients)):
            if self.patients[i]['id'] == id:
                print "Patient found"
                self.bednum.append(self.patients[i]['bed'])
                del self.patients[i]
                return
            
            print "patient not found"    
        return self

testHospital = Hospital("Arbor Heights Hospital")

testPatient = Patient(991425,"John Doe",["nuts","morphine"])
testPatient2 = Patient(991145,"Mike Mueller",["cats"])
testPatient3 = Patient(991155,"Don Kingsly",["candy","spice"])
testPatient4 = Patient(991165,"Sarah Smith",["boys","pop-music"])

testHospital.admit(testPatient)
testHospital.admit(testPatient2)
testHospital.admit(testPatient3)
testHospital.admit(testPatient4)

testHospital.discharge(991155)

print testHospital.patients, testHospital.bednum





