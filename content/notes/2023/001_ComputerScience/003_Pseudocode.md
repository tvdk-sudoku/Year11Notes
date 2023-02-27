---
title: Pseudocode
---
#### Problem
Write the code for a program that will add 3 numbers entered by the user and then determine if the sum of the numbers is greater than 15. If it is, the program will display a relevant message.


```Pseudocode
BEGIN
NUM1, NUM2, NUM3, SUM AS FLOAT
INPUT(NUM1, NUM2, NUM3)
SUM <- NUM1 + NUM2 + NUM3
	IF SUM > 15 THEN:
		OUTPUT("Greater than 15.")
	ENDIF
END
```


```python
# print("Greater than 15" if (float(input("> ")) + float(input("> ")) + float(input("> "))) > 15)


num1 = float(input("Number 1: "))
num2 = float(input("Number 2: "))
num3 = float(input("Number 3: "))

total = num1 + num2 + num3
if total > 15:
    print("Greater than 15.")

```


## The division method

104/2 = 0
52/2 = 0
26/2 = 0
13/2 = 1
6/2 = 0
3/2 = 1
1/2 = 1

71/2 = 1
35/2 = 1
17/2 = 1
8/2 = 0
4/2 = 0
2/2 = 0
1/2 = 1

99/2 = 1
49/2 = 1
24/2 = 0
12/2 = 0
6/2 = 0
3/2 = 1
1/2 = 1

## The Table Method

125
|           | 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |
| --------- | --- | --- | --- | --- | --- | --- | --- | --- |
| Binary    | 0   | 1   | 1   | 1   | 1   | 1   | 0   | 1   |
| Sub Total | 125 | 61  | 29  | 13  | 5   | 1   | 1   | 0   |





















