import os
import requests
from string import Template


def get_session_id(filename):
    with open(filename) as f:
        return f.read().strip()


YEAR = 2024
SESSION_ID_FILE = "session.cookie"
SESSION = get_session_id(SESSION_ID_FILE)
HEADERS = {
    "User-Agent": "https://github.com/BenWarwick-Champion"
}
COOKIES = {"session": SESSION}


def get_url(year, day):
    return f"https://adventofcode.com/{year}/day/{day}/input"


def find_latest_day():
    return max([int(file[3:5]) for file in os.listdir('src')])


def get_input(day):
    url = get_url(YEAR, day)
    response = requests.get(url, headers=HEADERS, cookies=COOKIES)
    if not response.ok:
        raise RuntimeError(
            f"Request failed\n\tstatus code: {response.status_code}\n\tmessage: {response.content}"
        )
    return response.text[:-1]


if __name__ == "__main__":
    latest_day = find_latest_day()
    next_day = latest_day + 1 if latest_day else 1

    template_mapping = {
        'day': f'# Day {next_day:02d}',
        'input': f'    with open("input/day{next_day:02d}.txt") as f:'
    }

    with open('utils/template.txt', 'r') as f:
        template = Template(f.read())
        new_day_file = template.substitute(template_mapping)

    with open(f'src/day{next_day:02d}.py', 'w') as f:
        f.write(new_day_file)

    with open(f'input/day{next_day:02d}.txt', 'w') as f:
        f.write(get_input(next_day))
