import os
import subprocess
import sys
import glob

here = os.path.dirname(os.path.abspath(__file__))
files = sorted(glob.glob(os.path.join(here, "exp*.py"))) + [os.path.join(here, "assessment1.py")]
for f in files:
    print(f"\n===== {os.path.basename(f)} =====")
    subprocess.run([sys.executable, f], check=True, cwd=here)
