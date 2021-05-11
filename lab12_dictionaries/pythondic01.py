#!/usr/bin/env python3
switch = {"hostname":"sw1", "ip":"10.0.0.1", "version":"1.2", "vendor": "cisco"}
print(switch["hostname"])
print(switch["ip"])

## print(switch["lynx"])

## request a fake key with get()
print("First test- .get()")
print(switch.get("lynx"))

print("second test")
print(switch.get("lynx", "THE KEY IS IN ANOTHER CASTLE!"))

print("Third test")
print(switch.get("version"))

## other functions of dictionaries
print("sixth test - .pop()")
switch.pop("version")
print(switch.keys())
print(switch.values())

print("seventh test - add a value")
switch["adminlogin"] = "karl08"
print(switch.keys())
print(switch.values())

print("seventh test - add a value")
switch["password"] = "karl08"
print(switch.keys())
print(switch.values())
