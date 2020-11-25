from kaggle_environments.envs.football.helpers import *

@human_readable_agent
def agent(obs):
    # Make sure player is running.
    if Action.Sprint not in obs['sticky_actions']:
        return Action.Sprint
    # We always control left team (observations and actions
    # are mirrored appropriately by the environment).
    controlled_player_pos = obs['left_team'][obs['active']]
    # Does the player we control have the ball?
    if obs['ball_owned_player'] == obs['active'] and obs['ball_owned_team'] == 0:
        # Shot if we are 'close' to the goal (based on 'x' coordinate).
        if controlled_player_pos[0] > 0.4:
            return Action.Shot
        # Run towards the goal otherwise.
        return Action.Right
    else:
        # Run towards the ball.
        if obs['ball'][0] > controlled_player_pos[0] + 0.07:
            return Action.Right
        if obs['ball'][0] < controlled_player_pos[0] - 0.07:
            return Action.Left
        if obs['ball'][1] > controlled_player_pos[1] + 0.07:
            return Action.Bottom
        if obs['ball'][1] < controlled_player_pos[1] - 0.07:
            return Action.Top
        # Try to take over the ball if close to the ball.
        return Action.Slide