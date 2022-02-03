export class Agent<State, Environment> {
  public state: State;
  
  constructor(
    public rulesFunction: (environment: Environment, currentState: State) => State,
    initialState: State,
  ) {
    this.state = initialState;
  }

  update(environment: Environment): void {
    this.state = this.rulesFunction(environment, this.state);
  }
}