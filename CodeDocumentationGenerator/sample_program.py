
def calculate_average(marks):
    total = sum(marks)
    return total / len(marks)


def check_result(average):
    if average >= 40:
        return "Pass"
    else:
        return "Fail"


marks = [75, 80, 65, 90, 70]

average = calculate_average(marks)
result = check_result(average)

print("Marks:", marks)
print("Average:", average)
print("Result:", result)
