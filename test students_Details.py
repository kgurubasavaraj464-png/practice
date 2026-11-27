from student import student_details

def test_student_name():
    s = student_details("Basanagouda", "01FE25BCA145",
                        "KLE Technological University", "Hubli")
    assert s["name"] == "Basanagouda"

def test_student_usn():
    s = student_details("Basanagouda", "01FE25BCA145",
                        "KLE Technological University", "Hubli")
    assert s["usn"] == "01FE25BCA145"

def test_college_name():
    s = student_details("Basanagouda", "01FE25BCA145",
                        "KLE Technological University", "Hubli")
    assert s["college"] == "KLE Technological University"

def test_student_city():
    s = student_details("Basanagouda", "01FE25BCA145",
                        "KLE Technological University", "Hubli")
    assert s["city"] == "Hubli"