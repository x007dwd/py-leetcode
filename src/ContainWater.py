class Solution(object):
    def bigger(self, A):
        flag = True
        B = ''
        T=A
        if len(A) > 1:
            if A[0] == '-':
                flag = False
                T = A[1:]
                if len(T) ==1:
                    return T
            elif A[0] == "+":
                T = A[1:]
        elif len(A) == 1:
            if A[0] > '0':
                B = '1'
                B += str(int(A[0])-1)
            return B
        else:
            return B

        acc = int(T[-1])
        idx = 2
        if len(T) > 1:
            for s in T[-2::-1]:
                if s > '9' or s < '0':
                    B = ''
                    return B
                if flag:
                    if s < '9' and acc > 0:
                        break
                    elif s == '9':
                        idx += 1
                    elif acc == 0:
                        idx += 1
                        acc += 1
                else:
                    if s > '0' and acc < (9 * idx):
                        break
                    elif acc < (9 * idx):
                        acc -= 1
                    else:
                        idx += 1
                acc += int(s)
            if flag:
                acc -= 1
            else:
                acc += 1
            for i in range(idx-1):
                if acc >= 9:
                    B += '9'
                    acc -= 9
                else:
                    B += str(acc)
                    acc =0
            if not flag:
                B =B[-1:]
        if idx < len(T):
            if flag:
                B += str(int(T[-idx]) + 1)
                B += T[-idx-1::-1]
            else:
                B += str(int(T[-idx]) - 1)
                B += T[-idx-1::-1]
        else:
            if flag:
                B += '1'
        if not flag:
            B += '-'
        return B[-1::-1]

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

if __name__ == '__main__':
    sol = Solution()
    # hei = [1,0,2,3,1,2]
    # sol.maxArea(hei)
    ss = '190'
    print  sol.bigger(ss)