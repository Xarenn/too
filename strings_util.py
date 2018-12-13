import string
import subprocess

def get_strings_from_file(file_name):
    print (subprocess.check_output(['strings', file_name]))

def get_strings_from_file_grep(file_name, grep):
    cmd = "strings " + file_name + " | grep " + grep
    print (subprocess.check_output(cmd, shell=True))

