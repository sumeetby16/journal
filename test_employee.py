from employee import get_employee_details

def test_get_employee_details():
    result = get_employee_details("Sakshi", "E101", "IT", 50000)

    expected_output = (
        "Employee Name: Sakshi\n"
        "Employee ID: E101\n"
        "Department: IT\n"
        "Salary: 50000"
    )

    assert result == expected_output
