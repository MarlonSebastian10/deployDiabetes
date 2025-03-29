from pydantic import BaseModel

class dataTest(BaseModel):
    nombre: str
    estudiantes: float

class DataEnfermedad(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int