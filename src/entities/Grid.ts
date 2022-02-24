import { IPosition } from '../interfaces/Position.ts'

export class Grid {
  constructor(public origin: IPosition, public end: IPosition) {}

  public isPositionInGrid(position: IPosition): boolean {
    return (
      position.x >= this.origin.x &&
      position.x <= this.end.x &&
      position.y >= this.origin.y &&
      position.y <= this.end.y
    );
  }

  public getPositionNeighbors(position: IPosition): IPosition[] {
    const neighbors: IPosition[] = [];

    const { x, y } = position;

    for(let a = x - 1; a <= x + 1; a++) {
      for(let b = y - 1; b <= y + 1; b++) {
        if((a === x && b === y) || !this.isPositionInGrid({ x: a, y: b })) continue;

        neighbors.push({ x: a, y: b });
      }
    }

    return neighbors;
  }


  public aStar(origin: IPosition, goal: IPosition) {
    let edges = [{position: origin, total: this.getDistanceBetweenPositions(origin, goal)}]

    const visited: IPosition[] = [];

    while(!this.verifyIfPositionsAreTheSame(origin, goal)) {
      visited.push(origin);

      const originTotal = edges.find(edge => this.verifyIfPositionsAreTheSame(edge.position, origin))?.total ?? 0;

      const possibleEdges = this.getPositionNeighbors(origin).map(neighbor => {
        const distance = originTotal - this.getDistanceBetweenPositions(origin, goal);
        const heuristic = this.getDistanceBetweenPositions(neighbor, goal);
  
        return {
          position: neighbor,
          total: distance + heuristic,
        }
      })

      
      edges = [...edges, ...possibleEdges].sort((a, b) => a.total - b.total);
  
      const closerDistance = edges.slice(0, 1)[0];

      origin = closerDistance.position;
    }

    return [...visited, origin];
  }

  private getDistanceBetweenPositions(positionA: IPosition, positionB: IPosition): number {
    const deltaX = Math.abs(positionA.x - positionB.x);
    const deltaY = Math.abs(positionA.y - positionB.y);

    return Math.sqrt(Math.pow(deltaX, 2) + Math.pow(deltaY, 2));
  }

  private verifyIfPositionsAreTheSame(positionA: IPosition, positionB: IPosition): boolean {
    return positionA.x === positionB.x && positionA.y === positionB.y;
  }
}