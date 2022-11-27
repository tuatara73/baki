import subprocess, sys

subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirments.txt'])
reqs = subprocess.check_output([sys.executable, '-m', 'pip',
'freeze'])
installed_packages = [r.decode().split('==')[0] for r in reqs.split()]
print(installed_packages)