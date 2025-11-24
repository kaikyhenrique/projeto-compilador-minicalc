Kaiky Henrique Alves dos Reis
RA: 12524116655

- Projeto de Compiladores – MiniCalc

Este repositório faz parte do trabalho da disciplina de Teoria da Computação e Compiladores.  
Aqui eu desenvolvi um compilador simples chamado **MiniCalc**, criado especialmente para este projeto.

A ideia foi mostrar, de forma prática, como funciona o processo básico de compilação, desde a leitura do código até a execução do resultado.

- Objetivo do Projeto

O MiniCalc serve para demonstrar as etapas principais de um compilador:

- análise léxica (geração de tokens)
- análise sintática (estrutura da expressão)
- análise semântica simples
- geração de um bytecode básico
- execução das instruções por uma máquina virtual

A linguagem MiniCalc é pequena de propósito, justamente para facilitar a visualização de cada etapa.

---

- Sobre a Linguagem MiniCalc

A linguagem permite:

- números inteiros  
- operadores `+`, `-`, `*`, `/`  
- parênteses  
- o comando `print`  

Exemplo usado no trabalho:

```text
print (3 + 5) * 2
