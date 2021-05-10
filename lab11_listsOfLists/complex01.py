#!/usr/bin/env python3
list1 = ["cisco_nxos", "arista_eos", "cisco_ios"]
print(list1)
print(list1[1])

list2 = ["juniper"]
list1.extend(list2)
print(list1)
list3 = ["10.0.0.1", "10.0.0.2", "10.0.0.3"]
list1.append(list3)
print(list1)
print(list1[4][1])
        
