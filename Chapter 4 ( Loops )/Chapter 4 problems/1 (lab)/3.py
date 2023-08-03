Celsius=0
while Celsius<=100:
    Fahrenheit=9/5*Celsius+32
    Kelvin=Celsius+273.15
    Rankine=1.8*Kelvin
    print('The Celsius value =',Celsius ,'is equivalent to : ')
    print(Fahrenheit,'in Fahrenheit')
    print(Kelvin,'in Kelvin')
    print(format(Rankine,'.1f'),'in Rankine')
    Celsius=Celsius+5