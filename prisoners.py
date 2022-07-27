#!/usr/bin/env python3

"""
Computing the probability to have chains/longer longer than number_of_prisoners/2 for "The 100 Prisoners Riddle"
https://www.youtube.com/watch?v=iSNsgj1OCLA
https://en.wikipedia.org/wiki/100_prisoners_problem

To profile the script: python -m cProfile ./prisoners.py
"""
import numpy as np

def run_prisoners_simulation():
    """
    Generate random permuatations of boxes, identify all chains and record the lengths
    """
    #Number of random realizations
    iterations = int(1e6)
    number_of_prisoners = 100

    #boxes: boxes are randomly shuffled and holds number of prisoner
    boxes = np.empty(number_of_prisoners, dtype='int', order='C')

    #length_count[i] => number of chains of length i
    length_count = np.zeros(number_of_prisoners+1, dtype='int', order='C')
    rng = np.random.default_rng()

    for iteration in range(1,iterations+1):
        #Create permutation
        #https://en.wikipedia.org/wiki/Fisher%E1%80%93Yates_shuffle#The_.22inside-out.22_algorithm
        #Alternative:
        #https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.permutation.html
        #for i in range(number_of_prisoners):
        #    j = rng.integers(low=0,high=i,endpoint=True)
        #    if j != i:
        #        boxes[i] = boxes[j]
        #    boxes[j] = i
        boxes = rng.permutation(number_of_prisoners)
        #print(boxes)

        #Identify all chains/loops
        boxes_checked = {}
        for i in boxes:
            #current_chain = []
            if i in boxes_checked.keys():
                # This box was already found on some loop
                continue
            length = 1
            next_element = boxes[i]
            j = i
            #current_chain.append(j)
            boxes_checked[j] = None
            while next_element != i:
                j = next_element
                next_element = boxes[j]
                length += 1
                #current_chain.append(j)
                boxes_checked[j] = None
            #print(current_chain)
            #print(boxes_checked)
            length_count[length] += 1
        if iteration%int(1e5) == 0:
            print(f"Iteration {iteration} out of {iterations} ({100.0*iteration/iterations} %)")

#print(length_count[1:])
    prob_to_fail = np.empty(2, dtype='float64', order='C')

    #Simulation
    prob_to_fail[0] = np.sum(length_count[number_of_prisoners//2+1:])/iterations*100.0
    #Theory
    prob_to_fail[1] = kahanSumOneOverN(number_of_prisoners//2+1, number_of_prisoners)*100.0
    print(f"Probablity to have chain longer than {number_of_prisoners//2} is:")
    print(f"  By simulation: {prob_to_fail[0]}%")
    print(f"  By theory    : {prob_to_fail[1]}%")
    print(f"  Difference   : {prob_to_fail[1]-prob_to_fail[0]}%")


#Check
    check = np.sum(np.multiply(np.arange(number_of_prisoners+1), length_count))
    if check != number_of_prisoners * iterations:
        print(f"Error detected! Expected value is {number_of_prisoners * iterations}, got {check}")

def kahanSumOneOverN(minimum,maximum):
    """
    Sum[1/i,{i,minimum,maximum}]
    Kahan Summation Algorithm: https://www.geeksforgeeks.org/kahan-summation-algorithm/
    """
    s = np.float128(0.0)
    c = np.float128(0.0)
    for i in reversed(range(minimum,maximum+1)):
        y = np.float128(1)/np.float128(i) - c
        t = s + y

        # Algebraically, c is always 0 when t is replaced by its
        # value from the above expression.But, when there is a loss,
        # the higher-order y is cancelled out by subtracting y from c and
        # all that remains is the lower-order error in c

        c = (t - s) - y
        s = t
    return s



if __name__ == '__main__':
    run_prisoners_simulation()
