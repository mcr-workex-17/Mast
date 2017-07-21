open('last_build_data_log.json','w').close()
f1 = open('last_build_data_log.json','a')

length = sum(1 for line in open('slack.log'))

f1.write(str('[['))
for x in range(2,length - 5,4):
    f = open('slack.log')
    line = f.readlines()[x]
    f1.write(str('"' + line).rstrip('\n'))
    f1.write(str('",').rstrip('\n'))
    f.close()
f = open('slack.log')
line = f.readlines()[length -2]
f1.write(str('"' +line).rstrip('\n'))
f1.write(str('"'))
f1.write(str('], '))
f1.write("[")
f.close()
for x in range(2,length -4 ,4):
    g = open('slack.log')
    line = g.readlines()[x+1]
    f1.write(str('"' + line).rstrip('\n'))
    f1.write(str('",').rstrip('\n'))
    g.close()
f = open('slack.log')
line = f.readlines()[length -1]
f1.write(str('"' +line).rstrip('\n'))
f1.write(str('"'))
f1.write(str(']').rstrip(','))
f1.write(str(']'))
f1.close()
