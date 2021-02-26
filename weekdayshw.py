weekdays=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
x=input()
for days in weekdays:
    if x==days[0]:
        print(days)

    else:
        li=[days]
        if li.count == 0:
            print("No day start with "+x)