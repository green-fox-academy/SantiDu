def should_hit(player_total, dealer_card_val, player_aces):
    """Return True if the player should hit (request another card) given the current game
    state, or False if the player should stay. player_aces is the number of aces the player has.
    """
    if dealer_card_val in (2, 3) and player_total in range(11, 18) and player_aces == 1:
        return True
    elif dealer_card_val in (2, 3) and player_total <= 12:
        return True
    elif dealer_card_val in (4, 5, 6) and player_total in range(11, 18) and player_aces == 1:
        return True
    elif dealer_card_val in (4, 5, 6) and player_total <= 11:
        return True
    elif dealer_card_val in (7, 8) and player_total in range(11, 18) and player_aces == 1:
        return True
    elif dealer_card_val in (7, 8) and player_total <= 16:
        return True
    elif dealer_card_val in (9, 10, 11) and player_total in range(11, 19) and player_aces == 1:
        return True
    elif dealer_card_val in (9, 10, 11) and player_total <= 16:
        return True
    return False