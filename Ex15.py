def level(grade):
    if grade >= 90:
        return 'A'
    elif grade >= 60:
        return 'B'
    else:
        return 'C'
print(level(50))
print(level(80))