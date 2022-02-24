import { Grid } from "./entities/Grid.ts";

const grid = new Grid({ x: -20, y: -20 }, { x: 10, y: 10 });

console.log(grid.aStar({ x: -3, y: -15 }, { x: 10, y: 4 }))