print ('👋 Hi there i am you assisstant to start the bmi calculation just type the needed objects. \n ')

name = input ('👨‍💻 what is your name? \n ')
weight = int (input ('👨‍💻 what is your weight? \n '))
age = int (input ('👨‍💻 how old are you? \n '))
height = float (input ('👨‍💻 how tall are you? (based on meter!!!) \n '))

print ('🧠 calculating on progress... \n ')

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

print ('👋 Hi ', name, 'you are ', age, 'years old \n your BIM is: ', bmi_calculation,'your weight: ', weight, 'your height: ', height )
