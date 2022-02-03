export function getNumberCloserToGoal(current: number, goal: number) {
  if (current > goal) {
    return current - 1;
  }
  
  return current + 1;
}