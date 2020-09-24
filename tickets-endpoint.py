users = []
with open('tickets', 'r') as f:
    for line in f:
        users.append(line)
f.close()

text = "---\\n### File d'attente\\n";
text += "| Position | Utilisateur |\\n";
text += "|:---------|:-----------:|\\n";

i = 1
for user in users:
    text+= '|'
    text+= str(i)
    text+= '| @'
    text+= user.split(',')[1].replace('\n', '')
    text+= '|\\n'
    i+=1

msg['payload'] = '{"response_type": "in_channel", "text": "' + text + '"}';

return msg
