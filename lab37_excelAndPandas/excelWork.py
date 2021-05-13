#!/usr/bin/env python3

import pyexcel

print("test")
pyexcel.save_as(records=[{"id":1, "driver":3}], dest_file_name="ip_list.xls")
print("file was created successfully")
