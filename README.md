## EiPrice Test WebScrapping

### Nessa solução utilizei python para realizar a buscar de preços e produtos no site: shopper.com.br
### Para rodar o projeto:

* acesse o site
* crie uma conta
* Logue e acesse essa página: https://unica.shopper.com.br/shop/#bemvindo
* Aperte F12 no seu navegador
* Vá para a aba "Network" ou "Rede"
* Selecione a aba "Fetch/XHR"
* Recarregue a página
* Selecione a requisição "departments"
* Ao lado direito aparecerá informações da requisição procure por "authorization"
* Copie o valor inteiro, será parecido com "Bearer asduhasfhgadv138vh93vb13h9...."
* Acesse o projeto python no arquivo: "python-webscraping\scripts\ShopperWebScraping.py"
* Substitua o valor da linha 13 ~ 15
* Se certifique que tenha o docker instalado
* Abra o terminal e execute: docker-compose build
* Ao concluir execute: docker-compose up -d

#### A documentação swagger estará disponível no endereço: http://127.0.0.1:8080/docs

##### Para iniciar o processo de coleta de dados siga os seguintes passos:
* Abra o endereço no navegador: http://127.0.0.1:8080/docs
* Ou execute a seguinte chamada no curl: "curl -X POST http://127.0.0.1:8080/scripts/shopper/start"
* No swagger execute a opção POST apontando para o endereço "/scripts/shopper/start"

##### Para validar o resultado que foi salvo é possível pelo PgAdmin ou pelo swagger
* Abra o endereço no navegador: http://127.0.0.1:8080/docs
* Ou execute a seguinte chamada no curl: "curl http://127.0.0.1:8080/api/assortment"
* Ou execute a seguinte chamada no curl substituindo "{product_name}" pelo nome do produto ou parte do nome: "curl http://127.0.0.1:8080/api/assortment/product/{product_name}"
* Ou execute a seguinte chamada no curl substituindo "{department_name}" pelo nome do departamento ou parte do nome: "curl http://127.0.0.1:8080/api/assortment/product/{department_name}"