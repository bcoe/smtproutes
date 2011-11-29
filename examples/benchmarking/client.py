import smtplib, time

messages_sent = 0.0
start_time = time.time()
msg = file('test/fixtures/valid_dkim.eml').read()

while True:
    
    if (messages_sent % 10) == 0:
        current_time = time.time()
        print '%s msg-written/sec' % (messages_sent / (current_time - start_time))
    
    server = smtplib.SMTP('localhost', port=25)
    server.sendmail('foo@localhost', ['bar@localhost'], msg)
    server.quit()
    
    messages_sent += 1.0