import re

with open("dicionario_medico.txt", "r", encoding="utf8") as file:
    texto = file.read()

texto = re.sub(r"[^\f]\n\f", r"\n", texto)  #retirar as quebras de página do texto

texto = re.sub(r"\n\n","\n\n@",texto) #marca com um @ cada conceito

texto = re.sub(r"\n\n(.+)",r"\n\n@\1",texto)

def limpa_descricao (descricao): #Limpa os \n que aparecem a meio do texto
    descricao = descricao.strip()
    descricao = re.sub(r"\n", " ", descricao)
    return descricao

#Extrair conceitos

conceitos_raw = re.findall(r'@(.*)\n([^@]*)',texto)

conceitos = [(designacao,limpa_descricao(descricao)) for designacao, descricao in conceitos_raw]

#Gerar o HTML

def gerar_html (conceitos):
    html_header = f"""
            <!DOCTYPE html>
                <head>
                <meta charset="UTF-8">
                </head>
                <body>
                <h3>Dicionário de Conceitos Médicos</h3>
                <p>Este dicionário foi desenvolvido para a aula de PLNEB 2024/2025</p>"""
    html_conceitos = ""  
    for designacao, descricao in conceitos:
        html_conceitos += f"""
                    <div>
                    <p><b>{designacao}</b></p>
                    <p>{descricao}</p>
                    </div>
                    <hr/>
                """        
    html_footer = """                          
                </body>
            </html> """
    return html_header + html_conceitos + html_footer

html = gerar_html(conceitos)
with open("dicionario_medico.html", "w", encoding="utf8") as file_out:
    file_out.write(html)