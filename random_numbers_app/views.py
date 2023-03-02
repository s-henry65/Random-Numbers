from django.shortcuts import render, redirect
import random, requests
from collections import OrderedDict
import numpy as np
from random_numbers_app.models import LotteryResults
from decouple import config
import schedule
import time

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

    context = {
        'results': results, 'times_drawn': sorted_values, 'by_number': sorted_keys,
    }
    return render(request, 'random_numbers/generate_nums.html', context)

def generate_luckylines(request):
    if request.method == 'GET':
        return render(request, 'random_numbers/generate_luckylines.html') 
    elif request.method == 'POST':
        num_count = {} # keeps track of how many times a number is drawn
        results = {}
        draw_count = 1
        draw = int(request.POST['draw'])
        while draw_count <= draw:
            counter = 0
            num_draw = []
            nums = [[1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ], [ 13, 14, 15, 16 ], [ 17, 18, 19, 20 ],
                    [ 21, 22, 23, 24 ], [ 25, 26, 27, 28 ], [ 29, 30, 31, 32 ]]
            while counter <= 7:
                pick = (random.choice(nums[counter]))
                num_count[pick] = num_count.get(pick, 0) + 1
                num_draw.append(pick)
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
   
    context = {
        'results': results, 'times_drawn': sorted_values, 'by_number': sorted_keys,
    }
    return render(request, 'random_numbers/generate_luckylines.html', context)

def generate_powerball(request):
    if request.method == 'GET':
        return render(request, 'random_numbers/generate_powerball.html') 
    elif request.method == 'POST':
        num_count = {} # keeps track of how many times a number is drawn
        powerball_count = {} # keeps track of how many times the powerball number is drawn
        results = {}
        draw_count = 1
        num_amount = 5
        draw = int(request.POST['draw'])
        while draw_count <= draw:
            counter = 1
            num_draw = []
            nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69 ]
            powerball_nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26]
            while counter <= num_amount:
                pick = (random.choice(nums))
                num_count[pick] = num_count.get(pick, 0) + 1
                num_draw.append(pick)
                nums.remove(pick)
                counter += 1
            pick_powerball = (random.choice(powerball_nums))
            powerball_count[pick_powerball] = powerball_count.get(pick_powerball, 0) + 1
            num_draw = sorted(num_draw)
            num_draw.append(pick_powerball)
            num_draw_str = ' '.join([str(elem) for elem in num_draw])
            results[draw_count] = num_draw_str
            draw_count += 1

    # Sorting powerball by values
    pb_keys = list(powerball_count.keys())
    pb_values = list(powerball_count.values())
    pb_sorted_value_index = np.argsort(pb_values)
    pb_sorted_values = {pb_keys[i]: pb_values[i] for i in pb_sorted_value_index}
    pb_sorted_values = dict(reversed(pb_sorted_values.items()))

    # Sorting by values
    keys = list(num_count.keys())
    values = list(num_count.values())
    sorted_value_index = np.argsort(values)
    sorted_values = {keys[i]: values[i] for i in sorted_value_index}
    sorted_values = dict(reversed(sorted_values.items()))
        # sorted_values = sorted(num_count.items(), key=lambda x:x[1], reverse=True)

    context = {
        'results': results, 'times_drawn': sorted_values, 'powerball': pb_sorted_values,
    }
    return render(request, 'random_numbers/generate_powerball.html', context)

