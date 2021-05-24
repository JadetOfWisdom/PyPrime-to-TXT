# PyPrime-to-TXT
Prime number generator that allows you to resume where you left off. It saves all results in readable .txt file.
# Run
`python3 PrimeNumber.py`
# Story
This program is writing out of my insomniac pressure at 3 am, and finished it at 9 am. I have been programming for many years but never really dove into this popular topic before.
I had done school examples before though, it was in C, and it's brain dead example. This time, I want to see for myself if I can do it without much guidance.
I read the theories from Wikipedia. I learn to write python program again after left it in dusts for many years. I chose python because it's easy to do in ubuntu subsystem for windows 10. However, I find more troublesome upgrading outdated Ubuntu to the latest LTS just to get the newest supported version of python (3.8.5) than the program itself.
# How it works?
The program creates 2 files:
  1. [number.txt](number.txt) to store the most recent number that had been checked.
  2. [prime.txt](prime.txt) to store very prime number it found.
These two works in conjuction to help save time checking prime factorization.
It then read both of them and start to check by increasing number in [number.txt](number.txt) by one and for every number in [prime.txt](prime.txt) that's doesn't exceed `sqrt(number)`
(a least that's the logic, and it turned out that I didn't do that.). If the number happened to be `moded by any number and gives 0`, the whole sequences is skipped.
And if finally no number can `mod number and get 0`, it's the prime we're looking for.
If the prime is detected, it prints out `the latest order of prime + 1` before appending it to [prime.txt](prime.txt)
That's it! notthing more.

# Extra Notes
How ever, due to lack of knowledge or the languege capability, I can not find a way to read a file in small chunks so it's not eating up the RAM. However, I'm aware that python can read files in lines without buffering the whole file to RAM. Might capitalize it later.

Memory usage of this program is in prime time notation as it's only stores prime numbers.
