users = []
with open('tickets', 'r') as f:
    for line in f:
        users.append(line)
f.close()


f = open('tickets', 'w')
if len(users) > 1:
    for i in range(1, len(users)):
        f.write('%s' % users[i])
    f.close()
else:
    f.write('')
    f.close()


text = '@' + users[0].split(',')[1].replace('\n', '')
text += " est le prochain. Vous pouvez suivre la file d'attente en tapant la `/tickets`"

msg['payload'] = '{"response_type": "in_channel", "text": "%s"}' % text;

return msg
