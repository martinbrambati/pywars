from bot import Bot

# Test
bot = Bot()

feedback = {
    'negativo': {'RESULT': 'FAILED',
                 'POSITION': None,
                 'MISSING':  None,
                 },
    'positivo': {'RESULT': 'SUCCESS',
                 'POSITION': (10, 0),
                 'MISSING': 'HOT',
                 },
}

print bot.evaluate_turn(feedback['negativo'],100)