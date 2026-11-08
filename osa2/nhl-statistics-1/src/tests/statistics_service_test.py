import unittest

from player_reader import PlayerReader
from statistics_service import StatisticsService
from player_reader import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Atte", "Aten tiimi", 46, 30),
            Player("Juuso", "JUUSOT", 20, 54),
            Player("Karri",   "Aten tiimi", 43, 44),
            Player("Terri", "JUUSOT", 12, 66),
            Player("Perri", "Aten tiimi", 26, 77)
        ]

class TestStatistics(unittest.TestCase):
    
    
    def setUp(self):
        self.stats = StatisticsService(PlayerReaderStub())

    def test_find_specific_player(self):
        player = self.stats.search("Atte")

        self.assertEqual(str(player), str(Player("Atte", "Aten tiimi", 46, 30)))

    def test_search_unknown_player(self):
        player = self.stats.search("Timppa")
        
        self.assertEqual(player, None)

    def test_find_team_by_name(self):
        team = self.stats.team("JUUSOT")

        self.assertEqual(team[0].team, "JUUSOT")
        self.assertEqual(team[1].team, "JUUSOT")

    def test_top_finds_correct_amount_of_players(self):
        result = self.stats.top(3)

        self.assertEqual(len(result), 4)