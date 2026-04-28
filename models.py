from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Boolean, Float, JSON
from sqlalchemy.orm import relationship
from database import Base
from datetime import datetime


class Material(Base):
    __tablename__ = "materials"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    file_path = Column(String(500), nullable=False)
    file_type = Column(String(50), nullable=False)
    content_text = Column(Text, default="")
    knowledge_base = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    questions = relationship("Question", back_populates="material", cascade="all, delete")
    courses = relationship("CourseMaterial", back_populates="material", cascade="all, delete")


class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, index=True)
    material_id = Column(Integer, ForeignKey("materials.id"))
    question_text = Column(Text, nullable=False)
    question_type = Column(String(20), default="choice")  # choice, true_false, fill_blank
    options = Column(JSON, default=list)  # ["A. xxx", "B. xxx", ...]
    correct_answer = Column(String(255), nullable=False)
    explanation = Column(Text, default="")
    created_at = Column(DateTime, default=datetime.now)

    material = relationship("Material", back_populates="questions")


class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, default="")
    certification_type = Column(String(255), default="")
    start_date = Column(DateTime, nullable=True)
    end_date = Column(DateTime, nullable=True)
    status = Column(String(20), default="draft")  # draft, open, closed, completed
    created_at = Column(DateTime, default=datetime.now)

    enrollments = relationship("Enrollment", back_populates="course", cascade="all, delete")
    materials = relationship("CourseMaterial", back_populates="course", cascade="all, delete")
    exams = relationship("Exam", back_populates="course", cascade="all, delete")


class CourseMaterial(Base):
    __tablename__ = "course_materials"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    material_id = Column(Integer, ForeignKey("materials.id"))

    course = relationship("Course", back_populates="materials")
    material = relationship("Material", back_populates="courses")


class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    employee_no = Column(String(50), unique=True, index=True, nullable=False)  # ACC账号
    name = Column(String(100), nullable=False)
    county = Column(String(100), default="")       # 县分
    branch = Column(String(100), default="")       # 支局
    department = Column(String(100), default="")   # 部门（县分+支局组合）
    position = Column(String(100), default="")     # 基准岗位名称
    emp_type = Column(String(20), default="")      # 类型：自维/外包
    email = Column(String(255), default="")
    password = Column(String(255), default="")     # 登录密码
    certifications = Column(JSON, default=list)  # [{"name": "", "status": "", "date": ""}]
    skill_tags = Column(JSON, default=list)
    practical_scores = Column(JSON, default=dict)  # {"认证名称": 分数}
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    enrollments = relationship("Enrollment", back_populates="employee", cascade="all, delete")
    exam_results = relationship("ExamResult", back_populates="employee", cascade="all, delete")
    certificates = relationship("Certificate", back_populates="employee", cascade="all, delete")


class Enrollment(Base):
    __tablename__ = "enrollments"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    status = Column(String(20), default="registered")  # registered, learning, completed, failed
    registered_at = Column(DateTime, default=datetime.now)
    completed_at = Column(DateTime, nullable=True)

    course = relationship("Course", back_populates="enrollments")
    employee = relationship("Employee", back_populates="enrollments")


class Exam(Base):
    __tablename__ = "exams"
    id = Column(Integer, primary_key=True, index=True)
    course_id = Column(Integer, ForeignKey("courses.id"))
    title = Column(String(255), nullable=False)
    duration = Column(Integer, default=60)  # minutes
    passing_score = Column(Integer, default=60)
    total_score = Column(Integer, default=100)
    question_ids = Column(JSON, default=list)
    status = Column(String(20), default="draft")  # draft, published, closed
    created_at = Column(DateTime, default=datetime.now)

    course = relationship("Course", back_populates="exams")
    results = relationship("ExamResult", back_populates="exam", cascade="all, delete")


class ExamResult(Base):
    __tablename__ = "exam_results"
    id = Column(Integer, primary_key=True, index=True)
    exam_id = Column(Integer, ForeignKey("exams.id"))
    employee_id = Column(Integer, ForeignKey("employees.id"))
    score = Column(Float, default=0)
    answers = Column(JSON, default=dict)  # {question_id: answer}
    passed = Column(Boolean, default=False)
    submitted_at = Column(DateTime, default=datetime.now)

    exam = relationship("Exam", back_populates="results")
    employee = relationship("Employee", back_populates="exam_results")


class ImportHistory(Base):
    __tablename__ = "import_history"
    id = Column(Integer, primary_key=True, index=True)
    import_type = Column(String(50), default="material")  # material, employee, practical, certificate
    source = Column(String(500), default="")  # 来源路径或描述
    file_name = Column(String(255), default="")
    operator = Column(String(100), default="")  # 操作人ACC
    success_count = Column(Integer, default=0)
    fail_count = Column(Integer, default=0)
    details = Column(Text, default="")  # 详细记录
    created_at = Column(DateTime, default=datetime.now)


class EmployeeCertification(Base):
    __tablename__ = "employee_certifications"
    id = Column(Integer, primary_key=True, index=True)
    employee_no = Column(String(50), index=True, nullable=False)  # ACC
    name = Column(String(100), default="")
    county = Column(String(100), default="")
    branch = Column(String(100), default="")
    emp_type = Column(String(20), default="")
    is_contracted = Column(String(20), default="")  # 是否承包
    star_level = Column(String(20), default="")  # 第3期星级
    
    # 各认证状态（0/1）
    has_electrician_cert = Column(Integer, default=0)  # 通过电工证
    has_height_work_cert = Column(Integer, default=0)  # 通过高空作业证
    has_line_specialist = Column(Integer, default=0)  # 线路一人多专
    has_equipment_specialist = Column(Integer, default=0)  # 设备一人多专
    has_wireless_specialist = Column(Integer, default=0)  # 无线一人多专
    has_power_specialist = Column(Integer, default=0)  # 动力一人多专
    has_all_yizhichan = Column(Integer, default=0)  # 所有专业一指禅
    
    # 等级
    has_group_level3 = Column(Integer, default=0)
    has_group_level4 = Column(Integer, default=0)
    has_group_level5 = Column(Integer, default=0)
    has_special_double_cert = Column(Integer, default=0)
    group_cert_count = Column(Integer, default=0)
    specialist_cert_count = Column(Integer, default=0)
    
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)


class Certificate(Base):
    __tablename__ = "certificates"
    id = Column(Integer, primary_key=True, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id"))
    cert_name = Column(String(255), nullable=False)
    cert_no = Column(String(255), default="")
    issue_date = Column(String(50), default="")
    expiry_date = Column(String(50), default="")
    issuer = Column(String(255), default="")
    scan_path = Column(String(500), default="")
    verified = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)

    employee = relationship("Employee", back_populates="certificates")
