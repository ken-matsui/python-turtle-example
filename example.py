from turtle import *

def calc(n_):
	for i in range(n_):
		forward(100)
		left(360 / n_)

def main():
	for i in range(3, 12):
		calc(i)
	raw_input()

if __name__ == '__main__':
	main()