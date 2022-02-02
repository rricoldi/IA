import { Agent } from "./entities/Agent.ts";
import { Environment } from "./entities/Environment.ts";
import { IState, Power } from "./interfaces/State.ts";

const environment = new Environment(3, 34);
const objective = new Environment(0, 18);

const state: IState = {
  temperature: 0,
  power: Power.low,
  isOn: false,
};


const rulesFunction = (environment: Environment, currentState: IState, objective: Environment): IState => {
  const currentTemperature = environment.getTemperature();
  const idealTemperature = objective.getTemperature();


  if(currentTemperature === idealTemperature) {
    currentState.isOn = false;
    return currentState;
  }

  currentState.temperature = idealTemperature;
  currentState.isOn = true;

  if(Math.abs(currentTemperature - idealTemperature) > 10) {
    currentState.power = Power.high;
  } else if(Math.abs(currentTemperature - idealTemperature) > 5) {
    currentState.power = Power.medium;
  } else {
    currentState.power = Power.low;
  }

  return currentState;
}

const agent = new Agent(rulesFunction, state, objective)

for(let i = 0; i < 15; i++) {
  environment.updateEnvironment(agent.state);
  agent.update(environment);
  const log =
    [`===================================`,
    `Temperatura do ambient: ${environment.getTemperature()} °C`,
    `Temperatura ideal: ${objective.getTemperature()} °C`,
    `Ar condicionado ${agent.state.isOn ? 'ligado' : 'desligado'}.`,
    `Potência do ar condicionado: ${agent.state.power}`,
    `===================================`,]
  
  console.log(log.join('\n'))
}