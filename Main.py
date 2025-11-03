import sqlite3

# Connect to database (auto-create if not exists)
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER,
    course TEXT,
    city TEXT
)
""")
conn.commit()

# Function to add student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")
    city = input("Enter city: ")
    cursor.execute("INSERT INTO students (name, age, course, city) VALUES (?, ?, ?, ?)", (name, age, course, city))
    conn.commit()
    print("✅ Student added successfully!\n")

# Function to view all students
def view_students():
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    if rows:
        print("\n--- Student Records ---")
        for row in rows:
            print(f"ID: {row[0]} | Name: {row[1]} | Age: {row[2]} | Course: {row[3]} | City: {row[4]}")
        print()
    else:
        print("No records found.\n")

# Function to update student
def update_student():
    view_students()
    student_id = input("Enter student ID to update: ")
    new_name = input("Enter new name: ")
    new_age = input("Enter new age: ")
    new_course = input("Enter new course: ")
    new_city = input("Enter new city: ")
    cursor.execute("UPDATE students SET name=?, age=?, course=?, city=? WHERE id=?", 
                   (new_name, new_age, new_course, new_city, student_id))
    conn.commit()
    print("✅ Student updated successfully!\n")

# Function to delete student
def delete_student():
    view_students()
    student_id = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=?", (student_id,))
    conn.commit()
    print("🗑️ Student deleted successfully!\n")

# Menu
def main():
    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
