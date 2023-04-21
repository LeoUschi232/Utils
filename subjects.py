from enum import Enum

fields_and_their_subjects = {
    "Physics": {
        "QM": "Quantum Mechanics",
        "AT": "Atomic Physics and Thermodynamics",
        "MAT": "Material Science",
        "ENE": "Energy Science",
    },
    "Informatics": {
        "FPV": "Functional Programming and Verification",
    }
}


class Subject(Enum):
    QM = "QM"
    FPV = "FPV"
    AT = "AT"
    MAT = "MAT"
    ENE = "ENE"

    @property
    def long_name(self):

        for field, subject_dict in fields_and_their_subjects.items():
            if self.value in subject_dict:
                return subject_dict[self.value]

    @property
    def field(self):
        for field, subject_dict in fields_and_their_subjects.items():
            if self.value in subject_dict:
                return field
