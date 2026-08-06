# 🌐 Exercício – Navegador com Histórico Completo usando Pilhas e Lista

**Objetivo:**  
Implementar a estrutura de dados **Pilha** e **Lista** em Python para simular um navegador com funções de **visitar**, **voltar**, **avançar** e **histórico completo** que registra todos os acessos e movimentos.

---

## Descrição

Você deve criar:

1. **Classe `Pilha`** para representar pilhas de páginas anteriores e futuras.
2. **Classe `Navegador`** que:
   - Possui duas pilhas:
     - **Páginas anteriores** (para o botão "Voltar").
     - **Páginas futuras** (para o botão "Avançar").
   - Possui uma **lista `historico_completo`** que registra **todos os acessos e movimentos** do usuário, na ordem exata em que ocorreram.
   - Mantém a **página atual**.
   - Permite visitar novas páginas, voltar, avançar e mostrar todo o histórico.

---

## Regras

1. **Classe `Pilha`** deve ter no mínimo:
   - `__init__(self)`
   - `esta_vazia(self)`
   - `empilhar(self, item)`
   - `desempilhar(self)`
   - `tamanho(self)`
   - `__str__(self)`

2. **Classe `Navegador`** deve ter:
   - `__init__(self, pagina_inicial)` – define a página inicial, cria as pilhas e inicializa o histórico.
   - `visitar(self, pagina)` – empilha a página atual na pilha de anteriores, limpa a pilha de futuras, atualiza a página atual e registra o acesso no histórico completo.
   - `voltar(self)` – move a página atual para futuras, atualiza a página atual para a última da pilha de anteriores, e registra o movimento no histórico completo.
   - `avancar(self)` – move a página atual para anteriores, atualiza a página atual para a última da pilha de futuras, e registra o movimento no histórico completo.
   - `pagina_atual(self)` – retorna a página atual.
   - `mostrar_historico(self)` – exibe a lista com todas as páginas visitadas e movimentos realizados, na ordem cronológica.

3. O programa deve permitir os comandos:
   - `visitar <site>`
   - `voltar`
   - `avancar`
   - `atual`
   - `historico`
   - `sair`

---

## Exemplo de execução

```
Digite um comando: visitar google.com
Página atual: google.com

Digite um comando: visitar youtube.com
Página atual: youtube.com

Digite um comando: visitar github.com
Página atual: github.com

Digite um comando: voltar
Página atual: youtube.com

Digite um comando: avancar
Página atual: github.com

Digite um comando: voltar
Página atual: youtube.com

Digite um comando: historico
Histórico completo: ['google.com', 'youtube.com', 'github.com', 'youtube.com', 'github.com', 'youtube.com']
```
