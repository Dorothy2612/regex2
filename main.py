import re
import os

if __name__ == '__main__':
    print(os.environ)
    z=re.compile("'C:")
    print(re.findall(z,str(os.environ)))
