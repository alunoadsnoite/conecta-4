# Conecta 4

Projeto de inteligência artificial para o jogo **Conecta 4** (Connect Four). O objetivo é formar uma sequência de **4 peças** consecutivas na horizontal, vertical ou diagonal.

## Visão geral

O projeto possui um mediador do jogo e dois jogadores:

- **Random**: realiza jogadas aleatórias.
- **Valdenor**: jogador baseado em uma busca heurística inspirada em colônia de abelhas.

## Requisitos

- Python 3.10+
- Dependências:
  - `numpy`
  - `matplotlib`

Instale com:

```bash
pip install numpy matplotlib
```

## Como executar

1. Entre na pasta do projeto:

```bash
cd "conecta 4"
```

2. Execute o mediador:

```bash
python mediador.py
```

A janela do `matplotlib` exibirá o tabuleiro e o resultado da partida.

## Estrutura do repositório

- `mediador.py`: controla o jogo e a interface visual.
- `jogador_random.py`: implementação do jogador aleatório.
- `valdenor.py`: implementação do jogador heurístico.

## Regras do jogo

- O tabuleiro tem 6 linhas e 7 colunas.
- Cada jogador solta uma peça por vez na coluna escolhida.
- Vence quem completar 4 peças consecutivas na horizontal, vertical ou diagonal.

## Personalização

Você pode criar novos jogadores implementando a função `jogada(board, piece)` e definindo a constante `NAME` em um novo módulo, depois importar no `mediador.py`.
