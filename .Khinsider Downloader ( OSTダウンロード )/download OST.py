import os
class bcolors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    LINE = '\033[90m'
    ENDC = '\033[0m'
print(f"{bcolors.OKBLUE}Enter the link of the {bcolors.WARNING}Khinsider OST{bcolors.OKBLUE} you would like to download...{bcolors.ENDC}")
print(f"{bcolors.LINE}---------------------------------------")
link = input(f"{bcolors.WARNING}Link {bcolors.ENDC}> {bcolors.WARNING}")
print(f"{bcolors.LINE}---------------------------------------{bcolors.WARNING}")
print(f"{bcolors.OKBLUE}Enter the {bcolors.WARNING}format of the audio{bcolors.OKBLUE} (must be available on the site)...{bcolors.ENDC}")
print(f"{bcolors.LINE}---------------------------------------")
audioFormat = input(f"{bcolors.WARNING}Format {bcolors.ENDC}> {bcolors.WARNING}")
print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
print(f"{bcolors.OKBLUE}Now downloading...")
print(f"{bcolors.LINE}---------------------------------------{bcolors.ENDC}")
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
command = "kh.py --format " + audioFormat + " " + link
os.system(command)
