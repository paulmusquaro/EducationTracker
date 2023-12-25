import logging
from psycopg2 import DatabaseError
from connect import create_connection

if __name__ == '__main__':

    # Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
    sql_expression_01 = """
        SELECT student_id, round(AVG(grade), 0) AS avg_grade
        FROM grades
        GROUP BY student_id
        ORDER BY avg_grade DESC
        LIMIT 5;
        """
    
    # Знайти студента із найвищим середнім балом з певного предмета.
    sql_expression_02 = """
        SELECT student_id, round(AVG(grade), 0) AS avg_grade
        FROM grades
        WHERE subject_id = 2
        GROUP BY student_id
        ORDER BY avg_grade DESC
        LIMIT 1;
        """

    # # Знайти середній бал у групах з певного предмета.
    sql_expression_03 = """
        SELECT groups.id, round(AVG(grades.grade), 0)
        FROM groups
        JOIN students ON groups.id = students.group_id
        JOIN grades ON students.id = grades.student_id
        WHERE grades.subject_id = 2
        GROUP BY groups.id;
        """

    # Знайти середній бал на потоці (по всій таблиці оцінок)
    sql_expression_04 = """
        SELECT ROUND(AVG(grade), 0)
        FROM grades;
        """
    
    # Знайти які курси читає певний викладач.
    sql_expression_05 = """
        select name 
        from subjects
        where teacher_id = 3;
        """

    # Знайти список студентів у певній групі.
    sql_expression_06 = """
        select fullname 
        from students
        where group_id = 3;
        """

    # Знайти оцінки студентів у окремій групі з певного предмета.
    sql_expression_07 = """
        select grades.grade
        from grades
        join students on grades.student_id = students.id
        where students.group_id = 2 and grades.subject_id =2
        """
    
    # # Знайти середній бал, який ставить певний викладач зі своїх предметів.
    sql_expression_08 = """
        SELECT round(AVG(grade), 0)
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE subjects.teacher_id = 2;
        """
    
    # # Знайти список курсів, які відвідує студент.
    sql_expression_09 = """
        SELECT subjects.name
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE grades.student_id = 2;
        """
    
    # # Список курсів, які певному студенту читає певний викладач.
    sql_expression_10 = """
        SELECT subjects.name
        FROM grades
        JOIN subjects ON grades.subject_id = subjects.id
        WHERE grades.student_id = 4 AND subjects.teacher_id = 2;
        """
    

    sql_list = [sql_expression_01, 
                sql_expression_02, 
                sql_expression_03, 
                sql_expression_04, 
                sql_expression_05, 
                sql_expression_06, 
                sql_expression_07, 
                sql_expression_08, 
                sql_expression_09, 
                sql_expression_10]


    try:
        with create_connection() as conn:
            if conn is not None:
                c = conn.cursor()
                try:
                    for sql_script in sql_list:
                        c.execute(sql_script)
                        result = c.fetchall()
                        print(result)
                except DatabaseError as e:
                    logging.error(e)
                finally:
                    c.close()
            else:
                print("Error! cannot create the database connection.")
    except RuntimeError as err:
        logging.error(err)