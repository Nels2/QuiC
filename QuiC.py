# This program 'QuiC' makes ratios simple. - as they should be. 
# Enjoy!
# Made by Nels_27/Nels2.



Accounting = True
while Accounting:
  print("============QuiC 1.0=================")
  print("============made by: Nels2===========")

  print("                                    ")
    #some random text art. - looks cool though. 
  print(" /﹋\                               ")
  print("(҂`_´)                              ")
  print("<,︻╦╤─ ҉ - -------------D          ")
  print(" /﹋\                               ")
  print("─────────────────────────────────────")
  print("What kind of ratio do you want to do?")
  print("                                    ")
  print("Available Options are: ")
  print("                                     ")
  print("|──────────────────────────────────|")
  print("|1. Return on Investments          |")
  print("|2. Quick                          |")
  print("|3. Return on Equity               |")
  print("|4. Gross Margin                   |")
  print("|5. Accounts Receivables Turnover  |")
  print("|6. Inventory Turnover             |")
  print("|7. Accounts Payable Turnover      |")
  print("|8. Current                        |")
  print("|──────────────────────────────────|")
  #1-7 are  options that can be chosen. each option just takes the numers entered and does the equation quick and simple - no mess.
  option = input("  ~ Option: ")
  if option == '1':
    print("======= Return on Investments ======")
    x =float(input("    Enter Net Income:"))
    y = float(input("   Enter Avg. Total Assets:"))
    print("  ~ Return on Investments Ratio = " + str(float(x / y)) + "%")
  if option == '2':
    print("======= Quick =====================")
    a = float(input("   Enter Cash:"))
    b = float(input("   Enter Short-Term Investments:"))
    c = float(input("   Enter Receivables:"))
    d = float(input("   Enter Current Liabilities:"))
    print("  ~ Quick Ratio = " + str(float(a + b + c) / d) + "%")
  if option == '3':
    print("======= Return on Equity    =======")
    n = float(input("   Enter Net Income:"))
    o = float(input("   Enter Average Owners Equity:"))
    print("  ~ Return On Equity" + str(float(n / o)) + "%")
  if option == '4':
    print("======= Gross Margin ==============")
    g = float(input("   Enter Gross Margin:"))
    s = float(input("   Enter Sales:"))
    print("  ~ Gross Margin Ratio = " + str(float(g / s)) + "%")
  if option == '5':
    print("======= A.R. Turnover =============")
    w = float(input("   Enter Sales:"))
    t = float(input("   Enter Avg. Accts. Receivable:"))
    print("               ~Turnover = " + str(float(w / t)) + "%")
    print("               ~Days = " + str(float(365/(w / t))))
  if option == '6':
    print("======= Inventory Turnover ========")
    u = float(input("   Enter Cost of Sales:"))
    i = float(input("   Enter Avg. Inventory:"))
    print("                       ~Turnover = " + str(float(u / i)) + "%" )
    print("                       ~Days = " + str(float(365/(u / i))))
  if option == '7':
    print("======= A.P. Turnover =============")
    m = float(input("   Enter Cost of Sales:"))
    p = float(input("   Enter Avg. Accts. Payable:"))
    print("                       ~Turnover = " + str(float(m / p)))
    print("                       ~Days = " + str(float(365/(m / p))))
  if option == '8':
    print("======== Current Ratio =============")
    j = float(input("   Enter Current Assets:"))
    k = float(input("   Enter Current Liablities:"))
    print("  ~ Current Ratio = " + str(float(j / k)) + "%")
  cont = input("  ~ New Ratio? ")
  if cont != 'yes':
    #resets, main screen is represented again.
    break
print("  ~ exiting...")
