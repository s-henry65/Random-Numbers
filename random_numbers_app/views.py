from django.shortcuts import render, redirect
import random, requests
from collections import OrderedDict
import numpy as np
from random_numbers_app.models import LotteryResults
from decouple import config

def index(request):
    return render(request, 'random_numbers/index.html')

def exit(request):
    return render(request, 'random_numbers/exit.html')

def generate_random_num(request):
    if request.method == 'GET':
        return render(request, 'random_numbers/generate_nums.html') 
    elif request.method == 'POST':
        num_count = {} # keeps track of how many times a number is drawn
        results = {}
        draw_count = 1
        num_amount = int(request.POST['num_amount'])
        draw = int(request.POST['draw'])
        while draw_count <= draw:
            counter = 1
            num_draw = []
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48 ]
            while counter <= num_amount:
                pick = (random.choice(nums))
                num_count[pick] = num_count.get(pick, 0) + 1
                num_draw.append(pick)
                nums.remove(pick)
                counter += 1
            num_draw = sorted(num_draw)
            num_draw_str = ' '.join([str(elem) for elem in num_draw])
            results[draw_count] = num_draw_str
            draw_count += 1
    # Sorting by keys
    num_count_keys = list(num_count.keys())
    num_count_keys.sort()
    sorted_keys = {i: num_count[i] for i in num_count_keys}
        # sorted_keys = sorted(num_count.items(), key=lambda x:x[0])

    # Sorting by values
    keys = list(num_count.keys())
    values = list(num_count.values())
    sorted_value_index = np.argsort(values)
    sorted_values = {keys[i]: values[i] for i in sorted_value_index}
    sorted_values = dict(reversed(sorted_values.items()))
        # sorted_values = sorted(num_count.items(), key=lambda x:x[1], reverse=True)
    # print('\nResults: ', results)
    # print('\nSorted by times drawn (number, draws)')
    # print(sorted_values)
    # print('\nSorted by number (number, draws)')
    # print(sorted_keys)
    context = {
        'results': results, 'times_drawn': sorted_values, 'by_number': sorted_keys,
    }
    return render(request, 'random_numbers/generate_nums.html', context)

def test_number(request):
    if request.method == 'GET':
        return render(request, 'random_numbers/test_numbers.html') 
    elif request.method == 'POST':
        match_count = 0
        pick2 = 0
        pick3 = 0
        pick4 = 0
        pick5 = 0
        pick6 = 0
        matches = {}
        num_pick = []
        num_pick = str(request.POST['num_pick'])
        num_pick = [int(x) for x in num_pick.split()]
        num_count = {}
        draw_count = 1
        draw = int(request.POST['draw'])
        match_num = int(request.POST['match_num'])
        while draw_count <= draw:
            counter = 1
            num_draw = []
            num_match = []
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48 ]
            while counter <= len(num_pick):
                pick = (random.choice(nums))
                num_count[pick] = num_count.get(pick, 0) + 1
                num_draw.append(pick)
                for num in num_pick:
                    if num == pick:
                        num_match.append(pick)
                nums.remove(pick)
                counter += 1
            # change numbers drawn from list to string
            num_draw = sorted(num_draw)
            num_draw_str = ' '.join([str(elem) for elem in num_draw])
            num_match = sorted(num_match)
            num_match_str = ' '.join([str(elem) for elem in num_match])
            # print(num_draw)
            if len(num_match) == 2:
                pick2 += 1
            if len(num_match) == 3:
                pick3 += 1
            if len(num_match) == 4:
                pick4 += 1
            if len(num_match) == 5:
                pick5 += 1
            if len(num_match) == 6:
                pick6 += 1
            if len(num_match) >= match_num:
                match_count += 1
                # print(f'\nDraw {draw_count} ',sorted(num_draw))
                # print(len(num_match), 'Match: ' ,sorted(num_match))
                matches[draw_count] = dict(match_total = len(num_match), numbers = num_draw_str, matches = num_match_str)
            draw_count += 1
    num_pick_str = ' '.join([str(elem) for elem in num_pick])
    # Sorting by keys
    num_count_keys = list(num_count.keys())
    num_count_keys.sort()
    sorted_keys = {i: num_count[i] for i in num_count_keys}
        # sorted_keys = sorted(num_count.items(), key=lambda x:x[0])

    # Sorting by values
    keys = list(num_count.keys())
    values = list(num_count.values())
    sorted_value_index = np.argsort(values)
    sorted_values = {keys[i]: values[i] for i in sorted_value_index}
    sorted_values = dict(reversed(sorted_values.items()))
        # sorted_values = sorted(num_count.items(), key=lambda x:x[1], reverse=True)
        # sorted_keys = sorted(num_count.items(), key=lambda x:x[0])
    # print()
    # print(match_count, 'Total Matches ', pick2,'2-Matches ', pick3,'3-Matches ', pick4,'4-Matches ', pick5,'5-Matches ', pick6,'6-Matches')
    # print('\nSorted by times drawn (number, draws)')
    # print(sorted_values)
    # print('\nSorted by number (number, draws)')
    # print(sorted_keys)
    context = { 'matches': matches,  
        'times_drawn': sorted_values, 'by_number': sorted_keys, 'total_matches': match_count, 'match2': pick2, 'match3': pick3,
        'match4': pick4, 'match5': pick5, 'match6': pick6, 'test_number': num_pick_str,
    }
    return render(request, 'random_numbers/test_results.html', context)

