# Exercises

Create these files inside your own folder:
`submissions/<your-github-username>/`.

In the example runs the prompt is on its own line and the user types on
the next line. To get that, end the prompt with `\n`, as in Workshop 2:
`input("What is your name?\n")`.

## exercise_1.py — Countdown

Ask the user for a number with `input()`, cast it to `int`. Using a
`while` loop, print every number from that number down to `1`. After
the loop, print `"Liftoff!"` once.

Example run (input is `3` — the first `3` is what the user typed):
```
Count down from:
3
3
2
1
Liftoff!
```

## exercise_2.py — Fix the bug

This code should print the even numbers from 2 to 10, but it prints `2`
forever. Copy it into `exercise_2.py`, run it (press `Ctrl+C` to stop
it), then fix the loop so it ends. After `Ctrl+C` you will see
`KeyboardInterrupt` — that is normal, it is not the bug.

```python
number = 2

while number <= 10:   # BUG: this loop never ends
    print(number)

print("Done")
```

Expected output:
```
2
4
6
8
10
Done
```

## exercise_3.py — Sum of numbers

Ask the user for a number with `input()`, cast it to `int`. Using a
`for` loop with `range()`, add up every number from `1` to that number
(including it) and print the total.

Example run (input is `5`; 1 + 2 + 3 + 4 + 5 = 15):
```
Enter a number:
5
Sum: 15
```

## exercise_4.py — Count the vowels

Ask the user for a word with `input()` and make it lowercase with
`.lower()`. Using a `for` loop over the word, count how many of its
letters are vowels (`a`, `e`, `i`, `o`, `u`) and print the count.

Example run (input is `Orange`):
```
Enter a word:
Orange
Vowels: 3
```

## exercise_5.py — Bonus: guess the number

Store a secret number in a variable: `secret = 7`. Using a `while`
loop, keep asking the user for a guess (cast it to `int`) until they
get it right. After each wrong guess print `"Too low"` or `"Too high"`.
When the guess is correct, print `"Correct!"` and stop.

Example run (inputs are `5`, `9`, `7`):
```
Guess the number:
5
Too low
Guess the number:
9
Too high
Guess the number:
7
Correct!
```
