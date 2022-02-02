export enum Power {
  low = 'low',
  medium = 'medium',
  high = 'high',
}

export interface IState {
  temperature: number;
  power: Power;
  isOn: boolean;
}