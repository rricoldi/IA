import { IState, Power } from "../interfaces/State.ts";

export class Environment {
  constructor(
    public variance: number,
    private temperature: number,
  ) {}

  public updateEnvironment(agentState: IState): Environment {
    if (agentState.isOn) {
      this.temperature = this.getNewTemperatureByPower(agentState.power, agentState.temperature) ;
    } else {
      this.temperature = this.temperature + this.randomlyAddOrSubtract(this.variance);
    }

    return this;
  }

  public getTemperature(): number {
    return this.temperature;
  }

  private getNewTemperatureByPower(power: Power, goalTemperature: number): number {
    if (power === Power.high) {
      return this.temperature + this.getTemperatureVariance(this.temperature, goalTemperature, 2);
    } 
    
    if (power === Power.medium) {
      return this.temperature + this.getTemperatureVariance(this.temperature, goalTemperature, 5);
    }
      
    return this.temperature + this.getTemperatureVariance(this.temperature, goalTemperature, 10);
  }
  
  private getTemperatureVariance(current: number, goal: number, divider: number) {
    const difference = goal - current;

    return difference < 0 ? Math.floor(difference / divider) : Math.ceil(difference / divider);
  }
  
  private randomlyAddOrSubtract(value: number): number {
    const randomNumber = Math.random();

    if (randomNumber < 0.5) {
      return Math.round(Math.random() * value);
    }

    return -Math.round(Math.random() * value);
  }
}