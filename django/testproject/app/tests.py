from django.test import TestCase
from .models import Department, Student

class DepartmentModelTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(dept_id=1, dept_name='Computer Science', dept_head='John Doe')

    def test_department_str_representation(self):
        self.assertEqual(str(self.department), 'Computer Science')

class StudentModelTestCase(TestCase):
    def setUp(self):
        self.department = Department.objects.create(dept_id=1, dept_name='Computer Science', dept_head='John Doe')
        self.student = Student.objects.create(std_id=1, first_name='Jane', last_name='Doe', department=self.department)

    def test_student_str_representation(self):
        self.assertEqual(str(self.student), 'Jane Doe')

    def test_student_full_name_property(self):
        self.assertEqual(self.student.full_name, 'Jane Doe')

    def test_student_department_relation(self):
        self.assertEqual(self.student.department, self.department)
