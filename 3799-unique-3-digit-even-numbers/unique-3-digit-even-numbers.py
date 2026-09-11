class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        # Set to store unique 3-digit numbers
        unique_numbers = set()
      
        # Iterate through all digits to find candidates for ones place (must be even)
        for ones_index, ones_digit in enumerate(digits):
            # Skip if ones digit is odd (number must be even)
            if ones_digit & 1:
                continue
          
            # Iterate through all digits for tens place
            for tens_index, tens_digit in enumerate(digits):
                # Skip if using the same digit position as ones place
                if ones_index == tens_index:
                    continue
              
                # Iterate through all digits for hundreds place
                for hundreds_index, hundreds_digit in enumerate(digits):
                    # Skip if hundreds digit is 0 (not valid for 3-digit number)
                    # or if using same digit position as ones or tens place
                    if hundreds_digit == 0 or hundreds_index in (ones_index, tens_index):
                        continue
                  
                    # Construct the 3-digit number and add to set
                    number = hundreds_digit * 100 + tens_digit * 10 + ones_digit
                    unique_numbers.add(number)
      
        # Return count of unique 3-digit numbers
        return len(unique_numbers)
