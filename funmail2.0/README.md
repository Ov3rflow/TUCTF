Funmail2.0 is the second RE challenge for TUCTF.

"john galt is having some problems with his email again. But this time it's not his fault. Can you help him?

funmail2.0 - md5: badb9b50dce8539a142c851b9c2c9165"

Doing strings will yet again reveal john galts password.

![Alt text](./Screenshots/Funmail2_password.png?raw=true "Password")

However this time the program errors out and closes..

![Alt text](./Screenshots/funmail2_login_error.png?raw=true "Not really an error")

Investigating the main function in hopper reveals that the program isnt erroring at all.
There are in fact only 2 paths it can take.
1. incorrect username/password try again
2. correct login credentials, print "error" and close the program

![Alt text](./Screenshots/funmail2_deadend.png?raw=true "Dead end in main")


However hopper does show us that the functions to show and print emails do exist. The main function just has no way to call the email functions.

![Alt text](./Screenshots/funmail2.0_showemails.png?raw=true "Hopper Functions")

Knowing these details it is a simple matter to fire up GDB and find the address that the "showEmails" function is loaded into.

![Alt text](./Screenshots/funmail2_gdb_show_emails.png?raw=true "GDB showEmails memory address")

Then we can simply change EIP to point to that function and let the program run to receive our flag!

![Alt text](./Screenshots/funmail2_flag.png?raw=true "Flag!")
