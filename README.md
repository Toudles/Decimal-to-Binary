In Computer Science we often work with different number systems to represent data. The most commonly used number system (which we refer to as "decimal") is a "base 10" number system, which means that we use the values 0-9 to represent all numbers.

The binary number system is a "base 2" number system, which means that we use the values 0 and 1 to represent all numbers. We refer to each value in a binary number as a "bit" (i.e. the number 0101 consists of 4 bits)

You can convert a decimal number into a binary number by doing the following:
  - Attempt to divide the number by 2.
  - If there is a remainder you should record the bit 1.
  - If there is no remainder, you should record the bit 0.
  - Divide the number by 2 and throw away the remainder.
  - If the number is positive, repeat the process.
  - If the number is 0, you should end the process.

Your challenge for this assignment is to write a program that prompts the user for an integer greater than or equal to zero. If the user supplies a value less than 0 you should re-prompt them. Next, articulate the steps necessary to convert the number in question to binary.
