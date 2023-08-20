# CLOCK CONVERSION

## OVERVIEW

The clock_conversion function is a Python utility that converts a time string from the 12-hour clock format (with AM/PM) to the 24-hour clock format.
eg 8:30 am to 0830
   8:30  pm to 2030

## FEATURES
1.Converts a time string from "hh:mm AM/PM" to "hhmm" (24-hour format).

## HOW IT WORKS
1. Open your terminal and  move to the folder holding the python files  in this case lib folder using this command:

      cd lib

2. Open the python shell to run your commands by typing in this command in the terminal:

    python3

The command depends on the python version..In this Project we will use python3

3. Import the function clock_conversion from the file by entering the following command in the terminal and press Enter:

      from clock import clock_conversion

4. Call the function with a time string as an argument.
      
       time_str = "02:30 PM"
       result = clock_conversion(time_str)
       print(result)  

The output expected should be  "1430".



# POSITIVE INTEGERS

## OVERVIEW

The positive_integers function is a Python utility that checks if exactly two out of three input integers are positive numbers (greater than zero). It returns True if this condition is met and False otherwise.

## FEATURES

Checks if exactly two out of three integers are positive.

## HOW IT WORKS
1. Open your terminal and  move to the folder holding the python files  in this case lib folder using this command:

      cd lib

2. Open the python shell to run your commands by typing in this command in the terminal:

    python3

The command depends on the python version..In this Project we will use python3

3. Import the function positive_integers  from the file by entering the following command in the terminal and press Enter:

      from positive import positive_integers

4. Call the function with three integers as arguments.
     result = positive_integers(2, 4, -3)
     print(result) 
    
The output expected in this particulart case is True


# CONSONANT SEARCH

## OVERVIEW

The consonant_find function is a Python utility that calculates the value of consonant substrings in a given word and finds the maximum value among them. It is designed to help you solve problems that involve assigning values to consonants in words.

## FEATURES

1. Calculates the value of consonant substrings in a word.
2. Finds the maximum value among the calculated substring values.

## HOW IT WORKS
1. Open your terminal and  move to the folder holding the python files  in this case lib folder using this command:

      cd lib

2. Open the python shell to run your commands by typing in this command in the terminal:

    python3

The command depends on the python version..In this Project we will use python3

3. Import the function consonant_find from the file by entering the following command in the terminal and press Enter:

      from consonant import consonant_find

4. Call the function with a word as an argument
     result = positive_integers("zodiacs")
     print(result) 
    
The output expected in this particulart case is 26

# LICENSE

This utility is provided under the MIT License. Feel free to use and modify it in your projects.

# CREDITS

This Project was created by Wambui Karanja.

# CONTACT 
If you have any questions or suggestions, please feel free to contact wambuik03@gmail.com.








