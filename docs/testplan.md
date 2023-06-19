# Test Plan

## Unit Testing - scraper.py
|TestID|Test|Inputs|Expected Outcome|
|------|----|------|----------------|
|S.1|Determines whether format_draw_date() is functioning as intended.|"Sunday 1st Jan 2023"|Pass - It should return 01/01/2023|
|S.2|Determines whether format_draw_date() is functioning as intended.|"Monday 2nd Feb 2004"|Pass - It should return 02/02/2004|
|S.3|Determines whether format_draw_date() is functioning as intended.|"Tuesday 3rd Mar 2020"|Pass - It should return 03/03/2020|
|S.4|Determines whether format_draw_date() is functioning as intended.|"Wednesday 3rd Mar 2020"|Pass - It should return 03/03/2020 despite the 03/03/2020 not being a Wednesday|
|S.5|Determines whether format_draw_date() is functioning as intended.|"Saturday 4th Aug 2012"|Pass - It should return 04/08/2012|
|S.6|Determines whether format_draw_date() is functioning as intended and can handle leap years.|"Saturday 28th Feb 2015"|Pass - It should return 28/02/2015|
|S.7|Determines whether format_draw_date() is functioning as intended and can handle leap years.|"Monday 29th Feb 2016"|Pass - It should return 29/02/2016|
|S.8|Determines whether format_draw_date() is functioning as intended and can handle leap years.|"Wednesday 29th Feb 2017"|Fail - It should return an error|
|S.9|Determines whether format_draw_date() is functioning as intended.|"Tuesday 31st Apr 2018"|Fail - It should return an error|
|S.10|Determines whether format_drawn_numbers() is functioning as intended.|"12\n13\n14\n"|Pass - It should return ["12", "13, "14"]|
|S.11|Determines whether format_drawn_numbers() is functioning as intended.|"\n\n22\n23\n24\n\n25"|Pass - It should return ["22", "23, "24", "25"]|
|S.12|Determines whether format_drawn_numbers() is functioning as intended.|"1\n2\n \n   \n\n3\n4\n5\n \n  "|Pass - It should return ["1", "2", "3", "4", "5"]|
|S.13|Determines whether format_maker_code() is functioning as intended.|"\nABCD12345\n"|Pass - It should return "ABCD12345"|
|S.14|Determines whether format_maker_code() is functioning as intended.|"\n\n"|Pass - It should return ""|
|S.15|Determines whether format_maker_code() is functioning as intended.|""|Pass - It should return ""|
|S.16|Determines whether format_maker_code() is functioning as intended.|"GHJD74926"|Pass - It should return "GHJD74926"|
|S.17|Determines whether format_maker_code() is functioning as intended.|"GHJD74926 plus another 5 winners"|Pass - It should return "Multiple millionaire maker codes"|
|S.18|Determines whether format_maker_code() is functioning as intended.|"THJ553468"|Pass - It should return "THJ553468"|
|S.19|Determines whether format_maker_code() is functioning as intended.|"abcd12345"|Pass - It should return "Multiple millionaire maker codes"|
|S.20|Determines whether format_maker_code() is functioning as intended.|"abc123456"|Pass - It should return "Multiple millionaire maker codes"|
|S.21|Determines whether format_prize() is functioning as intended.|"\n£123,456,789\n\n"|Pass - It should return ["£123,456,789", "No"]|
|S.22|Determines whether format_prize() is functioning as intended.|"£95,264,254\nRolled"|Pass - It should return ["£123,456,789", "Yes"]|
|S.23|Determines whether export_to_excel() is functioning as intended.|Filename of "test" and data of [[{"Header_1": "Data_1}]]|Pass - It should create test.xlsx with a column name of "Header_1" and a data cell with "Data_1"|
|S.24|Determines whether export_to_excel() is functioning as intended.|Filename of "test" and data of [[{"Col_1": "Data_1.0, "Col_2": "Data_2"}]]|Pass - It should override test.xlsx with new columns named of "Col_1" and "Col_2" with data "Data_1.0" and "Data_2"|
|S.25|Determines whether export_to_excel() is functioning as intended.|Filename of "test" and data of [[{"Col_1": "Data_1.0, "Col_2": "Data_2", "Col_3": ""}], [{"Col_1": "Data 3", "Col_2": "Data 4", "Col_3": "Data 5"}], [{"Col_1": "A", "Col_2": "", "Col_3": "BC"}]]|Pass - It should override test.xlsx with new columns and data corresponding to that of the inputted test data.|
|S.26|Determines that requests returns the expected HTML.| "testpage.html" which points to a local HTML file.|Pass - It should return the HTML stored in testpage.html|
|S.27|Determines as to whether the scraper returns the expected results for the euromillions lottery type.| "eurotestpage.html" which points to a local HTML file.|Pass - It should return the HTML stored in testpage.html|
|S.28|Determines as to whether the scraper returns the expected results for the euromillions lottery type with three columns in table.| "eurotestpage2.html" which points to a local HTML file.|Pass - It should return the HTML stored in testpage.html|
|S.29|Determines as to whether the scraper returns the expected results for the lotto lottery type.| "lottotestpage.html" which points to a local HTML file.|Pass - It should return the HTML stored in testpage.html|