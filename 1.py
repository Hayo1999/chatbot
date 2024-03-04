import g4f
def chatbot(content):
    response = g4f.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": content}],
    )
    return response
def savol(savol, mavzu=""):
    if mavzu=="tibbiyot":
        content = f"Savolim tibbiyot bilan bog'liq. {savol} ga tibbiyot yo'nalishida javob ber"
    elif mavzu == "dasturlash":
        content = f"Savolim dasturlash sohasi bilan bog'liq. {savol} ga dasturlash yo'nalishida javob ber"
    else:
        content = f"Ushbu savolga o'zbek tilida javob ber. Savol - {savol}"
    javob = chatbot(content)
    return javob
print(savol("Sikl"))
print(32*"*")
print(savol("Sikl", "tibbiyot"))
print(32*"*")
print(savol("sikl", "dasturlash"))
