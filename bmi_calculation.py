print ('👋 Hi there i am you assisstant to start the bmi calculation just type the needed objects.')

name = input ('👨‍💻 what is your name? ')
weight = int (input ('👨‍💻 what is your weight? '))
age = int (input ('👨‍💻 how old are you? '))
height = float (input ('👨‍💻 how tall are you? (based on meter!!!) '))

print ('🧠 calculating on progress...')

bmi_calculation = weight / (height ** 2)

if weight < 18.5:
    print ('⚰️ danger!!! gain weight ',name)
elif 18.5 < weight > 24.9:
    print ('✅ normal congrats', name)
elif 25 < weight > 29.9:
    print ('⁉️ over weighted!!! loose weight', name) 
elif 30 < weight > 34.9:
    print ('‼️ obse ver-1 ', name)
elif 35 < weight > 39.9:
    print ('‼️ obse ver-2 ', name)
else:
    print ('⚰️ DANGER OVER WEIGHT!!! ', name)

print ('👋 Hi ', name, 'you are ', age, 'years old and your BIM is: ', bmi_calculation,'your weight: ', weight, 'your height: ', height )
