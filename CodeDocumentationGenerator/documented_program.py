
def calculate_average(marks):
    """
    Calculate the arithmetic mean of a list of marks.

    Args:
        marks (list): A list of numeric marks.

    Returns:
        float: The average of the marks.

    Raises:
        ZeroDivisionError: If the list is empty.
    """
    total = sum(marks)
    return total / len(marks)


def check_result(average):
    """
    Determine whether a student passes.

    Args:
        average (float): The student's average marks.

    Returns:
        str: 'Pass' if average is at least 40, otherwise 'Fail'.
    """
    if average >= 40:
        return "Pass"
    return "Fail"


marks = [75, 80, 65, 90, 70]
average = calculate_average(marks)
result = check_result(average)

print("Marks:", marks)
print("Average:", average)
print("Result:", result)
