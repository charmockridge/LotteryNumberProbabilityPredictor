# Test Plan

## Unit Testing - scraper.py
|TestID|Test|Inputs|Expected Outcome|
|------|----|------|----------------|
|1|Determines whether format_draw_date() is functioning as intended.|"Sunday 1st Jan 2023"|Pass - It should return 01/01/2023|
|2|Determines whether format_draw_date() is functioning as intended.|"Monday 2nd Feb 2004"|Pass - It should return 02/02/2004|
|3|Determines whether format_draw_date() is functioning as intended.|"Tuesday 3rd Mar 2020"|Pass - It should return 03/03/2020|
|4|Determines whether format_draw_date() is functioning as intended.|"Wednesday 3rd Mar 2020"|Pass - It should return 03/03/2020 despite the 03/03/2020 not being a Wednesday|
|5|Determines whether format_draw_date() is functioning as intended.|"Saturday 4th Aug 2012"|Pass - It should return 04/08/2012|
|6|Determines whether format_draw_date() is functioning as intended and can handle leap years.|"Saturday 28th Feb 2015"|Pass - It should return 28/02/2015|
|7|Determines whether format_draw_date() is functioning as intended and can handle leap years.|"Monday 29th Feb 2016"|Pass - It should return 29/02/2016|
|8|Determines whether format_draw_date() is functioning as intended and can handle leap years.|"Wednesday 29th Feb 2017"|Fail - It should return an error|
|9|Determines whether format_draw_date() is functioning as intended.|"Tuesday 31st Apr 2018"|Fail - It should return an error|
|10|Determines whether format_drawn_numbers() is functioning as intended.|"12\n13\n14\n"|Pass - It should return ["12", "13, "14"]|
|11|Determines whether format_drawn_numbers() is functioning as intended.|"\n\n22\n23\n24\n\n25"|Pass - It should return ["22", "23, "24", "25"]|
|12|Determines whether format_drawn_numbers() is functioning as intended.|"1\n2\n \n   \n\n3\n4\n5\n \n  "|Pass - It should return ["1", "2", "3", "4", "5"]|
|13|Determines whether format_maker_code() is functioning as intended.|"\nABCD12345\n"|Pass - It should return "ABCD12345"|
|14|Determines whether format_maker_code() is functioning as intended.|"\n\n"|Pass - It should return ""|
|15|Determines whether format_maker_code() is functioning as intended.|""|Pass - It should return ""|
|16|Determines whether format_maker_code() is functioning as intended.|"GHJD74926"|Pass - It should return "GHJD74926"|
|17|Determines whether format_maker_code() is functioning as intended.|"GHJD74926 plus another 5 winners"|Pass - It should return "Multiple millionaire maker codes"|
|18|Determines whether format_maker_code() is functioning as intended.|"THJ553468"|Pass - It should return "THJ553468"|
|19|Determines whether format_maker_code() is functioning as intended.|"abcd12345"|Pass - It should return "Multiple millionaire maker codes"|
|20|Determines whether format_maker_code() is functioning as intended.|"abc123456"|Pass - It should return "Multiple millionaire maker codes"|
|21|Determines whether format_prize() is functioning as intended.|"\n£123,456,789\n\n"|Pass - It should return ["£123,456,789", "No"]|
|22|Determines whether format_prize() is functioning as intended.|"£95,264,254\nRolled"|Pass - It should return ["£123,456,789", "Yes"]|
|23|Determines whether export_to_excel() is functioning as intended.|Filename of "test" and data of [{"Header_1": "Data_1}]|Pass - It should create test.xlsx with a column name of "Header_1" and a data cell with "Data_1"|
|24|Determines whether export_to_excel() is functioning as intended.|Filename of "test" and data of [{"Col_1": "Data_1.0}, {"Col_2": "Data_2"}]|Pass - It should override test.xlsx with new columns named of "Col_1" and "Col_2" with data "Data_1.0" and "Data_2"|
