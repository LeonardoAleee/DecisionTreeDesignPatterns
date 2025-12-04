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

-----

### Iterator

O padrão **Iterator** possibilita percorrer uma estrutura de dados sem expor sua implementação interna.  
Na árvore de decisão, o Iterator controla como os nós são visitados:

- `PreOrderIterator` percorre a árvore em pré-ordem.
- `BFSIterator` percorre a árvore em largura, visitando primeiro todos os nós de um nível antes de avançar para o próximo.

O uso de iteradores permite navegar pela árvore de forma independente da lógica do nó, mantendo o design desacoplado e flexível.