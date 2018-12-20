import zipfile, requests, pickle, os, sqlite3
import pandas as pd


def download_file_from_google_drive(id, destination):
    URL = "https://docs.google.com/uc?export=download"

    session = requests.Session()

    response = session.get(URL, params = { 'id' : id }, stream = True)
    token = get_confirm_token(response)

    if token:
        params = { 'id' : id, 'confirm' : token }
        response = session.get(URL, params = params, stream = True)

    save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value

    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk: # filter out keep-alive new chunks
                f.write(chunk)

def download_data():

    file_id = '1xaBDhoobN5Ex2mFgWyxsAxOL9E20Ymzi'
    path = './data/football_data.zip'

    if not os.path.exists('./data'):
        os.mkdir('./data')
    if not os.path.exists('./data/football_data.zip'):
        try:
            download_file_from_google_drive(file_id, path)
        except requests.exceptions.RequestException as e:
            print(e)
            sys.exit(1)

def unzip_data():

    target_path = './data/football_data.sqlite'
    zip_path = './data/football_data.zip'

    if not os.path.exists(target_path):
        with zipfile.ZipFile(zip_path) as zip_ref:
            zip_ref.extractall()
            os.rename('./database.sqlite', target_path)
            os.remove('./data/football_data.zip')

def pickle_data():
    path = './data/football_data.sqlite'

    england_match_query = "SELECT * FROM Match WHERE league_id IN (SELECT id FROM Country WHERE name = 'England')"
    england_team_query = "SELECT * From Team WHERE id >= 3457 AND id <= 8784"
    england_player_qyery = """SELECT DISTINCT * FROM Player
                              WHERE player_api_id IN (SELECT home_player_1 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_2 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_3 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_4 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_5 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_6 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_7 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_8 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_9 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_10 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT home_player_11 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_1 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_2 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_3 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_4 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_5 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_6 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_7 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_8 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_9 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_10 FROM Match WHERE league_id = 1729)
                              OR player_api_id IN (SELECT away_player_11 FROM Match WHERE league_id = 1729)"""
    try:
        conn = sqlite3.connect(path)
        match_df = pd.read_sql_query(england_match_query, conn)
        match_df.to_pickle("./data/match_data.pkl")
        team_df = pd.read_sql_query(england_team_query, conn)
        team_df.to_pickle("./data/team_data.pkl")
        player_df = pd.read_sql(england_player_qyery, conn)
        player_df.to_pickle("./data/player_data.pkl")
        os.remove('./data/football_data.sqlite')

    except sqlite3.Error as e:
        print(e)
        sys.exit(1)

def get_data():
    if not os.path.exists('./data/match_data.pkl') or not os.path.exists('./data/team_data.pkl') or not os.path.exists('./data/player_data.pkl'):
        download_data()
        unzip_data()
        pickle_data()

    match_df = pd.read_pickle('./data/match_data.pkl')
    team_df = pd.read_pickle('./data/team_data.pkl')
    player_df = pd.read_pickle('./data/player_data.pkl')

    return (match_df, team_df, player_df)



