students = [
    {"name": "小明", "score": 90},
    {"name": "小红", "score": 85},
    {"name": "小刚", "score": 77},
]

def top_student(students):
    best = students[0]
    for s in students:
        if s["score"] > best["score"]:
            best = s
    return best

print(top_student(students))