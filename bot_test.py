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
    'agua': {'RESULT': 'FAILED',
                 'POSITION': None,
                 'MISSING':  'HOT',
                 },
    'agua_2': {'RESULT': 'FAILED',
                 'POSITION': None,
                 'MISSING':  'WARM',
                 },
    'agua_3': {'RESULT': 'FAILED',
                 'POSITION': None,
                 'MISSING':  'COLD',
                 },
    'agua_4': {'RESULT': 'FAILED',
                 'POSITION': None,
                 'MISSING':  'MISSING',
                 },
    'agua_5': {'RESULT': 'FAILED',
                 'POSITION': None,
                 'MISSING':  None,
                 },
    'nos_dieron': {'RESULT': 'FAILED',
                 'POSITION': None,
                 'MISSING':  None,
                 },
}

print bot.evaluate_turn(feedback['negativo'], 100)
print bot.evaluate_turn(feedback['positivo'], 100)
print bot.evaluate_turn(feedback['positivo'], 100)
print bot.evaluate_turn(feedback['agua'], 100)
print bot.evaluate_turn(feedback['agua_2'], 100)
print bot.evaluate_turn(feedback['agua_3'], 100)
print bot.evaluate_turn(feedback['agua_4'], 100)
print bot.evaluate_turn(feedback['agua_5'], 100)
print bot.evaluate_turn(feedback['nos_dieron'], 99)
