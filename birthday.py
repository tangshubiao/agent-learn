# 输入生日，算出今年多少岁、今年已经过了多少天
from datetime import date


def main():
    birthday_text = input("请输入你的生日（格式：1998-05-20）：")
    year, month, day = (int(part) for part in birthday_text.split("-"))
    birthday = date(year, month, day)

    today = date.today()

    age = today.year - birthday.year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age -= 1

    days_passed = (today - date(today.year, 1, 1)).days + 1

    print(f"你今年 {age} 岁")
    print(f"今年已经过了 {days_passed} 天")


if __name__ == "__main__":
    main()
