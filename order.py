def Pool_Order_IP(arg,i,Number,Pool_Order,IP_Address_Table,port):
    for j in range(arg,6,1):
        # print("Number is ",Number)
        # print("地点",IP_Address_Table[j][2])
        # print("运营商",IP_Address_Table[j][1])

        # print("Order is ",Pool_Order)
        # print("i is ",i)
        # print("j is :" ,j)
        # if Number == 12:
            # break
            # print("last_pool_order is ",Pool_Order)
            # return Pool_Order
        # print("__name__ is :",__name__)


        if IP_Address_Table[i][1] == 'CTC':
            if IP_Address_Table[j][1] == 'CTC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 2:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                # print("if CTC Number is ",Number)
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CUC' and IP_Address_Table[i][2] == IP_Address_Table[j][2] and Number == 4:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CUC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 6:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number+2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CMC' and IP_Address_Table[i][2] == IP_Address_Table[j][2] and Number == 8:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CMC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 10:
                Pool_Order = Pool_Order + IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number+1) +" } "
                # print("last_pool_order is ",Pool_Order)
                Number = Number+2
                return Pool_Order
                # Number = Number + 2
                # Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
        if IP_Address_Table[i][1] == 'CUC':
            if IP_Address_Table[j][1] == 'CUC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 2:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CTC' and IP_Address_Table[i][2] == IP_Address_Table[j][2] and Number == 4:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CTC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 6:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number+2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CMC' and IP_Address_Table[i][2] == IP_Address_Table[j][2] and Number == 8:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CMC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 10:
                Pool_Order = Pool_Order + IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order
                # Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
        if IP_Address_Table[i][1] == 'CMC':
            if IP_Address_Table[j][1] == 'CMC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 2:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CTC' and IP_Address_Table[i][2] == IP_Address_Table[j][2] and Number == 4:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CTC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 6:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number+2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CUC' and IP_Address_Table[i][2] == IP_Address_Table[j][2] and Number == 8:
                Pool_Order = Pool_Order + IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
            if IP_Address_Table[j][1] == 'CUC' and IP_Address_Table[i][2] != IP_Address_Table[j][2] and Number == 10:
                Pool_Order = Pool_Order + IP_Address_Table[j][4]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[j][3]+":"+ port +" { order "+ str(Number+1) +" } "
                Number = Number + 2
                return Pool_Order
                # Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
    # print(Pool_Order)
