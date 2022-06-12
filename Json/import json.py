import json
import pymysql

student = "student.json"
transcript = "transcript.json"
employee = "employee.json"
department = "department.json"


json_student = open(student).read()
json_obj_student = json.loads(json_student)

json_transcript = open(transcript).read()
json_obj_transcript = json.loads(json_transcript)

json_employee = open(employee).read()
json_obj_employee = json.loads(json_employee)

json_department = open(department).read()
json_obj_department = json.loads(json_department)

# do validation and checks before insert
def validate_string(val):
   if val != None:
        if type(val) is int:
            return str(val).encode('utf-8')
        else:
            return val


# connect to MySQL
print("Connecting ...")
con = pymysql.connect(host="localhost", port=3306, user="root",password="Boyka_2022",db="db1")
cursor = con.cursor()



# parse json data to SQL insert
print("Creating student ...")
cursor.execute("TRUNCATE student")
for i, item in enumerate(json_obj_student):
    ssn = validate_string(item.get("ssn"))
    name = validate_string(item.get("name"))
    major = validate_string(item.get("major"))
    status = validate_string(item.get("status"))

    cursor.execute("INSERT INTO student (ssn, name, major, status) VALUES (%s, %s, %s, %s)", (ssn, name, major, status))
    con.commit()


# parse json data to SQL insert
print("Creating transcript ...")
cursor.execute("TRUNCATE transcript")
for i, item in enumerate(json_obj_transcript):
    dcode = validate_string(item.get("dcode"))
    cno = validate_string(item.get("cno"))
    ssn = validate_string(item.get("ssn"))
    grade = validate_string(item.get("grade"))

    cursor.execute("INSERT INTO transcript (dcode, cno, ssn, grade) VALUES (%s, %s, %s, %s)", (dcode, cno, ssn, grade))
    con.commit()


# parse json data to SQL insert
print("Creating employee ...")
cursor.execute("TRUNCATE employee")
for i, item in enumerate(json_obj_employee):
    employeeID = validate_string(item.get("employeeID"))
    employeeName = validate_string(item.get("employeeName"))
    departmentID = validate_string(item.get("departmentID"))
    salary = validate_string(item.get("salary"))

    cursor.execute("INSERT INTO employee (employeeID, employeeName, departmentID, salary) VALUES (%s, %s, %s, %s)", (employeeID, employeeName, departmentID, salary))
    con.commit()


# parse json data to SQL insert
print("Creating department ...")
cursor.execute("TRUNCATE department")
for i, item in enumerate(json_obj_department):
    departmentID = validate_string(item.get("departmentID"))
    departmentName = validate_string(item.get("departmentName"))

    cursor.execute("INSERT INTO department (departmentID, departmentName) VALUES (%s, %s)", (departmentID, departmentName))
    con.commit()


con.close()
print("Disonnecting ...")