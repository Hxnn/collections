Days = ['Maandag', 'Dinsdag', 'Woensdag', 'Donderdag', 'Vrijdag', 'Zaterdag', 'Zondag']
Days1 = (input('Welke dag van de week wilt u kiezen? Kies uit:\nAlles/Werkdagen/Weekendd/AllesOm/WerkdagenOm/WeekendOm '))
if Days1 == 'Alles':
    print(Days[0:7])
elif Days1 == 'Werkdagen':
    print(Days[0:5])
elif Days1 == 'Weekend':
    print(Days[5:7])
elif Days1 == 'AllesOm':
    Days.reverse()
    print(Days[0:7])
elif Days1 == 'WerkdagenOm':
    Days.reverse()
    print(Days[2:7])
else:
    Days.reverse()
    print(Days[0:2])