def generate_megamill(request):
    if request.method == 'GET':
        return render(request, 'random_numbers/generate_megamill.html') 
    elif request.method == 'POST':
        num_count = {} # keeps track of how many times a number is drawn
        mega_count = {} # keeps track of how many times the megaball number is drawn
        results = {}
        draw_count = 1
        num_amount = 5
        draw = int(request.POST['draw'])
        while draw_count <= draw:
            counter = 1
            num_draw = []
            nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70 ]
            mega_nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25 ]
            while counter <= num_amount:
                pick = (random.choice(nums))
                num_count[pick] = num_count.get(pick, 0) + 1
                num_draw.append(pick)
                nums.remove(pick)
                counter += 1
            pick_mega = (random.choice(mega_nums))
            mega_count[pick_mega] = mega_count.get(pick_mega, 0) + 1
            num_draw = sorted(num_draw)
            num_draw.append(pick_mega)
            num_draw_str = ' '.join([str(elem) for elem in num_draw])
            results[draw_count] = num_draw_str
            draw_count += 1

    # Sorting megaball by values
    mb_keys = list(mega_count.keys())
    mb_values = list(mega_count.values())
    mb_sorted_value_index = np.argsort(mb_values)
    mb_sorted_values = {mb_keys[i]: mb_values[i] for i in mb_sorted_value_index}
    mb_sorted_values = dict(reversed(mb_sorted_values.items()))

    # Sorting by values
    keys = list(num_count.keys())
    values = list(num_count.values())
    sorted_value_index = np.argsort(values)
    sorted_values = {keys[i]: values[i] for i in sorted_value_index}
    sorted_values = dict(reversed(sorted_values.items()))
        # sorted_values = sorted(num_count.items(), key=lambda x:x[1], reverse=True)

    context = {
        'results': results, 'times_drawn': sorted_values, 'megaball': mb_sorted_values,
    }
    return render(request, 'random_numbers/generate_megamill.html', context)

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
    # Test number
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
    
    context = { 'matches': matches,  
        'times_drawn': sorted_values, 'by_number': sorted_keys, 'total_matches': match_count, 'match2': pick2, 'match3': pick3,
        'match4': pick4, 'match5': pick5, 'match6': pick6, 'test_number': num_pick_str,
    }
    return render(request, 'random_numbers/test_results.html', context)

def test_luckylines(request):
    if request.method == 'GET':
        return render(request, 'random_numbers/test_luckylines.html') 
    elif request.method == 'POST':
        match_count = 0
        pick2 = 0
        pick3 = 0
        pick4 = 0
        pick5 = 0
        pick6 = 0
        pick7 = 0
        pick8 = 0
        matches = {}
        num_pick = str(request.POST['num_pick'])
        num_pick = [int(x) for x in num_pick.split()]
        num_count = {}
        draw_count = 1
        draw = int(request.POST['draw'])
        match_num = int(request.POST['match_num'])
        while draw_count <= draw:
            counter = 0
            num_draw = []
            num_match = []
            nums = [[1, 2, 3, 4 ], [ 5, 6, 7, 8 ], [ 9, 10, 11, 12 ], [ 13, 14, 15, 16 ], [ 17, 18, 19, 20 ],
                    [ 21, 22, 23, 24 ], [ 25, 26, 27, 28 ], [ 29, 30, 31, 32 ]]
            while counter <= 7:
                pick = (random.choice(nums[counter]))
                num_count[pick] = num_count.get(pick, 0) + 1
                num_draw.append(pick)
                for num in num_pick:
                    if num == pick:
                        num_match.append(pick)
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
            if len(num_match) == 7:
                pick6 += 1
            if len(num_match) == 8:
                pick6 += 1
            if len(num_match) >= match_num:
                match_count += 1
                # print(f'\nDraw {draw_count} ',sorted(num_draw))
                # print(len(num_match), 'Match: ' ,sorted(num_match))
                matches[draw_count] = dict(match_total = len(num_match), numbers = num_draw_str, matches = num_match_str)
            draw_count += 1
    # Test number
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
    
    context = { 'matches': matches,  
        'times_drawn': sorted_values, 'by_number': sorted_keys, 'total_matches': match_count, 'match2': pick2, 'match3': pick3,
        'match4': pick4, 'match5': pick5, 'match6': pick6, 'match7': pick7, 'match8': pick8, 'test_number': num_pick_str,
    }
    return render(request, 'random_numbers/luckylines_results.html', context)

