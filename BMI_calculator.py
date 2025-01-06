#Body Mass Index
#formula: height in  meters squared(height*2) divided by weight in kgs = (1.74m*1.74m)/70. meters and kgs
import bmi_categories
import logging
logger= logging.getLogger(__name__)
error_file= logging.FileHandler('bmi.log')
error_file.setLevel(logging.WARNING)
formatting= logging.Formatter('%(levelname)s: %(name)s: %(message)s')
error_file.setFormatter(formatting)
logger.addHandler(error_file)

try:
    def weight_conversion():
        weight_unit = str(input('Weight unit. kgs/lbs: '))
        weight = float(input('Enter your weight: ')) #conversion in the if statement. kgs= wieght/0.45 lbs=weight/*0.45. be specific eg 65 kgs

        if weight_unit == 'kgs':
            return weight
        elif weight_unit == 'lbs': #converting to kilograms
            return weight*0.45

    def height_conversion():  
        height_unit = str(input('Height unit. m/cm: '))
        height = float(input('Enter your height: ')) #conversion in the if statement. be specific eg 174 cm

        if height_unit == 'cm': #converting centimeters to meters
            return height/100
        elif height_unit == 'm':
            return height 

    bmi_range = weight_conversion() / (height_conversion()**2)

    if bmi_range < 18.5:
        print(f'You\'re BMI is {bmi_range:.2f}. You\'re in the underweight range.') #use the f string to intergrate variables inside of strings. better cause it automatically converts intergers/floats into strings.
        print(bmi_categories.bmi_weights[0])
    elif bmi_range >= 18.5 and bmi_range <=24.9:
        print(f'You\'re BMI is {bmi_range:.2f}. You\'re in the healthy weight range.')
    elif bmi_range >=25 and  bmi_range <=29.9:
        print(f'You\'re BMI is {bmi_range:.2f}. You\'re in the overweight range.')
        print(bmi_categories.bmi_weights[1])
    elif bmi_range >=30:
        print(f'You\'re BMI is {bmi_range:.2f}. You\'re in the obese range.')
        print(bmi_categories.bmi_weights[2])
except:
    logger.exception('Error')
