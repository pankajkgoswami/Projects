import sys
in_data = [int(x) for x in sys.argv[1:]]
no_of_test_cases = in_data[0]
SeatNo=in_data[1:]

#no_of_test_cases = int(input())
#SeatNo=[]
seatLoc=['SU','LB','MB','UB','LB','MB','UB','SL']
#for i in range(no_of_test_cases):
#    data = int(input())
#    SeatNo.append(data)

for i in range(no_of_test_cases):
    
    SeatPos = SeatNo[i]%8
    
    if SeatPos==0:
        PairSeat=SeatNo[i]-1
    elif SeatPos==7:
        PairSeat=SeatNo[i]+1
    else:
        if SeatPos>3:
            PairSeat=SeatNo[i]-3
        else:
            PairSeat=SeatNo[i]+3
    print(str(PairSeat)+seatLoc[PairSeat%8])