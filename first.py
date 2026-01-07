import random

def challenge_guess_the_number():
    """도전! 숫자 맞추기 게임 (횟수 제한 및 점수)"""
    print("\n--- 도전! 숫자 맞추기 게임 ---")
    
    while True:
        try:
            max_attempts = int(input("몇 번 안에 맞추시겠어요? (예: 10): "))
            if max_attempts > 0:
                break
            else:
                print("1 이상의 숫자를 입력해주세요.")
        except ValueError:
            print("숫자만 입력할 수 있어요.")

    computer_number = random.randint(1, 1000)
    print(f"\n좋아요! 1부터 1000 사이의 숫자를 {max_attempts}번 안에 맞춰보세요!")

    for attempt_count in range(1, max_attempts + 1):
        try:
            print(f"\n[ {attempt_count}번째 시도 / 남은 횟수: {max_attempts - attempt_count + 1} ]")
            user_guess = int(input("숫자를 입력하세요: "))

            if user_guess < computer_number:
                print("더 큰 숫자입니다!")
            elif user_guess > computer_number:
                print("더 작은 숫자입니다!")
            else:
                remaining_attempts = max_attempts - attempt_count
                score = (remaining_attempts + 1) * 10
                print(f"\n🎉 정답입니다! {attempt_count}번 만에 맞추셨어요! 획득 점수: {score}점")
                return
        except ValueError:
            print("유효한 숫자를 입력해주세요. (시도 횟수는 차감됩니다)")

    print(f"\n아쉽지만 모든 기회를 사용했습니다. 정답은 {computer_number}였습니다.")


challenge_guess_the_number()


def print_shiny_crystal():
    """조금 더 장식된 크리스탈 모양을 출력하는 함수"""
    shiny_crystal_art = r"""
        '
       / \
      / _ \
     | / \ |
     | \_/ |
      \   /
       `.'
    """
    print(shiny_crystal_art)

# 함수를 호출하여 크리스탈 출력
# print_shiny_crystal()


def guess_the_1_to_100_number():
    """숫자 맞추기 게임 함수"""
    # 컴퓨터가 1부터 1000 사이의 임의의 숫자를 선택합니다.
    computer_number = random.randint(1, 1000)
    attempts = 0    # 변수(빈방), 초기화

    print("1부터 1000 사이의 숫자를 맞춰보세요!")

    while True:
        try:
            # 사용자로부터 추측을 입력받습니다.
            user_guess = int(input("숫자를 입력하세요: "))      # "23", 23
            attempts += 1   # attempts = attempts + 1, attempts++

            if user_guess < computer_number:
                print("더 큰 숫자입니다!")
            elif user_guess > computer_number:
                print("더 작은 숫자입니다!")
            else:
                print(f"축하합니다! {attempts}번 만에 숫자를 맞췄습니다.")
                break  # 정답을 맞췄으므로 반복문 종료
            
        except ValueError:
            print("유효한 숫자를 입력해주세요.")

            

# # 게임 시작
# guess_the_1_to_100_number()

# def add(x, y):
#     return x + y

# def subtract(x, y):
#     return x - y

# def multiply(x, y):
#     return x * y

# def divide(x, y):
#     if y == 0:
#         return "오류: 0으로 나눌 수 없습니다."
#     return x / y



def simple_calculator():
    """간단한 계산기 프로그램"""
    print("간단한 계산기입니다.")
    print("연산을 선택하세요:")
    print("1. 더하기")
    print("2. 빼기")
    print("3. 곱하기")
    print("4. 나누기")

    choice = input("선택(1/2/3/4): ")

    if choice not in ('1', '2', '3', '4'):
        print("잘못된 선택입니다.")
        return

    try:
        num1 = float(input("첫 번째 숫자를 입력하세요: "))
        num2 = float(input("두 번째 숫자를 입력하세요: "))
    except ValueError:
        print("숫자만 입력해주세요.")
        return

    if choice == '1':
        print(f"{num1} + {num2} = {add(num1, num2)}")
    elif choice == '2':
        print(f"{num1} - {num2} = {subtract(num1, num2)}")
    elif choice == '3':
        print(f"{num1} * {num2} = {multiply(num1, num2)}")
    elif choice == '4':
        print(f"{num1} / {num2} = {divide(num1, num2)}")

