from program import episode_data


def min_episodes():
    return min(episode_data.keys())


def get_episode(show_id):
    return episode_data.get(show_id)


def max_episode():
    return max(episode_data.keys())