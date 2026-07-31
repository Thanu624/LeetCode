class Solution:
    def minimumPushes(self, word: str) -> int:
        # Create a dictionary to store the frequency of each letter in the word
        letter_counts = {}
        
        # Count the occurrences of each letter in the word and store in the dictionary
        for c in word:
            letter_counts[c] = letter_counts.get(c, 0) + 1
        
        # Create a list to store the counts of each letter from the dictionary
        counts = list(letter_counts.values())
        
        # Sort the counts in descending order to prioritize the most frequent letters
        counts.sort(reverse=True)
        
        # Initialize variables to keep track of the total pushes and the current row
        ans, row = 0, 1
        
        # Iterate through the sorted counts and calculate the minimum pushes
        for i in range(len(counts)):
            # Check if more than 8 elements have been processed and if it's a multiple of 8
            # If true, increment the row number to move to the next row on the keypad
            if i > 7 and i % 8 == 0:
                row += 1
            
            # Add the minimum pushes for the current letter to the total pushes
            ans += row * counts[i]
        
        # Return the total minimum pushes required to type the word
        return ans