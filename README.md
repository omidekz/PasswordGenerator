# PasswordGenerator
a python script to generate strong password

```bash

python3 psg.py
output: a password with len: [12, 32]

python3 psg.py --len 20
output: a password with len: 20

python3 psg.py --min 20
output: a password with len: [20, 32]

python3 psg.py --max 20
output: a password with len: [12, 20]

python3 psg.py --min 14 --max 40
output: a password with len: [14, 40]

python3 psg.py --min 30 --max 40 -len 12 # in  a crazy manner :)
output: a password with len: 12

```
# Password contain
  * lowercase letters
  * uppercase letters
  * numbers
  * symbols: ```['@', '#', '&', '!', '$', '%', '^', '*', '(', ')', '-', '?', '.', ',', ';', ':', '[', ']', '{', '}',
                  '/',
                  '\\', '`', '~', '+', '=']```
