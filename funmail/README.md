Funmail is the first RE challenge for TUCTF.

"One of our employees has locked himself out of his account. can you help 'john galt' recover his password? And no snooping around his emails you hear.

funmail - md5: 2462f28c6d64be1dc5658dc5f7bc06b9"

So we have a binary and we know the user is john galt.
First thing is first, strings the binary..

![Alt text](./Screenshots/strings.png?raw=true "Strings!")

..snip..

![Alt text](./Screenshots/password.png?raw=true "Oops")


Well that was easy.
Now just login with the username and password..

![Alt text](./Screenshots/login.png?raw=true "Login")


And read Johns emails to receive the first RE flag!

![Alt text](./Screenshots/flag.png?raw=true "Flag")