def test_powerball(request):
    if request.method == 'GET':
        return render(request, 'random_numbers/test_powerball.html') 
    elif request.method == 'POST':
        match_count = 0
        pick2 = 0
        pick3 = 0
        pick4 = 0
        pick5 = 0
        pick6 = 0
        matches = {}
        num_pick = str(request.POST['num_pick'])
        num_pick = [int(x) for x in num_pick.split()]
        powerball_pick = int(request.POST['powerball_pick'])
        num_count = {} # keeps track of how many times a number is drawn
        powerball_count = {} # keeps track of how many times the powerball number is drawn
        draw_count = 1
        draw = int(request.POST['draw'])
        match_num = int(request.POST['match_num'])
        while draw_count <= draw:
            counter = 1
            num_draw = []
            num_match = []
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69 ]
            powerball_nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26]
            while counter <= len(num_pick):
                pick = (random.choice(nums))
                num_count[pick] = num_count.get(pick, 0) + 1
                num_draw.append(pick)
                for num in num_pick:
                    if num == pick:
                        num_match.append(pick)
                nums.remove(pick)
                counter += 1
            pick_powerball = (random.choice(powerball_nums))
            powerball_count[pick_powerball] = powerball_count.get(pick_powerball, 0) + 1
            # change numbers drawn from list to string
            num_draw = sorted(num_draw)
            num_draw.append(pick_powerball)
            num_draw_str = ' '.join([str(elem) for elem in num_draw])
            num_match = sorted(num_match)
            if powerball_pick == pick_powerball:
                num_match.append(pick_powerball)
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
    # Test number
    num_pick.append(powerball_pick)
    num_pick_str = ' '.join([str(elem) for elem in num_pick])

    # Sorting powerball by values
    pb_keys = list(powerball_count.keys())
    pb_values = list(powerball_count.values())
    pb_sorted_value_index = np.argsort(pb_values)
    pb_sorted_values = {pb_keys[i]: pb_values[i] for i in pb_sorted_value_index}
    pb_sorted_values = dict(reversed(pb_sorted_values.items()))

    # Sorting by values
    keys = list(num_count.keys())
    values = list(num_count.values())
    sorted_value_index = np.argsort(values)
    sorted_values = {keys[i]: values[i] for i in sorted_value_index}
    sorted_values = dict(reversed(sorted_values.items()))
        # sorted_values = sorted(num_count.items(), key=lambda x:x[1], reverse=True)

    context = { 'matches': matches,  
        'times_drawn': sorted_values, 'powerball': pb_sorted_values, 'total_matches': match_count, 'match2': pick2, 'match3': pick3,
        'match4': pick4, 'match5': pick5, 'match6': pick6, 'test_number': num_pick_str,
    }
    return render(request, 'random_numbers/powerball_results.html', context)

