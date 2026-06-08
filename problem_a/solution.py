import sys

def false():
    print('no')
    sys.exit()


#if len(sys.argv) != 2:
#    false()

input = input().strip()


suffix = '@odoo.com'


if len(input) > (len(suffix) + 4) or len(input) < (len(suffix) + 2):
    false()

elif not(input.endswith(suffix)):
    false()

username = input[:-len(suffix)]
if username.isalpha() and username.islower():
    print('yes')
else:
    false()
