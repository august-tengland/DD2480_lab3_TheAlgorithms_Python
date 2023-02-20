from __future__ import annotations

from collections.abc import Sequence
from typing import Literal


def compare_string(string1: str, string2: str) -> str | Literal[False]: #pragma: no cover
    """
    >>> compare_string('0010','0110')
    '0_10'

    >>> compare_string('0110','1101')
    False
    """
    list1 = list(string1)
    list2 = list(string2)
    count = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count += 1
            list1[i] = "_"
    if count > 1:
        return False
    else:
        return "".join(list1)


def check(binary: list[str]) -> list[str]: #pragma: no cover
    """
    >>> check(['0.00.01.5'])
    ['0.00.01.5']
    """
    pi = []
    while True:
        check1 = ["$"] * len(binary)
        temp = []
        for i in range(len(binary)):
            for j in range(i + 1, len(binary)):
                k = compare_string(binary[i], binary[j])
                if k is False:
                    check1[i] = "*"
                    check1[j] = "*"
                    temp.append("X")
        for i in range(len(binary)):
            if check1[i] == "$":
                pi.append(binary[i])
        if len(temp) == 0:
            return pi
        binary = list(set(temp))


def decimal_to_binary(no_of_variable: int, minterms: Sequence[float]) -> list[str]: #pragma: no cover
    """
    >>> decimal_to_binary(3,[1.5])
    ['0.00.01.5']
    """
    temp = []
    for minterm in minterms:
        string = ""
        for _ in range(no_of_variable):
            string = str(minterm % 2) + string
            minterm //= 2
        temp.append(string)
    return temp


def is_for_table(string1: str, string2: str, count: int) -> bool: #pragma: no cover
    """
    >>> is_for_table('__1','011',2)
    True

    >>> is_for_table('01_','001',1)
    False
    """
    list1 = list(string1)
    list2 = list(string2)
    count_n = 0
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            count_n += 1
    return count_n == count

#create a list called selection_list with 17 elements with the value false
selection_list = [False] * 31

def selection(chart: list[list[int]], prime_implicants: list[str]) -> list[str]:
    """
    >>> selection([[1]],['0.00.01.5'])
    ['0.00.01.5']

    >>> selection([[1]],['0.00.01.5'])
    ['0.00.01.5']

    >>> selection([[0]],['0.00.01.5'])
    []

    >>> selection([[1],[1]],['0.00.01.5'])
    ['0.00.01.5']
    """
    temp = []
    select = [0] * len(chart)
    for i in range(len(chart[0])):
        selection_list[0] = True
        count = 0
        rem = -1
        for j in range(len(chart)):
            selection_list[1] = True
            if chart[j][i] == 1:
                count += 1
                rem = j
                selection_list[2] = True
            else:
                selection_list[3] = True
        else:
            selection_list[4] = True
        if count == 1:
            select[rem] = 1
            selection_list[5] = True
        else:
            selection_list[6] = True
    else:
        selection_list[7] = True
    for i in range(len(select)):
        selection_list[8] = True
        if select[i] == 1:
            selection_list[9] = True
            for j in range(len(chart[0])):
                selection_list[10] = True
                if chart[i][j] == 1:
                    selection_list[11] = True
                    for k in range(len(chart)):
                        selection_list[12] = True
                        chart[k][j] = 0
                    else:
                        selection_list[13] = True
                else:
                    selection_list[14] = True
            else:
                selection_list[15] = True
            temp.append(prime_implicants[i])
        else:
            selection_list[16] = True
    else:
        selection_list[17] = True
    while True:
        max_n = 0
        rem = -1
        count_n = 0
        selection_list[18] = True
        for i in range(len(chart)):
            count_n = chart[i].count(1)
            selection_list[19] = True
            if count_n > max_n:
                max_n = count_n
                rem = i
                selection_list[20] = True
            else:
                selection_list[21] = True
        else:
            selection_list[22] = True

        if max_n == 0:
            selection_list[23] = True
            return temp
        else:
            selection_list[24] = True
        temp.append(prime_implicants[rem])

        for i in range(len(chart[0])):
            selection_list[25] = True
            if chart[rem][i] == 1:
                selection_list[26] = True
                for j in range(len(chart)):
                    chart[j][i] = 0
                    selection_list[27] = True
                else:
                    selection_list[28] = True
            else:
                selection_list[29] = True
        else:
            selection_list[30] = True


def prime_implicant_chart(
    prime_implicants: list[str], binary: list[str]
) -> list[list[int]]: #pragma: no cover
    """
    >>> prime_implicant_chart(['0.00.01.5'],['0.00.01.5'])
    [[1]]
    """
    chart = [[0 for x in range(len(binary))] for x in range(len(prime_implicants))]
    for i in range(len(prime_implicants)):
        count = prime_implicants[i].count("_")
        for j in range(len(binary)):
            if is_for_table(prime_implicants[i], binary[j], count):
                chart[i][j] = 1

    return chart


def main() -> None: #pragma: no cover
    no_of_variable = int(input("Enter the no. of variables\n"))
    minterms = [
        float(x)
        for x in input(
            "Enter the decimal representation of Minterms 'Spaces Separated'\n"
        ).split()
    ]
    binary = decimal_to_binary(no_of_variable, minterms)

    prime_implicants = check(binary)
    print("Prime Implicants are:")
    print(prime_implicants)
    chart = prime_implicant_chart(prime_implicants, binary)

    essential_prime_implicants = selection(chart, prime_implicants)
    print("Essential Prime Implicants are:")
    print(essential_prime_implicants)


if __name__ == "__main__": #pragma: no cover
    import doctest
    selection([[1]],['0.00.01.5'])
    selection([[1]],['0.00.01.5'])
    selection([[0]],['0.00.01.5']) #test should succeed if this output is an empty list
    selection([[1],[1]],['0.00.01.5']) #test should succeed if the output is ['0.00.01.5']
    doctest.testmod()
    print(selection_list)
    summ = 0
    for i in range(len(selection_list)):
        if(selection_list[i] == True):
            summ += 1
        else:
            continue

    percentage_branch_coverage = (summ/len(selection_list))*100
    print(percentage_branch_coverage)
    #main()
    
