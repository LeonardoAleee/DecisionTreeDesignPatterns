# Projeto Individual de Modelagem – Árvore de Decisão (Mock)

Este projeto apresenta a modelagem de uma árvore de decisão simplificada, utilizando quatro padrões de projeto fundamentais:

- Composite
- Iterator
- Visitor
- State

Todo o comportamento é mockado, sem execução de algoritmos reais — apenas prints que representam operações e transições.

-----

### Composite

O padrão **Composite** permite estruturar objetos em hierarquias do tipo árvore, onde elementos individuais e composições são tratados da mesma maneira.

No projeto, esse padrão modela a própria árvore de decisão:

- **Node** é o componente base.
- **DecisionNode** representa nós internos que possuem filhos (Composite).
- **LeafNode** representa folhas, sem filhos (Leaf).

Com isso, o código trata `DecisionNode` e `LeafNode` de forma uniforme, permitindo chamadas como `node.accept(visitor)` independentemente do tipo do nó. Esse padrão é ideal para estruturas hierárquicas como árvores de decisão.
