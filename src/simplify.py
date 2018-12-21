import resources
import pandas as pd

def clean_match_table(df):
    return df

def clean_team_table(df):
    return df

def clean_player_table(df):
    return df

def clean_tables():
    match_df, team_df, player_df = resources.get_data()
    match_df = clean_match_table(match_df)
    team_df = clean_team_table(team_df)
    player_df = clean_player_table(player_df)


