Descrição

Este projeto realiza a automação da consulta de processos no sistema IPS utilizando Selenium com Python.

A automação:

realiza login manual com CAPTCHA;
acessa a área de consulta de processos;
aplica filtros de palavras-chave e operadores lógicos;
filtra processos por período mensal;
executa as pesquisas automaticamente;
coleta o total de resultados encontrados;
atualiza automaticamente uma planilha .xlsx corporativa localizada em rede.
Tecnologias Utilizadas
Python
Selenium
OpenPyXL
ChromeDriver
Funcionalidades
Consulta automatizada de processos

O sistema percorre uma lista de tipos de processos previamente configurados, preenchendo automaticamente:

campos de resumo;
operadores lógicos;
período inicial e final da pesquisa.
Filtro mensal dinâmico

O usuário informa:

mês;
ano.

A automação gera automaticamente:

data inicial;
data final;
horário completo do período.
Atualização automática de planilha

Os resultados encontrados são gravados diretamente em uma planilha .xlsx.

A automação:

localiza a coluna correspondente ao mês;
encontra a linha do processo;
substitui o valor antigo pelo novo;
salva a planilha automaticamente.

Requisitos
Python 3.11+
Google Chrome instalado
ChromeDriver compatível com a versão do Chrome
Acesso à rede corporativa
Permissão de leitura e escrita na pasta da planilha
