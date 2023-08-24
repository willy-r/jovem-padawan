![LukeYoda](https://user-images.githubusercontent.com/47596121/99835654-ad95a200-2b43-11eb-9169-57eca7d3e432.jpg)

# jovem-padawan

Um programa que monitora novas ofertas para um produto específico no site [Hardmob](https://www.hardmob.com.br/forums/407-Promocoes) e te avisa por e-mail sobre as promoçãos encontradas.

> Inspirado pelo [robsonbittencourt/gafanhoto](https://github.com/robsonbittencourt/gafanhoto).

---

## Por quê?

Eu precisava de um *Kindle* e tava querendo comprar um baratinho, um amigo meu me apresentou esse site e então surgiu essa ideia de automatizar esse trabalho de ficar procurando por um!

Se você está se perguntando o porque do nome **jovem-padawan**, *“paciência você deve ter meu jovem Padawan”* para achar um produto baratinho e que atenda as suas necessidades.

---

## Instalação

- Você precisa da versão 3.9 do Python instalada no seu computador, na qual você pode encontrar [aqui](https://www.python.org/downloads/release/python-390/).

### Clone

- Clone esse repositório para o seu computador com o comando `$ git clone https://github.com/willy-r/jovem-padawan.git`

### Algumas configurações

- Vá para o repositório que você acabou de clonar, `jovem-padawan`:

```shell
$ cd jovem-padawan
```

- Crie um ambiente virtual dentro dessa pasta (recomendado mas opcional):

> aqui eu estou usando o `venv` por ele já vir instalado com o Python, mas sinta-se à vontade para escolher o que você mais se sentir confortável

```shell
$ python -m venv venv
```

- Ative o ambiente virtual e instale as dependências:

```shell
$ source env/bin/activate
(venv) $ pip install -r requirements.txt 
```

### Configurando a conta do Google para envio de email

Para usar o programa você tambêm precisará permitir o [**Acesso a apps menos seguro**](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Mlp8VVUEn2uTz6JmNPBaS9y3390NjZo52HWBjCQfMpL5LC6AR9ItTICZwSYq0gRefPyAV4pz329WcsXOvWABM2hzGzvQ) na sua conta do Google, dê uma lida sobre!

![20201120_200920](https://user-images.githubusercontent.com/47596121/99858540-8b644a00-2b6c-11eb-8efa-feb881a80ab0.jpg)

---

## Usando

Para usar é bem simples:

```shell
(env) $ python -m app.main product
? E-mail: exemplo@gmail.com
? Senha do e-mail:
```

- **product** é o nome do produto para monitorar.

- Sua senha não será mostrada quando você estiver digitando mas ela irá funcionar do mesmo jeito.

- Só irá aparecer para você colocar a senha e o e-mail se você não quiser seguir um dos passos abaixo.

O programa usa o mesmo e-mail para enviar e receber as ofertas, então é necessário você se autenticar com uma conta *Gmail* válida e existem outras duas formas de você fazer isso:

1. Usando enviroment variables (recomendado):

    ```shell
    (venv) $ export EMAIL_USERNAME='exemplo@gmail.com'
    (venv) $ export EMAIL_PASSWORD='senha_do_seu_email'
    ```
    > Ou mude o nome do arquivo `.env.example` para `.env` e preencha as variáveis de ambiente necessárias.

2. Passando como argumentos na linha de comando quando for executar o programa (não é recomendado mas é uma opção):

    ```shell
    (venv) $ python -m app.main -e exemplo@gmail.com -p senha_do_seu_email product
    ```

Digite `$ python -m app.main -h` para ver mais comandos.

---

## Exemplo

- Procurando por ofertas para o *Kindle* por exemplo, e usando minhas credênciais definidas nas enviroment variables:

```shell
(venv) $ python -m app.main kindle
(16:22) - jovem-padawan: INFO: Procurando por ofertas para "Kindle" em https://www.hardmob.com.br/forums/407-Promocoes
(16:22) - jovem-padawan: INFO: Novas ofertas encontradas para "Kindle"
(16:22) - jovem-padawan: INFO: Enviado e-mail com as ofertas para exemplo@gmail.com
```

  - Para parar o programa digite `CTRL + C`.

### E-mail recebido

- O e-mail recebido terá mais ou menos essa aparência:

![Imagem do e-mail reebido](https://user-images.githubusercontent.com/47596121/99842296-52b57800-2b4e-11eb-9863-e80705f9ea3a.jpg)

---

## Contribua!

> Tá afim de me ajudar? Estamos todos em uma plataforma que apoia o Open Source e não existe pessoa melhor do que você que está lendo isso para ajudar a melhorar esse projeto!

### Primeiro passo

- **Opção 1**
    - 🍴 Dê fork nesse repositório!

- **Opção 2**
    - 👯 Clona esse repositório no seu computador usando `https://github.com/willy-r/jovem-padawan.git`

### Segundo passo

- **MANDA VER!** 🔨🔨🔨

### Terceiro passo

- 🔃 Crie um PR usando <a href="https://github.com/willy-r/jovem-padawan/compare" target="_blank">`https://github.com/willy-r/jovem-padawan/compare`</a>.

---

## Me siga!

Você pode me encontrar falando um pouco de tudo (mais sobre programação) nos seguintes lugares:

- No Twitter em <a href="https://twitter.com/lliw_r?s=09" target="_blank">`@lliw_r`</a>

---
