def solution(phone_number):
    return "*" * (len(phone_number) - 4) + phone_number[-4:]


result = solution("01033334444")
print(result)
print(result == "*******4444")
