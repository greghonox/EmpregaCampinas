from bs4 import BeautifulSoup
import requests
import re

class Emprego:

    def limpar(self, txt):
        return str(txt).replace("\n", "").replace("\t", "").replace("\b", "")

    def cargo(self, txt):
        return str(txt).replace(" ","+")

    def pegar_vaga(self):
        for vaga in self.pagina.findAll(class_="thumbnail"):
            try:
                self.destalhes_vaga(vaga["href"])
            except Exception as erro:
                break

    vagas = []
    def destalhes_vaga(self, url):
        link = url
        pagina = BeautifulSoup(requests.get(url).text, "lxml")
        html = pagina.find(class_="col-lg-8 conteudo-vaga")
        lista = ["Clientes", "Sálario", "Beneficio", "Responsabilidade", "Requisitos", "Contato"]

        detalhes = []
        detalhes.append(self.limpar(html.h1.span)[17:-16])

        for contagem, topico in enumerate(html.findAll("p")):
            if(contagem == 2 or contagem == 3 or contagem == 4 or contagem == 5
               or contagem == 6):
                    detalhes.append(topico.text)
            elif(contagem >= 7):
                try:
                    self.validar_email_telefone(detalhes, topico.text)
                except Exception as erro:
                    print("SEM CONTATO", erro)
        vagas = [ detalhes[0], detalhes[3][8:], detalhes[4][11:], detalhes[1][19:],
                     detalhes[2][12:], detalhes[6], link ]
        self.vagas.append(vagas)

    def validar_email_telefone(self, detalhes, txt):
        valida = ["^([1-9]{2}) 9[7-9]{1}[0-9]{3}-[0-9]{4}$",
                  "[a-zA-Z0-9]+[a-zA-Z0-9_.-]+@{1}[a-zA-Z0-9_.-]*\\.+[a-z]{2,4}"]
        for conta in range(2):
            try:
                detalhes.append(re.findall(valida[conta], txt)[0])
            except Exception as erro:
                # print("Erro:",erro)
                pass

    def navegar(self, cargo, contador):
        url = "http://empregacampinas.com.br/page/{}/?s={}".format(contador, self.cargo(cargo))
        self.pagina = BeautifulSoup(requests.get(url).text, "lxml")
        self.pegar_vaga()

    def __str__(self):
        return self.pagina.text
#
# contador = 0
# emprego = Emprego()
# while True:
#     emprego.navegar("python", contador)
#     if(len(emprego.vagas) <= 0):
#         print("ACABOU A BUSCA!")
#         break
#     emprego.vagas.clear()
#     contador += 1
# print(Emprego().validar_email_telefone(1, 'email para mariana.cipriano@sofist.com.br"'))
