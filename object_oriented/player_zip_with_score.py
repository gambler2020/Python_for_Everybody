# print the player name and their goal scores
players=["Ronaldo", "Messi", "Neymar", "Mbappe", "Salah", "Luis_Suarez"]
Goals=[63, 62, 54, 50, 49, 43]
for pl, go in zip(players, Goals):
    print("Player : %s   Score : %d" %(pl, go))
