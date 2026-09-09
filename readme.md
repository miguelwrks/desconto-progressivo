# Programa de Desconto Progressivo

Este projeto consiste em um script em Python que calcula o valor final de uma compra aplicando uma porcentagem de desconto progressivo de acordo com o valor total inserido.

---

## 💡 Lógica Utilizada

1. **Limpeza do Terminal:** O programa verifica o sistema operacional (`os.name`) e executa o comando apropriado (`cls` para Windows ou `clear` para Linux/macOS) para manter a tela limpa.
2. **Entrada de Dados:** Solicita o valor total da compra ao usuário e converte para o tipo `float`, permitindo trabalhar com casas decimais para o cálculo percentual.
3. **Cálculo do Desconto:**
   - O valor do desconto é calculado multiplicando o `valorTotal` pela porcentagem correspondente (`0.05`, `0.10` ou `0.15`).
   - O valor final com desconto é obtido subtraindo o desconto do valor total (`valorTotal - desconto`).
4. **Exibição dos Resultados:** Exibe na tela o total final a ser pago, o valor economizado com a respectiva taxa de desconto e o valor original da compra.

---

## 🔀 Estrutura de Decisão (`if` / `elif` / `else`)

- **`if valorTotal < 200:`**
  - **Condição:** Compras com valor abaixo de R$ 200,00.
  - **Regra:** Aplica **5% de desconto** (`valorTotal * 0.05`).

- **`elif valorTotal >= 200 and valorTotal < 300:`**
  - **Condição:** Compras com valor igual ou superior a R$ 200,00 e inferior a R$ 300,00.
  - **Regra:** Aplica **10% de desconto** (`valorTotal * 0.10`).

- **`else:`**
  - **Condição:** Compras com valor igual ou superior a R$ 300,00 (`valorTotal >= 300`).
  - **Regra:** Aplica **15% de desconto** (`valorTotal * 0.15`).

---

**Desenvolvido por:** Miguel Gonçalves