# 계산기 실행
# simple_calculator()

def todo_list_app():
    """콘솔 기반 투두리스트 애플리케이션"""
    tasks = [] # 할 일을 저장할 리스트

    while True:
        print("\n--- TO-DO LIST ---")
        print("1. 할 일 추가")
        print("2. 할 일 목록 보기")
        print("3. 할 일 삭제")
        print("4. 종료")

        choice = input("원하는 작업의 번호를 입력하세요: ")

        if choice == '1':
            task = input("추가할 할 일을 입력하세요: ").strip()
            if task:
                tasks.append(task)
                print(f"'{task}'가 추가되었습니다.")
            else:
                print("내용이 없습니다.")
        elif choice == '2':
            if not tasks:
                print("할 일이 없습니다.")
            else:
                print("\n[할 일 목록]")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
        elif choice == '3':
            if not tasks:
                print("삭제할 할 일이 없습니다.")
                continue
            try:
                del_num = int(input("삭제할 할 일의 번호를 입력하세요: "))
                if 1 <= del_num <= len(tasks):
                    removed_task = tasks.pop(del_num - 1)
                    print(f"'{removed_task}'가 삭제되었습니다.")
                else:
                    print("잘못된 번호입니다.")
            except ValueError:
                print("숫자를 입력해주세요.")
        elif choice == '4':
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 1-4 사이의 숫자를 입력하세요.")

# # 투두리스트 앱 실행
# todo_list_app()

import random

def rock_paper_scissors():
    """가위바위보 게임"""
    options = ["가위", "바위", "보"]
    computer_choice = random.choice(options)

    user_choice = input("가위, 바위, 보 중 하나를 내세요: ").strip()

    if user_choice not in options:
        print("잘못된 입력입니다. 가위, 바위, 보 중에서 선택해주세요.")
        return

    print(f"사용자: {user_choice}, 컴퓨터: {computer_choice}")

    if user_choice == computer_choice:
        print("비겼습니다!")
    elif (user_choice == "가위" and computer_choice == "보") or \
         (user_choice == "바위" and computer_choice == "가위") or \
         (user_choice == "보" and computer_choice == "바위"):
        print("사용자 승리!")
    else:
        print("컴퓨터 승리!")

# 게임 시작
# rock_paper_scissors()


