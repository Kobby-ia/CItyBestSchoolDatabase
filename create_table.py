import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="israelaidoo",
        password="Kobbie@2025.",
        database="PROJECT_TUTORIAL"
    )

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE students (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(100),
            age INT,
            grade VARCHAR(10),
            email VARCHAR(100)
        )
    """)

    print("Table 'students' created successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():

        cursor.close()
        connection.close()

import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="israelaidoo",
        password="Kobbie@2025.",
        database="PROJECT_TUTORIAL"
    )

    cursor = connection.cursor()

    # Insert sample data into students table
    cursor.execute("""
        INSERT INTO students (name, age, grade, email)
        VALUES
        ('John Doe', 20, 'A', 'johndoe@example.com'),
        ('Jane Smith', 22, 'B', 'janesmith@example.com')
    """)

    # Insert sample data into courses table
    cursor.execute("""
        INSERT INTO courses (name, description)
        VALUES
        ('Mathematics', 'An introductory course to Mathematics'),
        ('Physics', 'An advanced course in Physics')
    """)

    # Insert sample data into teachers table
    cursor.execute("""
        INSERT INTO teachers (name, subject, email)
        VALUES
        ('Dr. James', 'Mathematics', 'drjames@example.com'),
        ('Prof. Sarah', 'Physics', 'profsarah@example.com')
    """)

    connection.commit()
    print("Sample data inserted successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