def or_lotto(request):
    results = LotteryResults.objects.all()
    context = {
        'results': results,
    }
    if request.method == 'GET':
        return render(request, 'random_numbers/oregon_lotto.html', context) 


def get_lotto_results(request):
    key = config("lotto_key")
    url = "https://lottery-results.p.rapidapi.com/games-by-state/US/OR"
    headers = {
        "X-RapidAPI-Key": key,
        "X-RapidAPI-Host": "lottery-results.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers)
    results = response.json()
    print(results)
    
    # Powerball
    lotto_data = LotteryResults.objects.get(id=2)
    lotto_data.game_name = results['0']['name']
    lotto_data.draw_date = results['0']['plays'][0]['draws'][0]['date']
    pb_nums = results['0']['plays'][0]['draws'][0]['numbers']
    pb_numbers = []
    for num in pb_nums:
        if num['order'] <= 5:
            pb_numbers.append(int(num['value']))
    pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
    lotto_data.numbers = pb_numbers_str
    lotto_data.special_num = results['0']['plays'][0]['draws'][0]['numbers'][5]['value']
    lotto_data.next_draw = results['0']['plays'][0]['draws'][0]['nextDrawDate']
    lotto_data.jackpot = results['0']['plays'][0]['draws'][0]['nextDrawJackpot']
    lotto_data.save()

    # Mega Millions
    lotto_data = LotteryResults.objects.get(id=4)
    lotto_data.game_name = results['1']['name']
    lotto_data.draw_date = results['1']['plays'][0]['draws'][0]['date']
    pb_nums = results['1']['plays'][0]['draws'][0]['numbers']
    pb_numbers = []
    for num in pb_nums:
        if num['order'] <= 5:
            pb_numbers.append(int(num['value']))
    pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
    lotto_data.numbers = pb_numbers_str
    lotto_data.special_num = results['1']['plays'][0]['draws'][0]['numbers'][5]['value']
    lotto_data.next_draw = results['1']['plays'][0]['draws'][0]['nextDrawDate']
    lotto_data.jackpot = results['1']['plays'][0]['draws'][0]['nextDrawJackpot']
    lotto_data.save()
    
    # mega_millions = {}
    # mega_millions['game'] = results['1']['name']
    # mega_millions['draw date'] = results['1']['plays'][0]['draws'][0]['date']
    # mega_nums = results['1']['plays'][0]['draws'][0]['numbers']
    # mega_numbers = []
    # for num in mega_nums:
    #     if num['order'] <= 5:
    #         mega_numbers.append(int(num['value']))
    # mega_numbers_str = ' '.join([str(elem) for elem in mega_numbers])
    # mega_millions['numbers'] = mega_numbers_str
    # mega_millions['megaball'] = results['1']['plays'][0]['draws'][0]['numbers'][5]['value']
    # mega_millions['next draw'] = results['1']['plays'][0]['draws'][0]['nextDrawDate']
    # mega_millions['jackpot'] = results['1']['plays'][0]['draws'][0]['nextDrawJackpot']
    # print('\nMega Millions: ', mega_millions)

    # Megabucks
    lotto_data = LotteryResults.objects.get(id=5)
    lotto_data.game_name = results['2']['name']
    lotto_data.draw_date = results['2']['plays'][0]['draws'][0]['date']
    pb_nums = results['2']['plays'][0]['draws'][0]['numbers']
    pb_numbers = []
    for num in pb_nums:
        if num['order'] <= 6:
            pb_numbers.append(int(num['value']))
    pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
    lotto_data.numbers = pb_numbers_str
    lotto_data.special_num = '-'
    lotto_data.next_draw = results['2']['plays'][0]['draws'][0]['nextDrawDate']
    lotto_data.jackpot = results['2']['plays'][0]['draws'][0]['nextDrawJackpot']
    lotto_data.save()

    # megabucks = {}
    # megabucks['game'] = results['2']['name']
    # megabucks['draw date'] = results['2']['plays'][0]['draws'][0]['date']
    # mega_nums = results['2']['plays'][0]['draws'][0]['numbers']
    # mega_numbers = []
    # for num in mega_nums:
    #     if num['order'] <= 6:
    #         mega_numbers.append(int(num['value']))
    # mega_numbers_str = ' '.join([str(elem) for elem in mega_numbers])
    # megabucks['numbers'] = mega_numbers_str
    # megabucks['megaball'] = '-'
    # megabucks['next draw'] = results['2']['plays'][0]['draws'][0]['nextDrawDate']
    # megabucks['jackpot'] = results['2']['plays'][0]['draws'][0]['nextDrawJackpot']
    # print('\nMegabucks: ', megabucks)

    # Win 4 Life
    lotto_data = LotteryResults.objects.get(id=6)
    lotto_data.game_name = results['3']['name']
    lotto_data.draw_date = results['3']['plays'][0]['draws'][0]['date']
    pb_nums = results['3']['plays'][0]['draws'][0]['numbers']
    pb_numbers = []
    for num in pb_nums:
        if num['order'] <= 4:
            pb_numbers.append(int(num['value']))
    pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
    lotto_data.numbers = pb_numbers_str
    lotto_data.special_num = '-'
    lotto_data.next_draw = results['3']['plays'][0]['draws'][0]['nextDrawDate']
    lotto_data.jackpot = results['3']['plays'][0]['draws'][0]['nextDrawJackpot']
    lotto_data.save()
     
    # win4life = {}
    # win4life['game'] = results['3']['name']
    # win4life['draw date'] = results['3']['plays'][0]['draws'][0]['date']
    # win_nums = results['3']['plays'][0]['draws'][0]['numbers']
    # win_numbers = []
    # for num in win_nums:
    #     if num['order'] <= 4:
    #         win_numbers.append(int(num['value']))
    # win_numbers_str = ' '.join([str(elem) for elem in win_numbers])
    # win4life['numbers'] = win_numbers_str
    # win4life['megaball'] = '-'
    # win4life['next draw'] = results['3']['plays'][0]['draws'][0]['nextDrawDate']
    # win4life['jackpot'] = results['3']['plays'][0]['draws'][0]['nextDrawJackpot']
    # print('\nWin 4 Life: ', win4life)

    # Lucky Lines
    lotto_data = LotteryResults.objects.get(id=7)
    lotto_data.game_name = results['4']['name']
    lotto_data.draw_date = results['4']['plays'][0]['draws'][0]['date']
    pb_nums = results['4']['plays'][0]['draws'][0]['numbers']
    pb_numbers = []
    for num in pb_nums:
        if num['order'] <= 8:
            pb_numbers.append(int(num['value']))
    pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
    lotto_data.numbers = pb_numbers_str
    lotto_data.special_num = '-'
    lotto_data.next_draw = results['4']['plays'][0]['draws'][0]['nextDrawDate']
    lotto_data.jackpot = results['4']['plays'][0]['draws'][0]['nextDrawJackpot']
    lotto_data.save()

    # luckylines = {}
    # luckylines['game'] = results['4']['name']
    # luckylines['draw date'] = results['4']['plays'][0]['draws'][0]['date']
    # lucky_nums = results['4']['plays'][0]['draws'][0]['numbers']
    # lucky_numbers = []
    # for num in lucky_nums:
    #     if num['order'] <= 8:
    #         lucky_numbers.append(int(num['value']))
    # lucky_numbers_str = ' '.join([str(elem) for elem in lucky_numbers])
    # luckylines['numbers'] = lucky_numbers_str
    # luckylines['megaball'] = '-'
    # luckylines['next draw'] = results['4']['plays'][0]['draws'][0]['nextDrawDate']
    # luckylines['jackpot'] = results['4']['plays'][0]['draws'][0]['nextDrawJackpot']
    # print('\nLucky Lines: ', luckylines)
      
    # pic4 = {}
    # pic4['game'] = results['5']['name']
    # pic4['draw date'] = results['5']['plays'][0]['draws'][0]['date']
    # pic_nums = results['5']['plays'][0]['draws'][0]['numbers']
    # pic_numbers = []
    # for num in pic_nums:
    #     if num['order'] <= 4:
    #         pic_numbers.append(int(num['value']))
    # pic_numbers_str = ' '.join([str(elem) for elem in pic_numbers])
    # pic4['numbers'] = pic_numbers_str
    # pic4['megaball'] = '-'
    # pic4['next draw'] = results['5']['plays'][0]['draws'][0]['nextDrawDate']
    # pic4['jackpot'] = results['5']['plays'][0]['draws'][0]['nextDrawJackpot']
 
    return redirect('random_numbers/oregon_lotto.html')

