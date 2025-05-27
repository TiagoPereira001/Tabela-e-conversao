from flask import Flask, render_template, request

app = Flask(__name__)

# Caio Dias
# Tiago Pereira
# Mário Eduardo

@app.route("/")
def index():
    return render_template("index.html")
#menu
@app.route("/menu", methods=["POST"])
def menu():
    menu_ativo = request.form.get("menu", "").strip()
    if menu_ativo == "Tabela de Gray":
        return render_template("tabela_de_gray.html")
    elif menu_ativo == "hexadecimal para decimal":
        return render_template("hexadecimal_para_decimal.html")
    elif menu_ativo == "decimal para hexadecimal":
        return render_template("decimal_para_hexadecimal.html")
    elif menu_ativo == "decimal para binario":
        return render_template("decimal_para_binario.html")
    else:
        return "erro"



@app.route("/decimal_para_binario", methods=["POST"])
def decimal_para_binario():
    numero = int(request.form.get("numero", 0))
    largura = int(request.form.get("largura", 0))
    binario = ''
    n = numero
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    while len(binario) < largura:
        binario = '0' + binario
    if binario == '':
        binario = '0'
    return render_template("resultado_decimal_para_binario.html", decimal=numero, binario=binario)

# Decimal para hexadecimal
@app.route("/decimal_para_hexadecimal", methods=["POST"])
def decimal_para_hexadecimal():
    n = int(request.form.get("numero", 0))  
    digitoshexa = '0123456789ABCDEF'
    hexadecimal = ''
    if n == 0:
        return '0'
    while n > 0:
        hexadecimal = digitoshexa[n % 16] + hexadecimal
        n = n // 16
    return render_template("resultado_decimal_para_hexadecimal.html", hexadecimal=hexadecimal)

# Hexadecimal para decimal
@app.route("/hexadecimal_para_decimal", methods=["POST"])
def hexadecimal_para_decimal():
    h = request.form.get("hexadecimal", "")
    digitoshexa = '0123456789ABCDEF'
    h = h.upper()
    decimal = 0
    for c in h:
        decimal = decimal * 16 + digitoshexa.index(c)
    return render_template("resultado_hexadecimal_para_decimal.html", hexadecimal=h, decimal=decimal)

#tabela gray
@app.route("/tabela_de_gray", methods=["POST"])
def tabela_de_gray():
    n_bits = int(request.form["bits"])
    digitoshexa = '0123456789ABCDEF'

    def decimal_para_binario(n, largura=0):
        binario = ''
        while n > 0:
            binario = str(n % 2) + binario
            n = n // 2
        while len(binario) < largura:
            binario = '0' + binario
        return binario if binario else '0'

    tabela = []
    for i in range(2 ** n_bits):
        binario = decimal_para_binario(i, n_bits)
        gray = i ^ (i >> 1)
        gray_bin = decimal_para_binario(gray, n_bits)
        hexadecimal = ''
        n = i
        if n == 0:
            hexadecimal = '0'
        else:
            while n > 0:
                hexadecimal = digitoshexa[n % 16] + hexadecimal
                n = n // 16
        tabela.append({
            "decimal": i,
            "binario": binario,
            "gray": gray_bin,
            "hexadecimal": hexadecimal
        })

    return render_template("resultado_tabela_de_gray.html", tabela=tabela, bits=n_bits)
if __name__ == "__main__":
    app.run(debug=True)