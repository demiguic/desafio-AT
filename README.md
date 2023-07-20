 # Desafio AT

Os seguintes requisitos funcionais são necessários:

Expor uma interface web para permitir que o usuário configure:

 * os ativos da B3 a serem monitorados;
 * os parâmetros de túnel de preço
 * a periodicidade da checagem (em minutos) de cada ativo

O sistema deve obter e armazenar as cotações dos ativos cadastrados de alguma fonte pública qualquer, respeitando a periodicidade configurada por ativo.
A interface web deve permitir consultar os preços armazenados dos ativos cadastrados.
Enviar e-mail para o investidor sugerindo a compra sempre que o preço de um ativo monitorado cruzar o seu limite inferior do túnel, e sugerindo a venda sempre que o preço de um ativo monitorado cruzar o seu limite superior do túnel

 ## Guia Para Teste
 - [ ] Instale as dependências contidas no documento 'requirements.txt'
 - [ ] Inicie o servidor redis com o comando 'redis-server'
 - [ ] Em outro terminal entre no diretório que contem o arquivo 'manage.py'
 - [ ] Execute 'python manage.py runserver' para executar a aplicação
 - [ ] Em outro terminal execute o comando 'worker celery -A investor_app worker -l info --pool=solo' para iniciar o agendador de atividades.
