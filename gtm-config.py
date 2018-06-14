from prettytable import PrettyTable
from order import Pool_Order_IP

print("下面请输入，相应的IP地址")
#while True:
HF_CTC=['DC_CT','CTC','HF']
HF_CMC=['DC_CMC','CMC','HF']
HF_CNC=['DC_CU','CUC','HF']
for i in range(1,3,1):
    print("合肥电信",i)
    IP_address=input()
    HF_CTC.append(IP_address)
for i in range(1,3,1):
    print("合肥移动",i)
    IP_address=input()
    HF_CMC.append(IP_address)
for i in range(1,3,1):
    print("合肥电信",i)
    IP_address=input()
    HF_CNC.append(IP_address)

SH_CTC=['DC-SPDB-CTC','CTC','SH']
SH_CMC=['DC-SPDB-CMC','CMC','SH']
SH_CNC=['DC-SPDB-CUC','CUC','SH']
for i in range(1,3,1):
    print("上海电信",i)
    IP_address=input()
    SH_CTC.append(IP_address)
for i in range(1,3,1):
    print("上海移动",i)
    IP_address=input()
    SH_CMC.append(IP_address)
for i in range(1,3,1):
    print("上海电信",i)
    IP_address=input()
    SH_CNC.append(IP_address)



# print("合肥电信:",HF_CTC)
# print("合肥移动:",HF_CMC)
# print("合肥联通:",HF_CNC)

# print("上海电信:",SH_CTC)
# print("上海移动:",SH_CMC)
# print("上海联通:",SH_CNC)
# IP_Address_Table=[HF_CTC]
IP_Address_Table=[HF_CTC,HF_CMC,HF_CNC,SH_CTC,SH_CMC,SH_CNC]
# IP_Address_Table=IP_Address_Table.append()
print("表格",IP_Address_Table)

# HF_IP_Address_Table=PrettyTable()
tab=["DataCenter","运营商","地点","IP地址线路1","IP地址线路2"]




Total_IP_Address_Table=PrettyTable()
Total_IP_Address_Table.add_row(tab)
Total_IP_Address_Table.add_row(HF_CTC)
Total_IP_Address_Table.add_row(HF_CMC)
Total_IP_Address_Table.add_row(HF_CNC)
Total_IP_Address_Table.add_row(SH_CTC)
Total_IP_Address_Table.add_row(SH_CMC)
Total_IP_Address_Table.add_row(SH_CNC)
# print("合肥地址",HF_IP_Address_Table)

print("IP地址列表",Total_IP_Address_Table)

# print("表格",IP_Address_Table)
print("创建servers，请输入业务的名字：例如，g/wap")
static_Servers_Name=input()
print("业务端口port：")
port=input()
for i in range(0,6,1):
    if IP_Address_Table[i][2] == 'HF':
        for j in range(1,3,1):
            Servers_Name="GH_"+static_Servers_Name+"_"+IP_Address_Table[i][j]+str(j)+"_HFI"
            VS_name="VS_"+static_Servers_Name+"_"+IP_Address_Table[i][j]+str(j)+"_HFI_"+port
            k=2+j
            man="create gtm server "+Servers_Name+"  product generic-host addresses add { "+IP_Address_Table[i][k]+" } datacenter "+IP_Address_Table[i][0]+" virtual-servers add { "+IP_Address_Table[i][k]+":"+port+" { name "+VS_name+" } }"
            print(man)
            Servers_Name=''
            VS_name=""
            k=0
        #第三列IP地址列表
    else:
        for j in range(1,3,1):
            Servers_Name="GH_"+static_Servers_Name+"_"+IP_Address_Table[i][j]+str(j)
            VS_name="VS_"+static_Servers_Name+"_"+IP_Address_Table[i][j]+str(j)+"_"+port
            k=2+j
            man="create gtm server "+Servers_Name+" product generic-host addresses add { "+IP_Address_Table[i][k]+" } datacenter "+IP_Address_Table[i][0]+" virtual-servers add { "+IP_Address_Table[i][k]+":"+port+" { name "+VS_name+" } }"
            print(man)
            Servers_Name=''
            VS_name=""
            k=0

# 先1后2，if 为上海 SH CMC 上海移动先2后1
Pool_Name = "P_"
for i in range(0,6,1):
        Next_Pool_Name = "P_"+static_Servers_Name+"_"+IP_Address_Table[i][1]+"_"+IP_Address_Table[i][2]
        Pool_Name = Next_Pool_Name
        print(Pool_Name)
        Number = 0
        Pool_Order = ""
        Pool_Order = Pool_Order + IP_Address_Table[i][3]+":"+ port +" { order "+ str(Number) +" } "+ IP_Address_Table[k][3]+":"+ port +" { order "+ str(Number+1) +" } "
        Number = Number+2

        man=Pool_Order_IP(0,i,Number,Pool_Order,IP_Address_Table,port)
        # print("man is ",man)
        man ="create gtm pool "+Pool_Name+" monitor tcp load-balancing-mode global-availability alternate-mode none fallback-mode none members add { "+ man +"}"
        print(man)
