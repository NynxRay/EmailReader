"""A collection of function for doing my project."""

def read_email_as_Strings(username,password):
    # EXTERNAL CODE
    # imap library which enables us to read emails from our inbox. It will loop through all the emails and put the body of email in a list
    import imaplib
    import email
    import os
    # Create TEXT folder to store messages
    if not os.path.exists('text'):
        os.mkdir('text')
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    # imaplib module implements connection based on IMAPv4 protocol
    mail.login(username, password)
    # >> ('OK', [username at gmail.com Vineet authenticated (Success)'])

    mail.list() # Lists all labels in GMail
    mail.select('inbox') # Connected to inbox.
    
    result, data = mail.uid('search', None, "ALL")
    # search and return uids instead
    i = len(data[0].split()) # data[0] is a space separate string
    for x in range(i):
        latest_email_uid = data[0].split()[x] # unique ids wrt label selected
        result, email_data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        # fetch the email body (RFC822) for the given ID
        raw_email = email_data[0][1]
        #continue inside the same for loop as above
        raw_email_string = raw_email.decode('utf-8')
        # converts byte literal to string removing b''
        email_message = email.message_from_string(raw_email_string)
        # this will loop through all the available multiparts in mail
        for part in email_message.walk():
            if part.get_content_type() == "text/plain": # ignore attachments/html
                body = part.get_payload(decode=True)
                if os.path.isfile("text/message_" + str(x) + ".txt"):
                    print('Already load the email Number'+str(x))
                else:
                    save_string = str("text/message_" + str(x) + ".txt")  
                    # location on disk
                    myfile = open(save_string, 'a')
                    final_text = body.decode('utf-8')
                    myfile.write(final_text)
                    # body is again a byte literal
                    myfile.close()
            else:
                  continue
    print('Email Load success')
def encryption(start_key,key_increment,message):
    #CLASE CODE
    encoded = ''
    key = start_key

    for char in message:
        unicode = ord(char)
        new_unicode = unicode + key
        new_char = chr(new_unicode)
        encoded = encoded+new_char
        key = key + key_increment
        
    return encoded
def decryption(start_key,key_increment,encoded):
    #CLASS CODE
    # Knowing the start key, and the length of the message, we can reconstruct the current key
    key = start_key + (len(encoded) * key_increment)

    decoded = ''

    # Note that this decodes the message backwards, stepping back along key values
    for char in encoded[::-1]:

        # Step the key back one step, and apply to current character
        key = key - key_increment
        decoded = decoded + chr(ord(char) - key)

    # Having decoded backwards, flip the message back around
    decoded = decoded[::-1]
    
    return decoded
    
