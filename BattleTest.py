import Monster,Players,Items,Battle,pygame

spieler = Players.Player()
gegner = Monster.Troll()
pygame.init()
spieler.waffe = Items.Axt()
spieler.inventar.einfuegen(Items.Heiltrank())
Battle.Kampf(spieler,gegner)