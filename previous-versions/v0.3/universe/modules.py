from sys import executable
from subprocess import check_call

# implement pip as a subprocess:
check_call([executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])