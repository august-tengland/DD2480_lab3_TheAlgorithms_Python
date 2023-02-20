singles = {
    0: "",
    1: "One",
    2: "Two",
    3: "Three",
    4: "Four",
    5: "Five",
    6: "Six",
    7: "Seven",
    8: "Eight",
    9: "Nine"
}

doubles = {
    0: "",
    2: "Twenty",
    3: "Thirty",
    4: "Forty",
    5: "Fifty",
    6: "Sixty",
    7: "Seventy",
    8: "Eighty",
    9: "Ninety"
}

teens = {
    0: "Ten",
    1: "Eleven",
    2: "Twelve",
    3: "Thirteen",
    4: "Fourteen",
    5: "Fifteen",
    6: "Sixteen",
    7: "Seventeen",
    8: "Eighteen",
    9: "Nineteen"
}

place_value = {
    2: "Hundred,",
    3: "Thousand,",
    5: "Lakh,",
    7: "Crore,"
}


def convert_when_even_digit(temp_num: int, counter: int, current: int, words: str):
    addition = ""
    if counter in place_value.keys() and current != 0:
        addition = place_value[counter]
    if counter == 2:
        words = singles[current] + addition + words
    elif counter == 0:
        if ((temp_num % 100) // 10) == 1:
            words = teens[current] + addition + words
            temp_num = temp_num // 10
            counter += 1
        else:
            words = singles[current] + addition + words

    else:
        words = doubles[current] + addition + words

    return temp_num, counter, words


def convert_when_odd_digit(temp_num: int, counter: int, current: int, words: str):
    if counter == 1:
        words = doubles[current] + words
    else:
        addition = ""
        if counter in place_value.keys():
            if current == 0 and ((temp_num % 100) // 10) == 0:
                addition = ""
            else:
                addition = place_value[counter]
        if ((temp_num % 100) // 10) == 1:
            words = teens[current] + addition + words
            temp_num = temp_num // 10
            counter += 1
        else:
            words = singles[current] + addition + words
    return temp_num, counter, words


def convert(number: int) -> str:
    """
    Given a number return the number in words.

     convert(123)
    'OneHundred,TwentyThree'
     convert(0)
    'Zero'
     convert(113)
    'OneHundred,Thirteen'
     convert(13000)
    'ThirteenThousand,'
     convert(100010)
    'OneLakh,Ten'
    """
    if number == 0:
        return "Zero"
    digits = len(str(number))
    words = ""
    temp_num = number
    counter = 0
    while counter < digits:
        current = temp_num % 10
        if counter % 2 == 0:
            tuple1 = convert_when_even_digit(temp_num, counter, current, words)
            temp_num = tuple1[0]
            counter = tuple1[1]
            words = tuple1[2]
        else:
            tuple2 = convert_when_odd_digit(temp_num, counter, current, words)
            temp_num = tuple2[0]
            counter = tuple2[1]
            words = tuple2[2]
        counter += 1
        temp_num = temp_num // 10
    return words

if __name__ == "__main__":
    word1 = convert(123)
    print(word1)
    word2 = convert(0)
    print(word2)
    word3 = convert(113)
    print(word3)
    word4 = convert(13000)
    print(word4)
    word5 = convert(100010)
    print(word5)