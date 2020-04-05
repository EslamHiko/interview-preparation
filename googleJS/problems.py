'''
Problem description
You are given a tree-shaped undirected graph consisting of N nodes and N-1 edges (N is up to 50). For a node X in the tree, let d(X) be the distance (the number of edges) from X to its farthest node. Your task is to compute the minimum value of d(X) for the given tree.

The tree has the following properties:

It is connected.
It has no cycles.
For any pair of distinct nodes X and Y in the tree, there is exactly one path connecting X and Y.
Input
Test cases will be provided in the following multiline text format, using only ASCII characters. The first line contains one integer, C, which is the number of test cases that will follow. The second line is blank. From the third line onwards, the test cases separated by a blank line will follow. Each test case describes a tree and has the following format.

N
X1 Y1
X2 Y2
...
XN-1 YN-1
N is the number of nodes in the tree. Nodes are numbered 1 through N.

Xi Yi represents an undirected edge between nodes Xi and Yi. There are N - 1 edges.

Guarantees
All numbers in the input are integers.
Number of test cases: 1 <= C <= 100
Number of nodes: 2 <= N <= 50
Node IDs: 1 <= Xi <=N, 1 <= Yi <= N, Xi != Yi
The given graph is always a tree.
Note: You can assume that the input data is valid and satisfies all constraints. Your solution does not need to include error handling code.

Output
For each test case, output the result in the following format:

Case #k: R
where k is the index of the test case, starting from 1, and R is the minimum of d(X) for the given tree.

All tokens in the output should be separated by a single space.
'''
'''
Problem description
A ramen shop offers N flavors of ramen along with M options. Flavors determine the taste of broth, such as shōyu (soy sauce), miso (soy bean paste), or tonkotsu (pork marrow). Options can be toppings (such as eggs and pork chops) and side dishes (such as rice bowls and fried chickens).

A customer there plans to spend around X Japanese yen. The customer should order exactly one flavor of ramen, and may order zero, one, or two options. Each option may be ordered only once (e.g. no “two eggs”).

Given the list of available flavors and options, each with its price, what is the price closest to X of possible orders? Here, a price is said closer to X when the difference from X is smaller. Note the customer is allowed to make an order that costs more than X.

Input
Test cases will be provided in the following format, using only ASCII characters. The first line contains one integer, C, which is the number of test cases that will follow. The second line is blank. From third line onwards, multiple test cases separated by a blank line will follow. Each test case has the following format:

X
N
FlavorName1 FlavorPrice1
FlavorName2 FlavorPrice2
…
FlavorNameN FlavorPriceN
M
OptionName1 OptionPrice1
OptionName2 OptionPrice2
…
OptionNameM OptionPriceM
X is the approximate price the customer plans to spend. N is the number of available flavors. FlavorNamei and FlavorPricei are the name and price of the i-th flavor respectively. M is the number of available options. OptionNamej and OptionPricej are the name and price of the j-th option respectively.

All tokens in a line are separated by a single space. All prices are given in Japanese yen.

Constraints
All numbers in the input are integers.
Number of test cases: 1 <= C <= 50
Customer’s budget: 1 <= X <= 10000
Number of flavors: 1 <= N <= 10
Number of options: 0 <= M <= 10
Price of each flavor: 1 <= FlavorPricei <= 10000
Price of each option: 1 <= OptionPricej <= 10000
The total price of all options does not exceed 10000.
Each name (FlavorNamei, OptionNamej) consists of English alphabets, uppercase (A-Z) and lowercase (a-z), and its length is between 1 and 16, inclusive.
All names are different within each test case.
The names are provided only to help you understand the test cases and maybe debug your programs. They do not make any effect to the output.
Note: You can assume that the input data is valid and satisfies all constraints. Your solution does not need to include error handling code.

Output
For each test case, output the result in the following format:

Case #k: Y
where k is the index of the test case, starting from 1, and Y is the price closest to X among the orders the customer can make.

If there are multiple possible prices equally close to X, prefer the lower value. For example, if the customer with (X = 1000) has choices to spend 900 yen and 1100 yen, but not any price in between, your program should output 900 rather than 1100.

Sample input
File: task1-sample-input.txt (You can download the file using right click -> "Save this link as" or similar)

8

1000
3
Shoyu 800
Miso 850
Tonkotsu 900
2
Egg 100
Sprout 150

1000
2
Shoyu 850
Miso 900
2
Rice 200
Chickens 250

1000
2
Superior 1100
Original 900
1
Veggies 200

1000
4
Shoyu 800
Miso 800
Shio 800
Tonkotsu 800
1
Egg 100

1000
4
Shoyu 700
Miso 700
Shio 700
Tonkotsu 700
3
Egg 100
Sprout 100
ExtraPork 100

1000
2
Miso 700
Shio 750
3
Butter 100
Gyoza 350
FriedRice 650

1000
1
MagicalFlavor 10000
0

10000
1
MagicalFlavor 10000
1
MagicalOption 10000
Output for sample input
File: task1-sample-output.txt (You can download the file using right click -> "Save this link as" or similar)

Case #1: 1000
Case #2: 1050
Case #3: 900
Case #4: 900
Case #5: 900
Case #6: 1050
Case #7: 10000
Case #8: 10000
Hint
Case #1: the customer can spend exactly 1,000 yen (two possible orders).
Case #2: the customer may make an order more expensive than 1,000 yen.
Case #3: the program should prefer 900 (lower) over 1,100 (higher).
Case #4: the customer may not order “two eggs” to make it 1,000 yen.
Case #5: the customer may not order all three options to make it 1,000 yen.
Case #6: the customer is not allowed to order only side dishes (Gyoza and FriedRice).
Case #7: an insane ramen shop, added merely as a boundary case.
Case #8: an even more insane ramen shop, added merely as a boundary case.
'''
