import random
import time
# 이론 정리

# list : 명확한 순서가 존재한다


# dictionary
# information = {"취미": "코딩", "고향": "경주", "이름": "김동한"}
# for x, y in information.items():
#     print(x, y)

# set : 순서가 따로 없다 / 순서대로 접근할 수가 없다 / 중복이 불가능함

# foods = ["된장찌개", "피자", "제육볶음", "된장찌개"]
# foods_set = set(foods)
# print(foods)
# print(foods_set)

# menu1 = set(["된장찌개", "피자", "제육볶음"])
# menu2 = set(["된장찌개", "떡국", "김밥"])
# menu3 = menu1 & menu2
# print(menu3)
# menu3 = menu1 - menu2
# print(menu3)


# condition
# food = random.choice(["된장찌개", "피자", "제육볶음"])

# print(food)
# if(food == "제육볶음"):
#     print("곱빼기 주세요.")
# else:
#     print("그냥 주세요.")
# print("종료")


# 초기 점심 메뉴 리스트
lunch = ["된장찌개", "피자", "제육볶음", "짜장면"]


def print_food(lunch):
    print(lunch, "중에서 점심이 결정됩니다.")
    for i in range(5):
        print(5-i)
        time.sleep(1)
    print(f'오늘의 점심은 {random.choice(lunch)}입니다.')


# main
while 1:
    set_lunch = set(lunch)
    print(set_lunch)
    item = input("음식을 추가해주세요 (q를 눌러 종료해주세요)  :  ")
    if(item == "q"):
        while 1:
            print(set_lunch)
            item = input("삭제할 음식을 입력해주세요 (q를 눌러 종료해주세요) : ")
            if(item == "q"):
                print_food(list(set_lunch))
                break
            else:
                set_lunch = set_lunch - set([item])
        break
    else:
        lunch.append(item)
