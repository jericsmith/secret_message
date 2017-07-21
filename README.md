# secret_message
python package.  a fun program to scramble an alpha and space only message using images of letters. 

Unless you want to add a fix to strip punctuation and other non alpha characters or an enhancement to accept 
them, use the happy path for now.

This is a silly, but fun little python package.  I'm sure you know some non techie who will get a kick out of it.

Currently, in the asset folder are individual png images of the English alphabet, along with a blank square to 
represent word breaks, or spaces as I like to call them.

In order for this to work as-is, you will need leave the assets in the existing root folder.

```
-> import secret_message
-> secret_message.message_scrambler.scramble_message('Pokemon is not a Japanese word', 'c:\secret\scrambled')
```

![alt text:](https://github.com/jericsmith/secret_message/blob/master/scrambled_sample.png "Scrambled letter images of our secret message")

```
-> import secret_message
-> secret_message.message_descrambler.descramble_message('c:\secret\scrambled')
```

![alt text:](https://github.com/jericsmith/secret_message/blob/master/descrambled_sample.png "Scrambled letter images of our secret message")


