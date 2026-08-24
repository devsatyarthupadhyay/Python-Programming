marks = {
    "Satyarth":"100",
    "Lakshita":"99",
    "Anjal":"90",
    "Saksham":"85"
}
print(marks)
print(marks["Satyarth"])
print(marks.items()) 

print(marks.keys())

marks.update({"Lakshita":"100"})
print(marks)

print(marks.get("Lakshita"))