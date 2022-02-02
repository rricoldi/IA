export class Agent<State, Environment> {
  public state: State;
  
  constructor(
    public rulesFunction: (environment: Environment, currentState: State, objective: Environment) => State,
    initialState: State,
    public objective: Environment,
  ) {
    this.state = initialState;
  }

  update(environment: Environment): void {
    this.state = this.rulesFunction(environment, this.state, this.objective);
  }
}