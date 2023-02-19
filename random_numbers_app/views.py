from django.shortcuts import render, redirect
import random
from collections import OrderedDict
import numpy as np

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
    if request.method == 'GET':
        return render(request, 'random_numbers/oregon_lotto.html') 

def get_lotto_results(request):
    if request.method == 'GET':
        
    # context = {
    #     'results': oregon_results,
    # }
        return render(request, 'random_numbers/oregon_lotto.httml')