def create_env_file():
    env_vars = {
    'API_KEY': 'your_api_key',
    'DB_NAME': 'your_database_name',
    'USERNAME': 'your_username',
    'PASSWORD': 'your_password'
    }
    with open('.env', 'w') as env_file:
        for key, value in env_vars.items():
            env_file.write(f'{key}={value}\n')