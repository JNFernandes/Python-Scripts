symbols_units = ["","I","II","III","IV",
                "V","VI","VII","VIII","IX"]

symbols_tens = ["","X","XX","XXX","XL",
                "L","LX","LXX","LXXX","XC"]

symbols_hundreds = ["","C","CC","CCC","CD","D",
                    "DC","DCC","DCCC","CM"]
                    
symbols_thousands = ["","M","MM","MMM"]                   

def int2roman(number):
  """
  Example: 238 -> transform to list [0,2,3,8] -> get the position of the roman numbers in each place based on the symbols measure
  """
  result = [symbols_thousands[int(number/1000)], 
            symbols_hundreds[int((number%1000)/100)], 
            symbols_tens[int((number%100)/10)], 
            symbols_units[int(number%10)]]
    
  print(''.join(result))

# Example 
int2roman(122) # The expected result is CXXII



