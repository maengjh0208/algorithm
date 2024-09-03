def solution(seoul: list):
    # 리스트의 index 함수 : 해당 원소가 없으면 에러 발생
    return f"김서방은 {seoul.index('Kim')}에 있다"


result = solution(["Jane", "Kim"])
print(result)
print(result == "김서방은 1에 있다")
