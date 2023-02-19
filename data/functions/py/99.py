def play_env_problem_randomly(env_problem,
                              num_steps):
  """Plays the env problem by randomly sampling actions for `num_steps`."""
  # Reset all environments.
  env_problem.reset()

  # Play all environments, sampling random actions each time.
  for _ in range(num_steps):
    # Sample batch_size actions from the action space and stack them.
    actions = np.stack([env_problem.action_space.sample() for _ in range(
        env_problem.batch_size)])

    # Execute actions, observations are stored in `env_problem`.
    _, _, dones, _ = env_problem.step(actions)

    # Get the indices where we are done and reset those.
    env_problem.reset(indices=done_indices(dones))