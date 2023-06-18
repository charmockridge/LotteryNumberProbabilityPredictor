import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime


def get_euromillions_draw_history():
    EUROMILLIONS_URL = "https://www.lottery.co.uk/euromillions/results/archive-"
    EUROMILLIONS_START_YEAR = 2004
    current_year = date.today().year
    data = []

    for i in range(current_year, EUROMILLIONS_START_YEAR - 1, -1):
        response = requests.get(EUROMILLIONS_URL + str(i))
        soup = BeautifulSoup(response.text, "lxml")

        table = soup.find("table")
        rows = table.find_all("tr")[1:]
        
        for row in rows:
            cells = row.find_all("td")

            draw_date = format_draw_date(cells[0].text)
            drawn_numbers = format_drawn_numbers(cells[1].text)

            if len(cells) == 4:
                maker_code = format_maker_code(cells[2].text)
                prize = format_prize(cells[3].text)
            else:
                maker_code = ""
                prize = format_prize(cells[2].text)

            draw = {}
            draw["draw_date"] = draw_date
            draw["num_1"] = str(drawn_numbers[0])
            draw["num_2"] = drawn_numbers[1]
            draw["num_3"] = drawn_numbers[2]
            draw["num_4"] = drawn_numbers[3]
            draw["num_5"] = drawn_numbers[4]
            draw["bonus_1"] = drawn_numbers[5]
            draw["bonus_2"] = drawn_numbers[6]
            draw["millionaire_maker_code"] = maker_code
            draw["jackpot"] = prize[0]
            draw["rollover"] = prize[1]

            data.append(draw)

    export_to_xlsx("euromillions", data)


def get_lotto_draw_history():
    LOTTO_URL = "https://www.lottery.co.uk/euromillions/results/archive-"
    LOTTO_START_YEAR = 1994
    current_year = date.today().year
    data = []

    for i in range(current_year, LOTTO_START_YEAR - 1, -1):
        response = requests.get(LOTTO_URL + str(i))
        soup = BeautifulSoup(response.text, "lxml")

        table = soup.find("table")
        rows = table.find_all("tr")[1:]

        for row in rows:
            cells = row.find_all("td")

            draw_date = format_draw_date(cells[0].text)
            drawn_numbers = format_drawn_numbers(cells[1].text)
            prize = format_prize(cells[2].text)

            draw = {}
            draw["draw_date"] = draw_date
            draw["num_1"] = str(drawn_numbers[0])
            draw["num_2"] = drawn_numbers[1]
            draw["num_3"] = drawn_numbers[2]
            draw["num_4"] = drawn_numbers[3]
            draw["num_5"] = drawn_numbers[4]
            draw["num_6"] = drawn_numbers[5]
            draw["bonus_1"] = drawn_numbers[6]
            draw["jackpot"] = prize[0]
            draw["rollover"] = prize[1]

            data.append(draw)

        
    export_to_xlsx("lotto", data)


def export_to_xlsx(filename, data):
    df = pd.DataFrame(data)
    df.to_excel(filename + ".xlsx")


def format_draw_date(draw_date):
    draw_date = draw_date.replace("th", "")
    draw_date = draw_date.replace("st", "")
    draw_date = draw_date.replace("nd", "")
    draw_date = draw_date.replace("rd", "")
    draw_date = datetime.strptime(draw_date, "%A %d %b %Y").strftime("%d/%m/%Y")

    return draw_date


def format_drawn_numbers(numbers):
    drawn_numbers = numbers.split("\n")
    return list(filter(None, drawn_numbers))


def format_maker_code(maker_code):
    maker_code = maker_code.replace("\n", "")

    if maker_code == "":
        return ""

    pattern_1 = "^[A-Z]{4}[0-9]{5}$"
    pattern_2 = "^[A-Z]{3}[0-9]{6}$"
    valid_1 = re.match(pattern_1, maker_code) != None
    valid_2 = re.match(pattern_2, maker_code) != None

    if valid_1 is True or valid_2 is True:
        return maker_code
    else:
        return "Multiple millionaire maker codes"


def format_prize(prize_information):
    prize = []
    prize_information = prize_information.replace("\n", "")

    if "Rolled" in prize_information:
        prize_information = prize_information.replace("Rolled", "")
        prize.append(prize_information)
        prize.append("Yes")
    elif "Roll Down" in prize_information:
        prize_information = prize_information.replace("Roll Down", "")
        prize.append(prize_information)
        prize.append("Roll Down")
    else:
        prize.append(prize_information)
        prize.append("No")

    return prize


if __name__ == "__main__":
    get_euromillions_draw_history()