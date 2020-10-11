def main():
	n=int(input())

	while n != -1:
		Times=[]
		miles=0

		for x in range(n):
			inputs=list(map(int,input().split()))
			Speed=inputs[0]
			Times.append(inputs[1])

			if x == 0 :
				miles+=(Speed*Times[x])
			else:
				miles+=(Speed*(Times[x]-Times[(x-1)]))
		print(miles,"miles")
		n=int(input())

if __name__ == '__main__':
	main()