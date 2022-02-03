import { Agent } from "./entities/Agent.ts";
import { Environment } from "./entities/Environment.ts";
import { IState } from "./interfaces/State.ts";
import { getNumberCloserToGoal } from "./utils/getNumberCloserToGoal.ts";

const environment = new Environment(3);

const state: IState = {
  story: 0,
  isDoorOpen: false,
  goalStory: 0,
  callQueue: [],
};


const rulesFunction = (environment: Environment, currentState: IState): IState => {
  if(!(currentState.callQueue.find(item => item === environment.storyCalling) || currentState.goalStory === environment.storyCalling)) // rule 4
    currentState.callQueue.push(environment.storyCalling);

  if(currentState.story === currentState.goalStory) { // rule 1
    currentState.isDoorOpen = true;
    currentState.goalStory = currentState.callQueue.shift() ?? currentState.story;
  } else { // rule 2 and 3
    currentState.isDoorOpen = false;
    currentState.story = getNumberCloserToGoal(currentState.story, currentState.goalStory);
  }

  return currentState;
}

const agent = new Agent(rulesFunction, state);

for (let i = 0; i < 15; i++) {
  environment.updateEnvironment();
  agent.update(environment);
  const log =
    [`===================================`,
    `Andar atual: ${agent.state.story}`,
    `Elevador está ${agent.state.story !== agent.state.goalStory ? `indo para o ${agent.state.goalStory}° andar` : `parado`}`,
    `Porta está ${agent.state.isDoorOpen ? `aberta` : `fechada`}`,
    `Próximos andares programados para ir: ${agent.state.callQueue}`,
    `===================================`,]
  
  console.log(log.join('\n'))
}