import random


def f_x(r):

	t = (x * r) % N

	return t > N//2 


def reconstruct():

	left = 0
	right = N - 1

	i = 0

	while (left != right):

		r_i = 2 ** i

		mid = (left + right) // 2

		if ((mid * r_i) % N > (N // 2)):

			pivot = mid

		else:

			pivot = mid + 1

		a = f_x(r_i)

		if (a == 0):

			right = pivot - 1

		else:

			left = pivot

		i = i + 1 

	return left	



def main():

	tests = 1000000

	for i in range(tests):

		global x

		global N

		N = random.randint(2, 100000000000)

		x = random.randint(0, N - 1)

		res = reconstruct()

		assert(x == res)

		print ("Test passed #", i, "\tN = ", N, "\tx = ", x, "\tres = ", res)



if __name__ == "__main__":

	main()
