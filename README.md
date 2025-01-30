# EducationTracker

EducationTracker is a PostgreSQL-based database system designed for managing student, course, and grading information in a university or academic setting. It includes features for tracking student grades, managing courses, assigning teachers to subjects, and performing various queries related to academic performance.

## Features

- **Student Management**: Keep track of students, their groups, and grades.
- **Teacher Management**: Assign teachers to courses and subjects.
- **Course Management**: Manage courses, including the subjects and teachers assigned to them.
- **Grade Tracking**: Record and query student grades by subject and teacher.
- **Comprehensive SQL Queries**: Perform various analytical queries to track student performance, course grades, and teacher evaluations.

## Database Schema

The database consists of the following tables:

- **students**: Information about students and their respective groups.
- **groups**: Group information for organizing students.
- **teachers**: Teacher data, including the courses they teach.
- **subjects**: Subjects offered, linked to teachers.
- **grades**: Student grades for specific subjects, along with the date of grading.

### SQL Tables Structure:

- **groups**  
  - `id`: Integer, primary key  
  - `name`: VARCHAR, name of the group  

- **students**  
  - `id`: Integer, primary key  
  - `fullname`: VARCHAR, full name of the student  
  - `group_id`: Integer, foreign key referencing `groups(id)`

- **teachers**  
  - `id`: Integer, primary key  
  - `fullname`: VARCHAR, full name of the teacher  

- **subjects**  
  - `id`: Integer, primary key  
  - `name`: VARCHAR, subject name  
  - `teacher_id`: Integer, foreign key referencing `teachers(id)`

- **grades**  
  - `id`: Integer, primary key  
  - `student_id`: Integer, foreign key referencing `students(id)`  
  - `subject_id`: Integer, foreign key referencing `subjects(id)`  
  - `grade`: Integer, grade (0 to 100)  
  - `grade_date`: DATE, date when the grade was assigned

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/paulmusquaro/EducationTracker.git
    cd EducationTracker
    ```

2. Set up a PostgreSQL database:
    - Create a database in PostgreSQL.
    - Import the provided schema (create_tables.sql) to set up the database tables.
  
3. Install required Python packages via `pipenv`

4. Update database connection settings in the script files to match your PostgreSQL configuration.

5. Run the script to populate the database with random data using Faker:
    ```bash
    python main.py
    ```

6. Use the migration and query scripts to perform operations on the database.

## Usage

- The system provides SQL scripts for common queries, including:
  - Finding the top 5 students with the highest average grade across all subjects.
  - Querying the highest-scoring student in a specific subject.
  - Calculating the average grade in a group for a particular subject.
  - Analyzing teacher performance across their subjects.
  - Getting a list of courses attended by a student.


### Example Queries:
- **Query 1**: Find the top 5 students with the highest average grade across all subjects.
- **Query 2**: Find the student with the highest average grade in a specific subject.
- **Query 3**: Calculate the average grade in a group for a given subject.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
