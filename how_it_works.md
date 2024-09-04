You may have noticed at first glance that there is a program that automatically selects a number and you have to guess that number using multiple guesses.And it is possible that you, like other ordinary people, will finally reach the number with a lot of guesswork, and in my opinion, this path is too long for you to test the numbers one by one in a simple way.In general, this method tells you that you must guess the middle of the numbers, for example, if you want a number between 1 and 100, you must first count 50, then the program will definitely answer you, now, according to the answer of the program, you have to find the middle of the new numbers.  For example, after guessing the number 50, we are told that the input number is low, we have to calculate the middle between 100 and 50 and enter the middle guess in the input to get a clue again.  This method continues until you can find the final number.

I want to solve an example for you to understand better: 
target number = 89

1 ... 50 ... 100
first guess = 50
>>> it's too low

50 ... 75 ...100
Second guess = 75
>>> it's too low

75 ... 87... 100
Third guess = 87
>>> it's too low

87... 92 ... 100
Fourth guess = 92
>>> it's too high 

87 ... 89 ... 92
Fifth guess = 89
>>> Congratulations. You guessed it in 5 attempts