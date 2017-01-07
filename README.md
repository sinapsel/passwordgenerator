# passwordgenerator
### ABOUT:
Password generator helps you to generate a random password in 5 different security levels
### USING:
Passgen could be run without any parameters. Script will ask you pass length and then you'll get your output like 
<pre>Pass length:    8
         Numbers only
91340218
         Chars in low case only
ymmtyrxq
         Numbers and low case chars
d843e4u8
         Numbers and chars
WBdgJW96
         All ASCII
4t"#2@&T</pre>

First parameter is password length, second parameter is a number of times random pass would be generated, third one is an output file

Example:

<pre>
Username@Machine:~$ passgen 8 2 pass.txt
8 chars random passwords
for 2 times
writing in pass.txt file
         Numbers only
22169292
65533843
         Chars in low case only
xmwdjhcc
kaxpvbjc
         Numbers and low case chars
5yo47agl
wsa0n14n
         Numbers and chars
5vefCr4d
8QBr6Noi
         All ASCII
PHVp:>r:
D4z)RvBs
</pre>
Pass.txt is:
<pre>
Username@Machine:~$ cat pass.txt
22169292
65533843
xmwdjhcc
kaxpvbjc
5yo47agl
wsa0n14n
5vefCr4d
8QBr6Noi
PHVp:>r:
D4z)RvBs
</pre>

### INSTALLATION:
To make passgen executable file unlinked to directory you need to install it with <pre>sh install.sh</pre> command in cloned from github dir
