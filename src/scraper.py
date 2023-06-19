import requests
import re
import pandas as pd
from bs4 import BeautifulSoup
from datetime import date
from datetime import datetime


def get_euromillions_draw_history():
    LOTTERY_TYPE = "euromillions"
    EUROMILLIONS_START_YEAR = 2004
    current_year = date.today().year
    data = []

    for i in range(current_year, EUROMILLIONS_START_YEAR - 1, -1):
        soup = get_html("https://www.lottery.co.uk/euromillions/results/archive-" + str(i))
        data.append(scrape_draw_history(soup, LOTTERY_TYPE))

    export_to_xlsx(LOTTERY_TYPE, data)


def get_lotto_draw_history():
    LOTTERY_TYPE = "lotto"
    LOTTO_START_YEAR = 1994
    current_year = date.today().year
    data = []

    for i in range(current_year, LOTTO_START_YEAR - 1, -1):
        soup = get_html("https://www.lottery.co.uk/euromillions/results/archive-" + str(i))
        data.append(scrape_draw_history(soup, LOTTERY_TYPE))

    export_to_xlsx("lotto", data)


# Returns HTML of given URL.
def get_html(URL):
    reposne = requests.get(URL)
    return BeautifulSoup(reposne.text, "lxml")


# Scrapes and returns each draw information stored in a table in the given HTML.
def scrape_draw_history(HTML, lottery_type):
        data = []
        table = HTML.find("table")
        rows = table.find_all("tr")[1:]
        
        for row in rows:
            draw = {}
            cells = row.find_all("td")

            draw_date = format_draw_date(cells[0].text)
            drawn_numbers = format_drawn_numbers(cells[1].text)

            draw["draw_date"] = draw_date

            # Handles information based on lottery type due to different structure.
            # Euromillions has 5 main numbers and 2 bonus number. It also has a millionaire maker code.
            # Lotto has 6 main numbers and 1 bonus ball.
            # Could be refactored num 1 - 5 are same and put 6 and maker code into if statement?
            if lottery_type == "euromillions":
                if len(cells) == 4:
                    maker_code = format_maker_code(cells[2].text)
                    prize = format_prize(cells[3].text)
                else:
                    maker_code = ""
                    prize = format_prize(cells[2].text)
                
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

            elif lottery_type == "lotto":
                prize = format_prize(cells[2].text)

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

        return data


# Exports data to spreadsheet.
def export_to_xlsx(filename, data):
    formatted_data = []

    for year in data:
        for draw in year:
            formatted_data.append(draw)

    df = pd.DataFrame(formatted_data)
    df.to_excel(filename + ".xlsx")


# Formats the scraped draw date.
# Scraped draw date format is: Tuesday 12th Jan 2023 (example)
# Desired format is: 12/01/2023
def format_draw_date(draw_date):
    # Is this necessary of can datetime handle suffixes?
    draw_date = draw_date.replace("th", "")
    draw_date = draw_date.replace("st", "")
    draw_date = draw_date.replace("nd", "")
    draw_date = draw_date.replace("rd", "")
    draw_date = datetime.strptime(draw_date, "%A %d %b %Y").strftime("%d/%m/%Y")

    return draw_date


# Formats scraped drawn numbers into array.
def format_drawn_numbers(numbers):
    drawn_numbers = numbers.split("\n")
    # Removes null elements.
    return list(filter(None, drawn_numbers))


# Formats the millionaire maker code. Euromillions only.
def format_maker_code(maker_code):
    # Four cases for maker code:
    # It can be null, maker code was introduced in November 2009 yet euromillions began in 2004.
    # It can have the pattern of 3 characters in capitals followed by 6 digits.
    # It can have the pattern of 4 characters in capitals followed by 5 digits.
    # Anything else means there are multiple maker codes.

    maker_code = maker_code.replace("\n", "")

    if maker_code == "":
        return ""

    # Original maker code pattern from 2009.
    pattern_1 = "^[A-Z]{3}[0-9]{6}$"
    # From 2016, pattern changed.
    pattern_2 = "^[A-Z]{4}[0-9]{5}$"
    valid_1 = re.match(pattern_1, maker_code) != None
    valid_2 = re.match(pattern_2, maker_code) != None

    if valid_1 is True or valid_2 is True:
        return maker_code
    else:
        return "Multiple millionaire maker codes"


# Formats prize information. Splits jackpot from rolled information.
def format_prize(prize_information):
    prize = []
    prize_information = prize_information.replace("\n", "")

    if "Rolled" in prize_information:
        prize_information = prize_information.replace("Rolled", "")
        prize.append(prize_information)
        prize.append("Yes")
    # Roll down is only relevant to lotto.
    # Roll down is where jackpot is shared on a must win draw where no one matched all numbers.
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