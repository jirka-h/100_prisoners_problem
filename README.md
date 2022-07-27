# 100_prisoners_problem
Program to simulate the probability to have chains/loops longer than the number of prisoners/2 for "The 100 Prisoners Riddle"
[The Riddle That Seems Impossible Even If You Know The Answer](https://www.youtube.com/watch?v=iSNsgj1OCLA)
[100 prisoners problem](https://en.wikipedia.org/wiki/100_prisoners_problem)

## Usage:
```
$./prisoners.py
Iteration 100000 out of 1000000 (10.0 %)
Iteration 200000 out of 1000000 (20.0 %)
Iteration 300000 out of 1000000 (30.0 %)
Iteration 400000 out of 1000000 (40.0 %)
Iteration 500000 out of 1000000 (50.0 %)
Iteration 600000 out of 1000000 (60.0 %)
Iteration 700000 out of 1000000 (70.0 %)
Iteration 800000 out of 1000000 (80.0 %)
Iteration 900000 out of 1000000 (90.0 %)
Iteration 1000000 out of 1000000 (100.0 %)
Probablity to have chain longer than 50 is:
  By simulation: 68.8652%
  By theory    : 68.81721793101951%
  Difference   : -0.04798206898048818%
```

## Changing the parameters of the simulation

1. Number of prisoners - change the value bellow directly in the script:
```
number_of_prisoners = 100
```
2. Number of random realizations - change the value bellow directly in the script:
```
iterations = int(1e6)
```
