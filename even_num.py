


def sumEvenAfterQueries(A, queries):
    sunm = []

    if (1 <= len(queries) <= 10000) and (1 <= len(A) <= 10000):
        for i in range(0, len(queries)):
            val = queries[i][0]
            index = queries[i][1]

            if (0 <= index < len(A)):
                num = A[index]

                A[index] = num + val
                result = 0

                for i in A:
                    if i % 2 == 0:
                        result += i
                sunm.append(result)
                result = 0
        return sunm


a = [1,2,3,4]
q = [[1,0],[-3,1],[-4,0],[2,3]]

print('correct: [8,6,2,4]', sumEvenAfterQueries(a,q))
