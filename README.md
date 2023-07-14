 ## Desafio AT

Os seguintes requisitos funcionais são necessários:

Expor uma interface web para permitir que o usuário configure:

 * os ativos da B3 a serem monitorados;
 * os parâmetros de túnel de preço
 * a periodicidade da checagem (em minutos) de cada ativo

 O sistema deve obter e armazenar as cotações dos ativos cadastrados de alguma fonte pública qualquer, respeitando a periodicidade configurada por ativo.
A interface web deve permitir consultar os preços armazenados dos ativos cadastrados.
Enviar e-mail para o investidor sugerindo a compra sempre que o preço de um ativo monitorado cruzar o seu limite inferior do túnel, e sugerindo a venda sempre que o preço de um ativo monitorado cruzar o seu limite superior do túnel