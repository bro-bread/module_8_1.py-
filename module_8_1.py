def add_everything_up(a,b):
    try:
        ab = a + b
        print(ab)
    except TypeError as err:
        print(f"{str(a)+ str(b)}")
    else:
        print(f"ВСЁ ПРОШЛО УСПЕШНО!!!")
    finally:
        g =  " "
        print("конец")
        return g

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
