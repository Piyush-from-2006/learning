'''Write a script in Python to copy the first 20 characters from an existing file
"SMS.TXT" into a new file "T20.TXT"'''
sms_file = "SMS.TXT"
t20_file = "T20.TXT"
with open(sms_file, 'r') as sms_file_handle:
    sms_content = sms_file_handle.read(20)
with open(t20_file, 'w') as t20_file_handle:
    t20_file_handle.write(sms_content)
print('20 characters copied from', sms_file, 'to', t20_file)
