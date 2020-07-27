def get_east_asian_width_count(text):
      import unicodedata
      count = 0
      for c in text:
          if unicodedata.east_asian_width(c) in 'FWA':
              count += 2
          else:
              count += 1
      return count



"""a = ["あいうえお","aiueo","あい１２３","１２３12"]
for test in a:
    c = get_east_asian_width_count(test)
    print(c)"""

"""
c = get_east_asian_width_count(123)
print(c)
"""
