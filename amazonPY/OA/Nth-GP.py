'''
Given 2nd and 3rd term of a Geometric Progression find the nth term of it and round it off upto 3 decimal places.

we have to complete the following function:

char* nthTerm(double input1, double input2, int input3) {
	//your code here
}
input1 = 2nd term and input2 = 3rd term and both are between -2 to 2.
input3 = nth term to be find and can be upto 100.
I was unable to convert the result from double to array of char in the time limits :( Need help. The test was on Mettle platform and i think i was unable to use to_string(), round() etc. Although pow() function working fine.

e.g input1 = 1, input2 = 2, input3 = 4
      output = 4.0

'''
def sol(n1,n2,n):

    n1 = n1 * pow(n2,n-2)

    return "{0:.2f}".format(n1)

print(sol(1,2,4))
