# 🚌 PoccoBus - Sistema de Venda de Passagens

Projeto desenvolvido para modernizar o sistema de venda de passagens da **PoccoBus**, empresa que integra a holding **Pocco In**. Mesmo sendo uma das maiores do setor, o sistema atual é manual e ultrapassado. A diretora de operações, **Toni Collette**, contratou nossa equipe para desenvolver uma nova solução utilizando **Python**.

---

## 🎯 Objetivo

Automatizar o processo de venda de passagens com as seguintes funcionalidades:

- Exibição de matriz de assentos com legendas visuais;
- Compra de assentos disponíveis (em verde);
- Atualização automática da matriz após cada venda;
- Geração de relatório `.txt` com todos os assentos vendidos e disponíveis;
- Tratamento de entradas inválidas ou tentativas de compra de assentos indisponíveis.

---

## 🪑 Visão dos Assentos

A matriz do ônibus segue o seguinte padrão:

- 🟦 **Azul**: Assento do motorista  
- ⬜ **Cinza**: Corredor e partes não disponíveis  
- 🟩 **Verde**: Assentos disponíveis para venda  
- ❌ **Vermelho** (durante execução): Assentos já vendidos  

A estrutura da matriz é gerada automaticamente de acordo com a visão fornecida pela diretoria.

---

## 🧠 Lógica do Sistema

1. Geração automática da matriz do ônibus com base na estrutura predefinida;
2. Exibição da matriz para visualização dos assentos;
3. Validação de entrada do usuário (assento válido, não vendido);
4. Venda do assento e atualização da matriz em tempo real;
5. Registro final em `vendas.txt` com:
   - Lista de assentos vendidos;
   - Lista de assentos ainda disponíveis.

---
