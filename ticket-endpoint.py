users = []
with open('tickets', 'r') as f:
    for line in f:
        users.append(line)
f.close()

user = msg['user_id'] + ',' + msg['user_name'] + '\n'
if user not in users:
    users.append(user)
    f = open('tickets', 'w')
    for user in users:
        f.write('%s' % user)
    f.close()

text = "Vous displosez du ticket n°";
text += str(len(users));

msg['payload'] = '{"response_type": "ephemeral", "text": "%s"}' % text;

return msg
