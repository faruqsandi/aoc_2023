import requests
from myconfig import cookies

response = requests.get("https://adventofcode.com/2023/day/1/input", cookies=cookies)

total_num = 0
for line in response.text.splitlines():
    while not line[0].isdigit():
        line = line[1:]
    while not line[-1].isdigit():
        line = line[:-1]
    total_num += int(line[0] + line[-1])
print("answer:", total_num)
