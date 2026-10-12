# 🎂 Days Alive Counter

A small Python script that asks for your birth date and works out how old you are, using Python's `datetime` module.

## Example

```
Enter Birth Year (e.g., 2000): 2003
Enter Birth Month (1-12): 5
Enter Birth Day (1-31): 14
You are approximately 23 years old.
```

## How it works

Subtracting two `datetime.date` objects gives a `timedelta`, the exact number of days between them. Dividing by 365 gives the approximate age in years.

## Run it

```bash
python days-alive-counter.py
```

## Ideas for improvement

- Print the exact number of days alive, which the script already calculates
- Handle leap years exactly, and reject invalid dates or future birthdays
