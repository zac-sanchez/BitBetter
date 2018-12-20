import resources
import pandas as pd

def clean_tables():
    match_df, team_df, player_df = resources.get_data()
    clean_match_table(match_df)
    clean_team_table(team_df)
    clean_player_table(player_df)