def main():
    """모든 미니 프로젝트를 실행할 수 있는 메인 메뉴 함수"""
    
    # 시작 시 크리스탈 출력
    print_shiny_crystal()

    while True:
        print("\n======= 미니 프로젝트 모음 ========")
        print("1. 숫자 맞추기 게임")
        print("2. 간단한 계산기")
        print("3. 투두리스트")
        print("4. 가위바위보 게임")
        print("5. 종료")
        print("===================================")

        choice = input("실행할 프로그램 번호를 입력하세요: ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            simple_calculator()
        elif choice == '3':
            todo_list_app()
        elif choice == '4':
            rock_paper_scissors()
        elif choice == '5':
            print("프로그램을 종료합니다. 이용해주셔서 감사합니다.")
            break
        else:
            print("잘못된 번호입니다. 1-5 사이의 숫자를 입력해주세요.")

# 이 파일이 직접 실행될 때만 main() 함수를 호출합니다.
# if __name__ == "__main__":
#     main()

# import random

def print_cute_goodbye_1():
    """잘가라는 인사를 하는 말을 출력하는 함수"""
    cute_goodbye = r"""
    안녕~잘가~~   `
    """
    print(cute_goodbye)

# 함수를 호출하여 크리스탈 출력
# print_cute_goodbye_1()

def print_cute_goodbye_2():
    """'안녕~잘가~~' 메시지를 출력하는 함수"""
    message = "안녕~잘가~~"
    print(message)

# 이 파이썬 파일이 직접 실행되었을 때만 아래 코드를 동작시켜라! 라는 약속입니다.
# if __name__ == "__main__":
    # 위에서 만든 print_cute_goodbye 함수를 호출(실행)합니다.
    # print_cute_goodbye_2()


# import random

# # ======================================================================
# # 함수 정의 (Function Definitions)
# # ======================================================================

# def 일부터백까지더하기():
#     """1부터 100까지의 숫자를 더하는 함수"""
#     user_tap = 

import random
import string

def password_generator():
    """지정한 길이의 무작위 비밀번호를 생성하는 프로그램"""
    try:
        length = int(input("생성할 비밀번호의 길이를 입력하세요 (8 이상): "))
        if length < 8:
            print("보안을 위해 8자 이상의 길이를 권장합니다.")
            return

        # 비밀번호에 사용될 문자셋 정의
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # 무작위 문자 선택
        password_list = [random.choice(characters) for _ in range(length)]
        
        # 문자 순서 섞기
        random.shuffle(password_list)
        
        # 리스트를 문자열로 변환
        password = "".join(password_list)
        
        print(f"생성된 비밀번호: {password}")

    except ValueError:
        print("숫자만 입력해주세요.")

# 프로그램 실행
password_generator()

import time

def countdown_timer():
    """사용자가 지정한 시간(초)만큼 카운트다운하는 프로그램"""
    try:
        seconds = int(input("카운트다운 할 시간(초)을 입력하세요: "))
        if seconds <= 0:
            print("0보다 큰 숫자를 입력해주세요.")
            return

        print("카운트다운 시작!")
        for i in range(seconds, 0, -1):
            print(f"{i}...")
            time.sleep(1) # 1초 동안 프로그램 실행을 멈춤
        
        print("땡! 시간이 다 되었습니다!")

    except ValueError:
        print("숫자만 입력해주세요.")

# 프로그램 실행
countdown_timer()

import random

def roll_the_dice():
    """1부터 6까지의 숫자 중 하나를 무작위로 출력하는 주사위 프로그램"""
    print("주사위를 던집니다...")
    dice_number = random.randint(1, 6)
    print(f"나온 숫자: {dice_number}!")

# 프로그램 실행
roll_the_dice()

def personal_greeting():
    """사용자에게 이름을 물어보고 맞춤 인사를 건네는 프로그램"""
    name = input("안녕하세요! 이름이 무엇인가요? ")
    print(f"반가워요, {name}님! 오늘 하루도 즐겁게 보내세요!")

# 프로그램 실행
personal_greeting()

import time
import sys
import os

# ======================================================================
# 'random' 라이브러리를 대체하는 간단한 함수들
# ======================================================================

# 간단한 난수 생성을 위한 초기값(seed) 설정
_seed = int(time.time() * 1000)

def simple_rand_int(min_val, max_val):
    """단순한 의사 난수 정수 생성기 (Linear Congruential Generator)"""
    global _seed
    # LCG 공식: X_{n+1} = (a * X_n + c) % m
    a = 1664525
    c = 1013904223
    m = 2**32

    _seed = (a * _seed + c) % m

    # 결과를 원하는 범위 [min_val, max_val]로 조정
    range_size = max_val - min_val + 1
    return (_seed % range_size) + min_val

def simple_choice(sequence):
    """시퀀스(리스트 등)에서 임의의 요소를 선택하는 간단한 함수"""
    if not sequence:
        raise IndexError("빈 시퀀스에서는 선택할 수 없습니다")
    idx = simple_rand_int(0, len(sequence) - 1)
    return sequence[idx]

# ======================================================================
# 함수 정의 (Function Definitions)
# ======================================================================


