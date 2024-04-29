# https://leetcode.com/problems/baseball-game/

def calPoints(operations):
    """
    :type operations: List[str]
    :rtype: int
    """
    score =[]

    for i in range(len(operations)):
        if operations[i].lstrip("-").isnumeric():
            score.append(int(operations[i]))
        elif operations[i] == "C":
            score.pop()
        elif operations[i] == "D":
            score.append(score[-1] * 2)
        elif operations[i] == "+":
            score.append(score[-1] + score[-2])

    return sum(score)

print(calPoints(["5","-2","4","C","D","9","+","+"]))
