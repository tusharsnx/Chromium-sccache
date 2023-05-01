import os

def write_github_output(name: str, value: str):
    # $GITHUB_OUTPUT will always be available, default value is to avoid typing error.
    github_output_filepath = os.getenv("GITHUB_OUTPUT", "output.txt") 
    with open(github_output_filepath, "a") as f:
        f.write("{}={}\n".format(name, value))

def write_github_env(name: str, value: str):
    # $GITHUB_OUTPUT will always be available, default value is to avoid typing error.
    github_output_filepath = os.getenv("GITHUB_ENV", "output.txt") 
    with open(github_output_filepath, "a") as f:
        f.write("{}={}\n".format(name, value))