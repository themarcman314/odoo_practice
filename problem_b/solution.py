import sys

def process_line(line:str):
    model = 'ODOO'
    num_changes = 0
    linesize = len(line)
    print(line)
    if linesize == 4:
        for i, char in enumerate(line):
            if char != model[i]:
                num_changes += 1
        print(num_changes)
    else: #linesize > 4
        assert(linesize > 4)



def check_line(line:str)->bool:
    model = 'ODOO'
    for i,char in enumerate(line):
        if char != model[i]:
            return False
    return True;


input = ''

for line in sys.stdin:
    input += line

inputlines = input.splitlines()

num_cases = int(inputlines[0])

for i in range(1, num_cases+1):
    line = inputlines[i]
    process_line(line)

