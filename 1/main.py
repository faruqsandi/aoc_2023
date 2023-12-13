import requests

from myconfig import cookies

response = requests.get("https://adventofcode.com/2023/day/1/input", cookies=cookies)


lines = response.text.splitlines()
# lines = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen
# """.splitlines()

total_num = 0
for line in lines:
    while not line[0].isdigit():
        line = line[1:]
    while not line[-1].isdigit():
        line = line[:-1]
    total_num += int(line[0] + line[-1])
print("answer:", total_num)
number_tuple = (
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
)

total_num = 0
for line in lines:
    print("1", line)
    while not line[0].isdigit() and not line.startswith(number_tuple):
        line = line[1:]
    while not line[-1].isdigit() and not line.endswith(number_tuple):
        line = line[:-1]
    print("2", line)
    if not line[0].isdigit():
        for number in number_tuple:
            if line.startswith(number):
                line = line.replace(number, str(number_tuple.index(number) + 1), 1)
                break
        print("3", line)
    if not line[-1].isdigit():
        line = line[::-1]
        for number in number_tuple:
            number = number[::-1]
            if line.startswith(number):
                line = line.replace(
                    number, str(number_tuple.index(number[::-1]) + 1), 1
                )
                break
        line = line[::-1]
        print("4", line)
    num = int(line[0] + line[-1])
    print(line, num)
    total_num += num
print("answer 2nd:", total_num)
