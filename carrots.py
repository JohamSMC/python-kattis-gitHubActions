import os

def main():
	output=input().split()[1]
	print(output)	
	
if __name__ == '__main__':
	path_file = os.path.dirname(os.path.abspath(__file__))
	main()	