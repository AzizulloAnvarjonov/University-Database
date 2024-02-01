from main import Database



def faculty():
    query = """
CREATE TABLE faculty (
    faculty_id SERIAL PRIMARY KEY,
    name VARCHAR(25),
    create_date DATE,
    description VARCHAR(25));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


def speciality():
    query = """
CREATE TABLE speciality (
    speciality_id SERIAL PRIMARY KEY,
    name VARCHAR(25),
    education_type VARCHAR(25),
    faculty_id INT REFERENCES faculty(faculty_id));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


def subject():
    query = """
CREATE TABLE subject (
    subject_id SERIAL PRIMARY KEY,
    name VARCHAR(20),
    credit INT,
    teacher_id INT,
    semester INT,
    create_date DATE DEFAULT NOW());"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


def subject_faculty():
    query = """
CREATE TABLE subject_faculty (
    faculty_id INT REFERENCES faculty(faculty_id),
    subject_id INT REFERENCES subject(subject_id));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


def user():
    query = """
CREATE TABLE user (
    teacher_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20),
    last_name VARCHAR(20),
    status VARCHAR(20),
    birth_year INT,
    gender VARCHAR(10),
    salary NUMERIC(10, 2),
    username VARCHAR(25),
    password VARCHAR(25));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


def teacher_subject():
    query = """
CREATE TABLE teacher_subject (
    teacher_id INT REFERENCES user(teacher_id),
    subject_id INT REFERENCES subject(subject_id));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


def teacher_faculty():
    query = """
CREATE TABLE teacher_faculty(
    teacher_id INT REFERENCES user(teacher_id),
    faculty_id INT REFERENCES faculty(faculty_id));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)

def control():
    query = """
CREATE TABLE control (
    control_id SERIAL PRIMARY KEY,
    name VARCHAR(25));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


def user_control():
    query = """
CREATE TABLE user_control (
    teacher_id INT REFERENCES user(teacher_id),
    control_id INT REFERENCES control(control_id));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)




def group():
    query = """
CREATE TABLE group_table(
    group_id SERIAL PRIMARY KEY,
    name VARCHAR(25),
    student_count INT,
    faculty_id INT REFERENCES faculty(faculty_id));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


def students():
    query = """
CREATE TABLE students(
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(25),
    last_name VARCHAR(25),
    birth_year DATE,
    phone_number VARCHAR(20),
    address VARCHAR(255),
    gender VARCHAR(10),
    specialty_id INT,
    group_id INT REFERENCES group_table(group_id));"""

    Database.connect("localhost", "university", "postgres", "azizullo", query)


if __name__ == "__main__":
    faculty()
    speciality()
    subject()
    subject_faculty()
    user()
    teacher_faculty()
    teacher_subject()
    control()
    user_control()
    group()
    students()
