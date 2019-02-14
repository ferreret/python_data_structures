# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

senders = dict()

for line in handle:
    if not line.startswith("From "): continue
    words = line.split()
    if len(words) < 2: continue
    sender = words[1]
    senders[sender] = senders.get(sender, 0) + 1

most_sender = None
max_mails = None

for name_sender, number_send in senders.items():
    if max_mails is None or number_send > max_mails:        
        most_sender  = name_sender
        max_mails = number_send

print(most_sender, max_mails)


