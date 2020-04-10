'''
ref : https://leetcode.com/discuss/interview-question/352458/
'''
def sol(A,B):
    A = A.split(',')
    B = B.split(',')
    A_minFreqs = {}
    B_minFreqs = {}
    sol

    for w in A:
        A_minFreqs[w] = w.count(min(w))

    for w in B:
        B_minFreqs[w] = w.count(min(w))
    def countWords(freq,Afreqs):
        count = 0
        for w in Afreqs:
            if freq > Afreqs[w]:
                count += 1
        return count

    result = [countWords(B_minFreqs[bW],A_minFreqs) for bW in B_minFreqs]

    return result

print(sol("abcd,aa,bd","aaa,aa"))
