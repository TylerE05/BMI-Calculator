def calc_BMI(weight,height):
    return (weight / (height ** 2)) * 703

def BMI_Cat(BMI):

    if BMI < 16:
        return 'Severe Thin'
    elif 16 <= BMI < 17:
        return 'Moderate Thin'
    elif 17 <= BMI < 18.5:
        return 'Mild Thinness'
    elif 18.5 <= BMI < 25:
        return 'Normal'
    elif 25 <= BMI < 30:
        return 'Overweight'
    elif 30 <= BMI < 35:
        return 'Obese I'
    elif 35 <= BMI < 40:
        return 'Obese II'
    else:
        return 'Obese III'

def main():
    while True:
        weight = float(input("Enter your weight in lbs: "))
        height = float(input("Enter your height in inches: "))

        bmi = calc_BMI(weight,height)
        category = BMI_Cat(bmi)

        print(f"Your BMI is {bmi:.2f}. You are considered {category}.")
        break
main()