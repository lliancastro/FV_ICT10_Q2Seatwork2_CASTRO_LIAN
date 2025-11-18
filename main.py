from pyscript import display 

def general_weighted_average(e):

First name: = float(document.getElementById('First name:').value)
Last name: = float(document.getElementById('Last name:').value)

Science: = float(document.getElementById('Science:').value)
English: = float(document.getElementById('English:').value)
Math: = float(document.getElementById('Math:').value)
Filipino: = float(document.getElementById('Filipino:').value)
ICT: = float(document.getElementById('ICT:').value)
PE: = float(document.getElementById('PE:').value)


weighthed_sum = (science*5 + english *5 + math*5 +filipino*3+ ict*2 +pe *1)
total_units = (5*3)+3+2+1
gwa = weighted_sum / total_units


summary = f " " " {subjects[0]}: {science:.95}

{subjects[1]}: {math:.88}
{subjects[2]}: {english:.95}
{subjects[3]}: {filipino:.93}
{subjects[4]}: {ict:.90}
{subjects[5]}: {pe:.97}
" " "
display(f'Name:{first_name}{last_name}', target="student_info")
display(summary, target='summary')
display(f'Your general weighted average is {gwa:.2f}', target='output')
