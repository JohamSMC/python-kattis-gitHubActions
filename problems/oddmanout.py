def main():
	numberCases = int(input())
	for case in range(numberCases):
		numberGuests = int(input())
		invitationCodes= list(input().split(" "))
		auxInvitationCodes = " ".join(invitationCodes)+" "
		for i in range((len(invitationCodes)//2)+1):
			if auxInvitationCodes.count(invitationCodes[i]+" ") == 1:
				print("Case #",(case+1),": ",invitationCodes[i],sep="")
				break
			if auxInvitationCodes.count(invitationCodes[len(invitationCodes)-(i+1)]+" ") == 1:
				print("Case #",(case+1),": ",invitationCodes[len(invitationCodes)-(i+1)],sep="")

if __name__ == '__main__':
	main()