# The 100 Prisoners problem
The 100 prisoners problem is a mathematical problem in probability theory and combinatorics, [first proposed](https://www.brics.dk/RS/03/44/BRICS-RS-03-44.pdf) in 2003 by danish computer scientists Peter Bro Miltersen and Anna Gál.</br>
In this problem, each of 100 numbered prisoners must find their own number in one of 100 drawers in order to survive. The rules state that each prisoner may open only 50 drawers and cannot communicate with other prisoners. the prisoners may decide on a strategy before they start.</br> At first glance, the situation appears hopeless (probability of success is $1\over2 ^{100}$), but a clever strategy offers the prisoners a more realistic (~30%) chance of survival.

## Seminar
as part of our SE BSc [Daniella Vardi](https://github.com/DaniellaVardi) and I have decided to explore this problem and created a python GUI program that simulates the problem and shows how one suggested strategy can significantly improve the prisoners chance of survival. The seminar has been guided by Dr. Yitzhak Aviv of the Afeka college of Engineering.

The problem, the suggested strategy and the mathematical approach behind it are beautifully described by the [Veritasium youtube video](https://www.youtube.com/watch?v=iSNsgj1OCLA)

## Getting started
1. Clone the repository using `git clone https://github.com/Noam-Levy/The100Prisoners.git`
2. Change to the repository working directory using `cd The100Prisoners`
3. install the required dependencies using `pip install -r requirements.txt` or `python -m pip install -r requirements.txt`
4. run using `python main.py`
