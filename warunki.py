wiek = int(input("ile masz lat? "))

if wiek >= 65:
    print("jesteś osobą w wieku emerytalnym") 
elif wiek >= 18:
    print("jesteś osobą pełnoletnią")
else:
    print("jesteś osobą niepełnoletnią")