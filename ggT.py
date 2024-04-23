def ggT(a, b):
    while b:
        a, b = b, a % b
    return a

print(ggT(2200,600)) #Trage hier die Zahlen ein, für die du den größten gemeinsamen Teiler suchst.