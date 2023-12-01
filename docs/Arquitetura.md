Visão Geral da Arquitetura - Projeto Mega-Sena
Introdução

O projeto Mega-Sena é um sistema de engenharia de dados desenvolvido para realizar o processo de Extração, Transformação e Carregamento (ETL) dos dados dos sorteios da loteria Mega-Sena. O objetivo principal é coletar, processar e armazenar os resultados dos sorteios em um formato adequado para análise posterior.
Componentes Principais
1. Extração de Dados

    Módulo responsável por extrair os resultados dos sorteios da Mega-Sena a partir de fontes oficiais, como APIs ou sites autorizados.
    Utiliza requisições HTTP ou outras técnicas para obter os dados mais recentes dos sorteios.

2. Transformação de Dados

    Etapa onde os dados brutos são processados e transformados para um formato consistente e pronto para análise.
    Aplica limpezas, conversões de formato, cálculos estatísticos básicos e identificação de padrões nos dados.

3. Carregamento de Dados

    Processo de carregar os dados processados em um local de armazenamento persistente, como um banco de dados ou arquivos estruturados.
    Garante que os dados estejam prontos para serem consultados e utilizados em análises posteriores.

Tecnologias Utilizadas

    Python: Principal linguagem de programação para o desenvolvimento dos scripts de ETL.
    Pandas: Biblioteca utilizada para manipulação e análise de dados tabulares.
    Requests: Utilizada para fazer requisições HTTP para a extração de dados.
    SQLite: Banco de dados utilizado para armazenar os resultados dos sorteios de forma estruturada.

Estrutura do Projeto

    /scripts: Contém os scripts Python para a extração, transformação e carregamento dos dados.
    /data: Armazena os dados brutos e processados dos sorteios.
    /docs: Documentação do projeto, incluindo instruções de uso e detalhes da arquitetura.