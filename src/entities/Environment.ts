export class Environment {
  constructor(
    public storyCalling: number,
  ) {}

  public updateEnvironment(): Environment {
    if(Math.random() > 0.9) 
      this.storyCalling = Math.round(Math.random() * 10);

    return this;
  }

}