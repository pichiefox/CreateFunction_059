def convertsTemperature(value, unit):
    if unit.upper() == "C":
        return (value * 9/5) + 32
    elif unit.upper() == "F":
        return (value - 32) * 5/9
    else :
        print("Unit Harus 'C' atau 'F'")

input_suhu = float(input("Masukkan nilai suhu: "))


   