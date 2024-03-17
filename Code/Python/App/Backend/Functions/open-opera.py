import subprocess


def run_opera_incognito(URL: str) -> None:
    """Open the specified URL in Opera private (incognito) mode."""


    #  Create a variable containing the command to run Opera in private mode.
    #  'f' prefix is for creating an f-string
    #  'r' prefix denotes a raw string literal (backslashes '\' are treated as literal characters and not as escape characters)
    #  having combined both the 'f' and 'r' prefixes we have the 'fr' prefix
    
    #  The string is made out of three components: (displayed in order)
    #  1. Path to the Opera browser executable file
    #  2. ' --private ' => an argument that launches Opera  in private browsing mode
    #  3. ' --remote {url} ' => an argument that specifies a URL to open in the browser

    cmd = fr'C:\Users\Olivier\AppData\Local\Programs\Opera\launcher.exe --private --remote {URL}'


    #  "subprocess.PIPE" as a value for < stdout= > or < stderr= > parameters in the < subprocess.Popen(...) > -- Python creates pipes for the corresponding streams.
    #  When you call < subprocess.Popen(...) > class to execute an external command -- Python spawns a new child process to run that command.
    #  If you've specified < stdout=subprocess.PIPE > -- the < stdout > of the child process is redirected to a pipe created by Python.
    #  This means that instead of printing output directly to the console -- the output produced by the child process is captured by Python and made available for reading.
    #  After the child process completes its execution -- Python can read the output captured in the pipe and (in this case) open the link in Opera incognito browser.

    subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


if __name__ == '__main__':
    run_opera_incognito(URL="https://google.com")
