import gspread

#service account
sa = gspread.service_account()

#spreadsheet as sh variable
#sa.open() opens the google drive document
sh = sa.open("Bingo Winnings")

#wks variable used to pass in selected spreadsheet to work on
wks = sh.worksheet("Week 1 Bingo Winnings")

#use different methods to manipulate data
#print all records
#print(wks.get_all_records())
#print(wks.get_all_values())
#print('Rows: ', wks.row_count)
#print('Cols: ', wks.row_count)
#print(wks.cell(20, 4).value)

#green = wks.findall('Green Special')
#print(green)

values = wks.row_values(1)
print(values)