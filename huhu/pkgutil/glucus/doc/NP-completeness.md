# Goals

- Understand the basic idea of P and NP
- Formulate some problems from the perspective of NP-completeness

# Tables of contents

# Contents

## Introduction and motivation

### Big-Oh notation

### Classify Problems According to Computational Requirements

Is polynomoial-time Algorithms
| Yes | Probably no |
| :--------: | :-------: |
| Shortest path | Longest path |
| Matching | 3D-matching |
| Min cut | Maxcut |
| 2-SAT | 3-Sat |
| Planar 4-color| Planar 3-color |
| Bipartite vertex cover | Vertex cover |
| Primality testing | Factoring |

## P and NP

- The `class P`: consists of those problems that are solvable in polynomial time.
- More specifically, they are problems that can solved in time `O(n^k)` for some constant **_k_**, where n is the size of the input to the problem.
- The key is that n is the size of input.

`Observation` of NP-complete and polynomial reduce to one another!

`CIRCUIT-SAT`
- 3-SAT
    - INDEPENDENT SET
        - VERTEX COVER
            - SET COVER
    - DIR-HAM-CYCLE
        - HAM-CYCLE
            - TSP
    - GRAPH 3-COLOR
        - PLANAR 3-CORLOE
            - TSP
    - SUBSET-SUM
        - SCHEDULING
            - TSP
            

## NP-Completeness

## Reduction

## Solving NP-Complete Problems
