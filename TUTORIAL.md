# 🌌 Como usar este Perfil Automático no seu GitHub

Gostou do visual interativo com os SVGs dinâmicos? Este repositório foi customizado para não apenas usar o gerador de SVGs do [vinimlo/galaxy-profile](https://github.com/vinimlo/galaxy-profile), mas também **atualizar automaticamente seus repositórios mais recentes**!

Siga o passo a passo abaixo para usar essa automação no seu próprio perfil.

## 1. Faça um Fork / Use como Template
1. Faça um **Fork** deste repositório ou crie um repositório com o mesmo nome do seu usuário do GitHub (ex: `seu-usuario/seu-usuario`).
2. Copie os arquivos deste repositório para o seu, especialmente:
   - `config.yml`
   - A pasta `.github/workflows/` inteira.

## 2. Gere o seu Token de Acesso (PAT)
Para que os gráficos consigam ler seus **repositórios privados** e atualizar corretamente suas linguagens e commits:
1. Vá em **Settings > Developer settings > Personal access tokens > Tokens (classic)** no GitHub.
2. Clique em **Generate new token (classic)**.
3. Dê um nome (ex: `Profile_SVGs`) e em **Expiration** coloque *No expiration* (ou renove quando expirar).
4. Em **Select scopes**, marque **apenas a caixinha principal `repo`** (isso marcará as sub-opções automaticamente e dará acesso para ler seus commits privados).
5. Clique em **Generate token** e copie o código `ghp_...` gerado.

## 3. Configure o Token no Repositório
1. Vá no seu repositório recém-criado (`seu-usuario/seu-usuario`).
2. Vá em **Settings > Secrets and variables > Actions**.
3. Clique em **New repository secret**.
4. No nome, coloque exatament: **`PAT_TOKEN`**.
5. No valor, cole o token (`ghp_...`) que você acabou de gerar.

## 4. Edite o `config.yml` (Opcional)
Você pode editar o `config.yml` para mudar:
- Seu nome de usuário (`username: seu-usuario`)
- Suas descrições e links sociais
- As cores (`theme`)
- *Nota: Você não precisa preencher os `projects` manualmente, pois nosso script customizado fará isso por você!*

## 5. Deixe a Mágica Acontecer! 🪄
Pronto! Sempre que você fizer um *push* neste repositório ou à meia-noite todos os dias, a GitHub Action irá:
1. Rodar o nosso script em Python (`auto_projects.py`) para buscar seus 3 repositórios mais recentes.
2. Injetar esses repositórios no seu `config.yml`.
3. Gerar as novas imagens SVG.
4. Fazer um *commit* automático das imagens atualizadas na pasta `assets/generated/`.

Agora o seu perfil será 100% dinâmico e mostrará sempre no que você está trabalhando! 🚀
