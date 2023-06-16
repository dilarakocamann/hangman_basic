name = input("What's your name? ")
print(f"Hello {name}")

secret_word = "Grumpy"

guess_string = " "

lives = 10

while lives > 0:    
        char_left = 0
    
        for char in secret_word:
        
            if char in guess_string:           
                print(char)
            
            else:            
                print("-")
                char_left += 1
            
        if char_left == 0:       
            print("You won")	
            break
        
          
        guess = input("Guess a word: ")
        guess_string += guess
        
        if guess not in secret_word:
                lives -= 1
                
                print("Wrong")
                print(f"You have {lives} word left")
                
                if lives == 0:
                    print("You died")