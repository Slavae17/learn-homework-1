print("Введите Ваш возраст")
age = int(input())

def main(age):
    if age < 7:
        return "Детский сад" 
    elif age >= 7 and age < 18:
        return "Школа"
    elif age >= 18 and age < 21:
        return "ВУЗ"
    else:
        return "Работать"

if __name__ == "__main__":
    print(main(age))