def test_megamill(request):
    if request.method == 'GET':
        return render(request, 'random_numbers/test_megamill.html') 
    elif request.method == 'POST':
        match_count = 0
        pick2 = 0
        pick3 = 0
        pick4 = 0
        pick5 = 0
        pick6 = 0
        matches = {}
        num_pick = str(request.POST['num_pick'])
        num_pick = [int(x) for x in num_pick.split()]
        megaball_pick = int(request.POST['megaball_pick'])
        num_count = {} # keeps track of how many times a number is drawn
        megaball_count = {} # keeps track of how many times the powerball number is drawn
        draw_count = 1
        draw = int(request.POST['draw'])
        match_num = int(request.POST['match_num'])
        while draw_count <= draw:
            counter = 1
            num_draw = []
            num_match = []
            nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38,
                39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
                 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70 ]
            megaball_nums = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
                21, 22, 23, 24, 25 ]
            while counter <= len(num_pick):
                pick = (random.choice(nums))
                num_count[pick] = num_count.get(pick, 0) + 1
                num_draw.append(pick)
                for num in num_pick:
                    if num == pick:
                        num_match.append(pick)
                nums.remove(pick)
                counter += 1
            pick_megaball = (random.choice(megaball_nums))
            megaball_count[pick_megaball] = megaball_count.get(pick_megaball, 0) + 1
            # change numbers drawn from list to string
            num_draw = sorted(num_draw)
            num_draw.append(pick_megaball)
            num_draw_str = ' '.join([str(elem) for elem in num_draw])
            num_match = sorted(num_match)
            if megaball_pick == pick_megaball:
                num_match.append(pick_megaball)
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
    # Test number
    num_pick.append(megaball_pick)
    num_pick_str = ' '.join([str(elem) for elem in num_pick])

    # Sorting powerball by values
    mb_keys = list(megaball_count.keys())
    mb_values = list(megaball_count.values())
    mb_sorted_value_index = np.argsort(mb_values)
    mb_sorted_values = {mb_keys[i]: mb_values[i] for i in mb_sorted_value_index}
    mb_sorted_values = dict(reversed(mb_sorted_values.items()))

    # Sorting by values
    keys = list(num_count.keys())
    values = list(num_count.values())
    sorted_value_index = np.argsort(values)
    sorted_values = {keys[i]: values[i] for i in sorted_value_index}
    sorted_values = dict(reversed(sorted_values.items()))
        # sorted_values = sorted(num_count.items(), key=lambda x:x[1], reverse=True)

    context = { 'matches': matches,  
        'times_drawn': sorted_values, 'megaball': mb_sorted_values, 'total_matches': match_count, 'match2': pick2, 'match3': pick3,
        'match4': pick4, 'match5': pick5, 'match6': pick6, 'test_number': num_pick_str,
    }
    return render(request, 'random_numbers/megamill_results.html', context)

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
    try:
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
        lotto_data.special_num = int(results['0']['plays'][0]['draws'][0]['numbers'][5]['value'])
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
        lotto_data.special_num = int(results['1']['plays'][0]['draws'][0]['numbers'][5]['value'])
        lotto_data.next_draw = results['1']['plays'][0]['draws'][0]['nextDrawDate']
        lotto_data.jackpot = results['1']['plays'][0]['draws'][0]['nextDrawJackpot']
        lotto_data.save()

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
        lotto_data.jackpot = '$1000/wk for Life'
        lotto_data.save()

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
        
        # Pick4 @ 1
        lotto_data = LotteryResults.objects.get(id=8)
        lotto_data.game_name = 'Pick4 @ 1pm'
        lotto_data.draw_date = results['5']['plays'][0]['draws'][0]['date']
        pb_nums = results['5']['plays'][0]['draws'][0]['numbers']
        pb_numbers = []
        for num in pb_nums:
            if num['order'] <= 4:
                pb_numbers.append(int(num['value']))
        pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
        lotto_data.numbers = pb_numbers_str
        lotto_data.special_num = '-'
        lotto_data.next_draw = results['5']['plays'][0]['draws'][0]['nextDrawDate']
        lotto_data.jackpot = 'Up to $5000'
        lotto_data.save()

        # Pick4 @ 4
        lotto_data = LotteryResults.objects.get(id=9)
        lotto_data.game_name = 'Pick4 @ 4pm'
        lotto_data.draw_date = results['5']['plays'][1]['draws'][0]['date']
        pb_nums = results['5']['plays'][1]['draws'][0]['numbers']
        pb_numbers = []
        for num in pb_nums:
            if num['order'] <= 4:
                pb_numbers.append(int(num['value']))
        pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
        lotto_data.numbers = pb_numbers_str
        lotto_data.special_num = '-'
        lotto_data.next_draw = results['5']['plays'][1]['draws'][0]['nextDrawDate']
        lotto_data.jackpot = 'Up to $5000'
        lotto_data.save()

        # Pick4 @ 7
        lotto_data = LotteryResults.objects.get(id=10)
        lotto_data.game_name = 'Pick4 @ 7pm'
        lotto_data.draw_date = results['5']['plays'][2]['draws'][0]['date']
        pb_nums = results['5']['plays'][2]['draws'][0]['numbers']
        pb_numbers = []
        for num in pb_nums:
            if num['order'] <= 4:
                pb_numbers.append(int(num['value']))
        pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
        lotto_data.numbers = pb_numbers_str
        lotto_data.special_num = '-'
        lotto_data.next_draw = results['5']['plays'][2]['draws'][0]['nextDrawDate']
        lotto_data.jackpot = 'Up to $5000'
        lotto_data.save()

        # Pick4 @ 10
        lotto_data = LotteryResults.objects.get(id=11)
        lotto_data.game_name = 'Pick4 @ 10pm'
        lotto_data.draw_date = results['5']['plays'][3]['draws'][0]['date']
        pb_nums = results['5']['plays'][3]['draws'][0]['numbers']
        pb_numbers = []
        for num in pb_nums:
            if num['order'] <= 4:
                pb_numbers.append(int(num['value']))
        pb_numbers_str = ' '.join([str(elem) for elem in pb_numbers])
        lotto_data.numbers = pb_numbers_str
        lotto_data.special_num = '-'
        lotto_data.next_draw = results['5']['plays'][3]['draws'][0]['nextDrawDate']
        lotto_data.jackpot = 'Up to $5000'
        lotto_data.save()

        return redirect('or_lotto')
    except:
        print('Error in receiveing data')
        return redirect('or_lotto')

