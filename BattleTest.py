import Monster,Players,Battle,pygame

spieler = Players.Player()
gegner = Monster.Goblin()
pygame.init()
Battle.Kampf(spieler,gegner)
    
    