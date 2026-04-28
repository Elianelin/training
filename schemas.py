from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime


# Material schemas
class MaterialBase(BaseModel):
    title: str


class MaterialCreate(MaterialBase):
    pass


class MaterialResponse(MaterialBase):
    id: int
    file_path: str
    file_type: str
    content_text: str
    knowledge_base: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Question schemas
class QuestionBase(BaseModel):
    question_text: str
    question_type: str = "choice"
    options: List[str] = []
    correct_answer: str
    explanation: str = ""


class QuestionCreate(QuestionBase):
    material_id: int


class QuestionResponse(QuestionBase):
    id: int
    material_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Course schemas
class CourseBase(BaseModel):
    title: str
    description: str = ""
    certification_type: str = ""
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None


class CourseCreate(CourseBase):
    pass


class CourseUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    certification_type: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    status: Optional[str] = None


class CourseResponse(CourseBase):
    id: int
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class CourseDetail(CourseResponse):
    materials: List[MaterialResponse] = []


# Enrollment schemas
class EnrollmentBase(BaseModel):
    course_id: int
    employee_id: int


class EnrollmentCreate(BaseModel):
    course_id: int
    employee_id: int


class EnrollmentByAcc(BaseModel):
    course_id: int
    employee_acc: str


class EnrollmentResponse(EnrollmentBase):
    id: int
    status: str
    registered_at: datetime
    completed_at: Optional[datetime] = None
    employee: Optional[Dict[str, Any]] = None

    class Config:
        from_attributes = True


# Employee schemas
class EmployeeBase(BaseModel):
    employee_no: str
    name: str
    county: str = ""
    branch: str = ""
    department: str = ""
    position: str = ""
    emp_type: str = ""
    email: str = ""


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    county: Optional[str] = None
    branch: Optional[str] = None
    department: Optional[str] = None
    position: Optional[str] = None
    emp_type: Optional[str] = None
    email: Optional[str] = None
    certifications: Optional[List[Dict]] = None
    skill_tags: Optional[List[str]] = None
    practical_scores: Optional[Dict[str, float]] = None


class EmployeeResponse(EmployeeBase):
    id: int
    certifications: List[Dict] = []
    skill_tags: List[str] = []
    practical_scores: Dict[str, float] = {}
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


# Exam schemas
class ExamBase(BaseModel):
    title: str
    duration: int = 60
    passing_score: int = 60
    total_score: int = 100


class ExamCreate(ExamBase):
    course_id: int
    question_ids: List[int] = []


class ExamUpdate(BaseModel):
    title: Optional[str] = None
    duration: Optional[int] = None
    passing_score: Optional[int] = None
    status: Optional[str] = None


class ExamResponse(ExamBase):
    id: int
    course_id: int
    question_ids: List[int] = []
    status: str
    created_at: datetime

    class Config:
        from_attributes = True


class ExamSubmit(BaseModel):
    answers: Dict[str, str]


class ExamResultResponse(BaseModel):
    id: int
    exam_id: int
    employee_id: int
    score: float
    passed: bool
    submitted_at: datetime

    class Config:
        from_attributes = True


# Certificate schemas
class CertificateBase(BaseModel):
    cert_name: str
    cert_no: str = ""
    issue_date: str = ""
    expiry_date: str = ""
    issuer: str = ""


class CertificateCreate(CertificateBase):
    employee_id: int


class CertificateResponse(CertificateBase):
    id: int
    employee_id: int
    scan_path: str
    verified: bool
    created_at: datetime

    class Config:
        from_attributes = True


# Auth schemas
class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: Optional[Dict] = None


# ImportHistory schemas
class ImportHistoryResponse(BaseModel):
    id: int
    import_type: str
    source: str
    file_name: str
    operator: str
    success_count: int
    fail_count: int
    details: str
    created_at: datetime

    class Config:
        from_attributes = True


# EmployeeCertification schemas
class EmployeeCertificationBase(BaseModel):
    employee_no: str
    name: str = ""
    county: str = ""
    branch: str = ""
    emp_type: str = ""
    is_contracted: str = ""
    star_level: str = ""
    has_electrician_cert: int = 0
    has_height_work_cert: int = 0
    has_line_specialist: int = 0
    has_equipment_specialist: int = 0
    has_wireless_specialist: int = 0
    has_power_specialist: int = 0
    has_all_yizhichan: int = 0
    has_group_level3: int = 0
    has_group_level4: int = 0
    has_group_level5: int = 0
    has_special_double_cert: int = 0
    group_cert_count: int = 0
    specialist_cert_count: int = 0


class EmployeeCertificationResponse(EmployeeCertificationBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class CertificationDashboard(BaseModel):
    total_employees: int
    total_contracted: int
    total_by_type: Dict[str, int]
    total_by_county: Dict[str, int]
    cert_stats: Dict[str, int]
    star_stats: Dict[str, int]
    avg_specialist_count: float


# General response
class MessageResponse(BaseModel):
    message: str
    data: Optional[Any] = None
