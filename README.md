# Projeto de Compiladores – MiniCalc

Repositório do projeto desenvolvido para a disciplina de **Teoria da Computação e Compiladores** (4º semestre de Ciência da Computação).

Este trabalho é composto por:

- Estudo de caso de um compilador real (**GCC – GNU Compiler Collection**)
- Projeto de arquitetura de um compilador acadêmico (**MiniCalc**)
- Protótipo funcional de **analisador léxico e sintático**
- Execução das expressões via interpretador (simulando geração/execução de código)
- Relatório teórico separado em PDF/Word (entregue via AVA / Moodle / Canvas)


# Objetivo do Projeto

O objetivo é **colocar em prática os conceitos de compiladores**:

- Análise léxica (tokens)
- Análise sintática (gramática / parser)
- Construção de uma AST (árvore sintática abstrata)
- Execução / interpretação baseada na AST (simulando geração de código)
- Organização do projeto em repositório Git

O compilador **MiniCalc** funciona sobre uma mini-linguagem matemática simples, usada como exemplo didático.

---

## 🧠 Linguagem MiniCalc

A linguagem **MiniCalc** suporta:

- Números inteiros  
- Operadores: `+`, `-`, `*`, `/`  
- Parênteses `(` `)` para prioridade  
- Comando `print` para exibir o resultado  

Exemplo de código em MiniCalc:

```text
print (3 + 5) * 2
****
