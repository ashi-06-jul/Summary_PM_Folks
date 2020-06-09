import re
from datetime import datetime
import pandas as pd
import json
from iteration_utilities import duplicates

file = open ("w.txt",'r')
f = file.readlines()
data=json.loads(f)
print(type(data))
