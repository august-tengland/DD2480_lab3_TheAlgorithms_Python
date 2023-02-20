import math


def convert(number: int) -> str:
    """
    Given a number return the number in words.

    # >>> convert(123)
    'OneHundred,TwentyThree'
    # >>> convert(0)
    'Zero'
    # >>> convert(113)
    'OneHundred,Thirteen'
    # >>> convert(13000)
    'ThirteenThousand,'
    # >>> convert(100010)
    'OneLakh,Ten'
    """

    reached_branches = []

    if number == 0:
        words = "Zero"
        reached_branches.append("11T")
        # return words + ''.join(reached_branches)
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
        counter = 0  # 记现在是第几位，位数为counter+1
        digits = int(digits)
        while counter < digits:
            reached_branches.append("62T")
            current = temp_num % 10  # 取目前最小一位
            if counter % 2 == 0:  # counter表示个 百 10千 10lakh 10crore时
                reached_branches.append("64T")
                addition = ""
                if counter in placevalue.keys() and current != 0:  # 最小一位不为零并且counter有对应的placevalue即百 千 lakh crore时
                    reached_branches.append("66T")
                    addition = placevalue[counter]
                else:
                    reached_branches.append("66F")
                if counter == 2:  # counter正好是百
                    reached_branches.append("68T")
                    words = singles[current] + addition + words
                else:
                    reached_branches.append("68F")
                    if counter == 0:  # counter正好是个
                        reached_branches.append("70T")
                        if ((temp_num % 100) // 10) == 1:  # 正好是十几
                            reached_branches.append("71T")
                            words = teens[current] + addition + words
                            temp_num = temp_num // 10
                            counter += 1  # 多加一位，因为十位数不用算了
                        else: # 数个数
                            reached_branches.append("71F")
                            words = singles[current] + addition + words

                    else:  # 剩下几十千，几十lakh，几十crore的情况了
                        reached_branches.append("70F")
                        words = doubles[current] + addition + words

            else:  # counter表示个 百 10千 10lakh 10crore以外的位数时
                reached_branches.append("64F")
                if counter == 1: # counter正好是十
                    reached_branches.append("82T")
                    if current == 1:  # 十几
                        reached_branches.append("83T")
                        words = teens[number % 10] + words
                    else: # 几十几
                        reached_branches.append("83F")
                        addition = ""
                    if counter in placevalue.keys():  # counter有对应的placevalue
                        reached_branches.append("87T")
                        addition = placevalue[counter]
                    else:
                        reached_branches.append("87F")
                        words = doubles[current] + addition + words
                else:
                    reached_branches.append("82F")
                    addition = "" # 剩下所有位数
                    if counter in placevalue.keys():  # counter有对应的placevalue
                        reached_branches.append("92T")
                        if current == 0 and ((temp_num % 100) // 10) == 0:
                            reached_branches.append("93T")# 目前最后两位正好是零零
                            addition = ""
                        else:
                            reached_branches.append("93F")
                            addition = placevalue[counter]
                    else:
                        reached_branches.append("92F")
                    if ((temp_num % 100) // 10) == 1: # 正好是十几
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
    #  return words + ','.join(reached_branches)
    return reached_branches

if __name__ == "__main__":  # pragma: no cover
    """word1 = convert(123)
    print(word1)
    word2 = convert(0)  # C: 12, 13 B: 15-17
    print(word2)
    word3 = convert(113)  # C: 72-74 B: 86-89
    print(word3)
    word4 = convert(13000)  # C: 91-93, 95-101 B: 115-119 122-132
    print(word4)
    word5 = convert(100010)  # C: 79, 94 B: 95-96, 120-121, 133-134
    print(word5)"""

    list1 = convert(123)
    list2 = convert(0)
    list3 = convert(113)
    list4 = convert(13000)
    list5 = convert(100010)
    list_to_calculate = list(set(list1 + list2 + list3 + list4 + list5))
    branch_coverage = len(list_to_calculate)/26
    print(branch_coverage)
