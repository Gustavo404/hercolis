# Hercolis
O bot "hercolis" é um script desenvolvido para automatizar a verificação do cadastro de clientes no sistema Zeus. Ele utiliza o Edge WebDriver e o Selenium para realizar essa tarefa de forma eficiente e precisa. O bot permite que os usuários forneçam uma lista de clientes e verifica se cada cliente está cadastrado no sistema Zeus. O resultado da verificação é registrado em arquivos de texto para análise posterior.

## Pré-Requisitos
Antes de executar o bot "hercolis", certifique-se de que os seguintes pré-requisitos sejam atendidos:

1. **Microsoft Edge WebDriver:** O bot requer a instalação do Microsoft Edge WebDriver compatível com a versão do Microsoft Edge instalada no sistema. Certifique-se de configurar o caminho do executável do Microsoft Edge WebDriver corretamente no código.

2. **Python:** É necessário ter o Python instalado no sistema para executar o script.

3. **Bibliotecas Python:** Instale as bibliotecas Python necessárias usando o pip. As bibliotecas usadas incluem o Selenium.

```bash
pip install selenium
```

## Como Usar o Bot
Siga as etapas abaixo para usar o bot "hercolis":

1. Execute o script Python "hercolis.py" em um ambiente Python configurado corretamente.
```bash
python hercolis.py
```

## Como o Bot funciona
1. O bot iniciará o Microsoft Edge e abrirá a página de login do sistema Zeus.

2. O usuário será solicitado a inserir o login e a senha. Essas informações são inseridas manualmente pelo usuário.

3. O bot começará a verificar o cadastro dos clientes fornecidos em um arquivo de texto chamado "clientes.txt". Cada linha deste arquivo deve conter informações de um cliente.

4. Para cada cliente na lista, o bot preencherá o campo correspondente na página do sistema Zeus e verificará se o cliente está cadastrado.

5. O resultado da verificação é registrado em dois arquivos de texto: "cadastrado.txt" (para clientes cadastrados) e "semCadastrado.txt" (para clientes não cadastrados).

6. O bot continuará verificando os clientes na lista até que todos sejam processados.

7. Após a conclusão da verificação, o Microsoft Edge será fechado e o bot encerrará a execução.

## Arquivos de Saída
O bot gera dois arquivos de saída:

1. **cadastrado.txt:** Este arquivo contém os dados dos clientes que foram encontrados cadastrados no sistema Zeus durante a verificação.

2. **semCadastrado.txt:** Este arquivo contém os dados dos clientes que não foram encontrados cadastrados no sistema Zeus durante a verificação.

## Observações
>Certifique-se de que os nomes e identificadores dos elementos da página da web (como campos de login, senha e botões) no código correspondam à estrutura da página do sistema Zeus atual. Qualquer alteração na estrutura da página pode exigir atualizações no código.

>Este bot é destinado apenas para uso educacional ou em ambientes onde a automação é permitida e ética. O uso inadequado ou não autorizado do bot pode violar os termos de serviço do site.

## Autor
O bot "hercolis" foi desenvolvido por Marcio Gustavo (Gustavo404) como um projeto de automação de tarefas.

## Contribuições
Contribuições para a melhoria deste bot são bem-vindas. Você pode enviar solicitações de pull com melhorias, correções de bugs ou novos recursos.

## Licença
Este bot é distribuído sob a *GPL2.0* License. Consulte o arquivo LICENSE para obter detalhes.

## Contato
Para entrar em contato com os desenvolvedores ou relatar problemas, você pode enviar um e-mail para gustavo404.marcio@gmail.com.

## Agradecimentos
Agradecemos à comunidade de código aberto e às bibliotecas de automação, como o Selenium, que tornaram possível o desenvolvimento deste bot.
