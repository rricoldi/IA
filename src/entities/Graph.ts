import { Node } from "../interfaces/Node.ts";

export class Graph {
  constructor(
    public nodes: Node[],
  ) {}

  public print(): void {
    const result = this.nodes.map(node => `${node.index} -> ${node.neighbors.join(', ')}`);

    console.log(result.join('\n'));
  }

  public getHeight() {
    const foundVertices: string[] = [];
    let height = 1;
    
    const dfs = (node: Node, currentHeight: number) => {
      if(currentHeight > height)
        height = currentHeight;

      foundVertices.push(node.index);

      node.neighbors.forEach(neighbor => {
        if (!foundVertices.includes(neighbor)) {
          currentHeight += 1;
          dfs(this.nodes.find(n => n.index === neighbor)!, currentHeight);
          currentHeight -= 1;
        }
      });
    };

    dfs(this.nodes[0], height);

    return height;
  }

  public depthFirstSearch(goalVertex: string, limit?: number): string[] | null {
    const foundVertices: string[] = [];

    let currentLimit = 0;

    const dfs = (node: Node) => {
      currentLimit += 1;

      if(limit && currentLimit > limit) return;

      foundVertices.push(node.index);

      if(node.index === goalVertex) {
        return;
      }

      node.neighbors.forEach(neighbor => {
        if (!foundVertices.includes(neighbor) && !foundVertices.includes(goalVertex)) {
          dfs(this.nodes.find(n => n.index === neighbor)!);
          currentLimit -= 1;
        }
      });
    };

    dfs(this.nodes[0]);

    if(!foundVertices.includes(goalVertex))
      return null;

    return foundVertices;
  }

  public iterativeDepthFirstSearch(goalVertex: string): string[] {
    let limit = 1;

    console.log(`\nIterative Depth First Search:`);

    while(limit <= this.getHeight()) {
      const foundVertices = this.depthFirstSearch(goalVertex, limit);

      console.log(`Limit: ${limit} | Search: ${foundVertices ? foundVertices.join(', ') : 'Not found'}`);

      if(foundVertices)
        return foundVertices;

      limit += 1;
    }

    return [];
  }
}