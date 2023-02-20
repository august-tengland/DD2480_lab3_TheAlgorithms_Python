import math


def convert(number: int) -> str:
    """
    Given a number return the number in words.

    # >>> convert(123)
    'OneHundred,TwentyThree'
    """
    reached_branches = []
    if number == 0:
        words = "Zero"
        reached_branches.append("11T")
        # return words
        return reached_branches
    else:
        reached_branches.append("11F")
        digits = math.log10(number)
        digits = digits + 1
        singles = {}
        singles[0] = ""
        singles[1] = "One"
        singles[2] = "Two"
        singles[3] = "Three"
        singles[4] = "Four"
        singles[5] = "Five"
        singles[6] = "Six"
        singles[7] = "Seven"
        singles[8] = "Eight"
        singles[9] = "Nine"

        doubles = {}
        doubles[0] = ""
        doubles[2] = "Twenty"
        doubles[3] = "Thirty"
        doubles[4] = "Forty"
        doubles[5] = "Fifty"
        doubles[6] = "Sixty"
        doubles[7] = "Seventy"
        doubles[8] = "Eighty"
        doubles[9] = "Ninety"

        teens = {}
        teens[0] = "Ten"
        teens[1] = "Eleven"
        teens[2] = "Twelve"
        teens[3] = "Thirteen"
        teens[4] = "Fourteen"
        teens[5] = "Fifteen"
        teens[6] = "Sixteen"
        teens[7] = "Seventeen"
        teens[8] = "Eighteen"
        teens[9] = "Nineteen"

        placevalue = {}
        placevalue[2] = "Hundred,"
        placevalue[3] = "Thousand,"
        placevalue[5] = "Lakh,"
        placevalue[7] = "Crore,"

        temp_num = number
        words = ""
        counter = 0
        digits = int(digits)
        while counter < digits:
            current = temp_num % 10
            reached_branches.append("62T")
            if counter % 2 == 0:
                reached_branches.append("64T")
                addition = ""
                if counter in placevalue.keys() and current != 0:
                    reached_branches.append("66T")
                    addition = placevalue[counter]
                else:
                    reached_branches.append("66F")
                if counter == 2:
                    reached_branches.append("68T")
                    words = singles[current] + addition + words
                else:
                    reached_branches.append("68F")
                    if counter == 0:
                        reached_branches.append("70T")
                        if ((temp_num % 100) // 10) == 1:
                            reached_branches.append("71T")
                            words = teens[current] + addition + words
                            temp_num = temp_num // 10
                            counter += 1
                        else:
                            reached_branches.append("71F")
                            words = singles[current] + addition + words

                    else:
                        reached_branches.append("70F")
                        words = doubles[current] + addition + words

            else:
                reached_branches.append("64F")
                if counter == 1:
                    reached_branches.append("82T")
                    if current == 1:
                        reached_branches.append("83T")
                        words = teens[number % 10] + words
                    else:
                        reached_branches.append("83F")
                        addition = ""
                        if counter in placevalue.keys():
                            reached_branches.append("87T")
                            addition = placevalue[counter]
                        else:
                            reached_branches.append("87F")
                            words = doubles[current] + addition + words
                else:
                    reached_branches.append("82F")
                    addition = ""
                    if counter in placevalue.keys():
                        reached_branches.append("92T")
                        if current == 0 and ((temp_num % 100) // 10) == 0:
                            reached_branches.append("93T")
                            addition = ""
                        else:
                            reached_branches.append("93F")
                            addition = placevalue[counter]
                    else:
                        reached_branches.append("92F")
                    if ((temp_num % 100) // 10) == 1:
                        reached_branches.append("97T")
                        words = teens[current] + addition + words
                        temp_num = temp_num // 10
                        counter += 1
                    else:
                        reached_branches.append("97F")
                        words = singles[current] + addition + words
            counter += 1
            temp_num = temp_num // 10
    reached_branches.append("62F")
    reached_branches = list(set(reached_branches))
    # return words
    return reached_branches


if __name__ == "__main__":  # pragma: no cover
    list1 = convert(123)
    list_to_calculate = list(set(list1))
    branch_coverage = len(list_to_calculate)/26
    print(branch_coverage)
