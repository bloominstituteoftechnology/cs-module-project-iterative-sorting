def timeConversion(s):
    #find last 3 characters
    #if it is PM, add 12 to the first two characters
    #remove pm
    #if it is AM, remove am
    s_list = list(s)
    amPm = s_list[-2:]
    time = s_list[:-2]
    begin = 'The time is'
    end = 'in Beijing'
    print(time)
    if amPm == ['P','M'] and time[:2] != ['1','2']:
        two = time[:2] 
        twoInt = int(two[0] + two[1])
        twoInt = twoInt + 12
        return str(twoInt) + ''.join(time[2:])
    elif amPm == ['P','M'] and time[:2] == ['1','2']:
        return ''.join(time)
    elif amPm == ['A', 'M'] and time[:2] != ['1','2']:
        return begin + ' ' + ''.join(time)+ ' ' + end
    elif amPm == ['A', 'M'] and time[:2] == ['1','2']:
        #return 'io {:^10}'.format('test')
        return '{} 00{} {}'.format('Wake up, it is', ''.join(time[2:]), 'in the morning')



    
s = '12:05:45AM'
print(timeConversion(s))
