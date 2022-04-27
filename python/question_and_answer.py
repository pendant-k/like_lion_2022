# 이상형이 뭐에요?

# questions, answers 저장하는 list 선언
questions = []
answers = []
result = {}
q_count = 1

# 구분선
div = "========================================================="

# 질문 받기
while 1:
    question = input(f"{q_count}번째 질문을 입력해주세요 (q를 눌러 질문 종료) : ")
    if question == "q":
        break
    else:
        result[question] = ""
        q_count += 1

print(div)
print('답변을 시작합니다')

# 질문에 대한 응답 받기 (순서대로)
for x in result:
    answer = input(x + ":   ")
    result[x] = answer

# 결과 출력하기
print(div)
print("결과값")
print(result)
