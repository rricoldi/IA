import { Graph } from "./entities/Graph.ts";

const graph = new Graph([
  {
    index: 'A',
    neighbors: ['B', 'C'],
  },
  {
    index: 'B',
    neighbors: ['D'],
  },
  {
    index: 'C',
    neighbors: ['E', 'F'],
  },
  {
    index: 'D',
    neighbors: ['G'],
  },
  {
    index: 'E',
    neighbors: [],
  },
  {
    index: 'F',
    neighbors: [],
  },
  {
    index: 'G',
    neighbors: [],
  }
]);

graph.print();

console.log(`\nHeight: ${graph.getHeight()}`);

const DFSResult = graph.depthFirstSearch('G');

if(!DFSResult) 
  console.log('\n---------------\nItem not found!\n---------------')
else
  console.log(`\nDepth First Search: ${DFSResult.join(', ')}`);

graph.iterativeDepthFirstSearch('G');