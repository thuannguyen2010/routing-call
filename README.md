# Routing Call Service

## Problem

### Routing of telephone calls

Some telephone operators have submitted their price lists including price per minute for different phone number
prefixes. The price lists look like this:

- Operator A

| Prefix | Price |
|--------|-------|
| 1      | 0.9   |
| 268    | 5.1   |
| 46	    | 0.17  |
| 4620   | 0.0   |
| 468    | 0.15  |
| 4631   | 0.15  |
| 4673   | 0.9   |
| 4673   | 1.1   |

- Operator B:

| Prefix | Price |
|--------|-------|
| 1      | 0.92  |
| 44     | 0.5   |
| 46     | 0.2   |
| 467    | 1.0   |
| 48     | 1.2   |

And so on...

The left column represents the telephone prefix (country + area code) and the right column represents the operators
price per minute for a number starting with that prefix. When several prefixes match the same number, the longest one
should be used. If you, for example, dial +46-73-212345 you will have to pay $ 1.1/min with Operator A and $ 1.0/min
with Operator B.

If a price list does not include a certain prefix you cannot use that operator to dial numbers starting with that
prefix. For example it is not possible to dial +44 numbers with operator A but it is possible with Operator B.

### The Goal

The goal with this exercise is to write a program that can handle any number of price lists (operators) and then can
calculate which operator that is cheapest for a certain number. You can assume that each price list can have thousands
of entries but they will all fit together in memory.

Telephone numbers should be inputted in the same format as in price lists, for example “68123456789”. The challenge is
to find the cheapest operator for that number.

## Solution

### Data structure

I use Trie as my data structure to store data of price lists. I assume:
- m: number of operators 
- n: number of entries in price of each operator
- l: average length of all prefixes

So the time complexity to build trie is ```O(m*n*l)```

### Get the cheapest price

After building the data structure to store price list, we can find the cheapest operator by search the longest prefix with phone number

Assume ```n``` is the length of phone number that we need to find the operator. The complexity to find will be ```O(n)```

## Continues

- We can generalize the data structure to adapt with removal operation. In stead of storing only min pricing in for each prefix. We can store list of all pricing for 1 prefix, if we need to remove some price list in the future, we just remove in list of that prefix
- For huge data, we can persist trie in the database (MongoDB or MySQL) and we can find the operator by query in the database.