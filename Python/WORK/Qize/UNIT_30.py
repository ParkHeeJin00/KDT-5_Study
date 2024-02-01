# [연습문제] 30.6
korean, english, mathematics, science = 100, 86, 81, 91

def get_max_score(*args):
    return max(args)

max_score = get_max_score(korean, english, mathematics, science)
print(f'높은 점수 : {max_score}')

max_score = get_max_score(english, science)
print(f'높은 점수 : {max_score}')

# [심사문제] 30.7
korean, english, mathematics, science = map(int,input().split())

def get_min_max_score(*args):
    return min(args), max(args)
def get_average(**args):
    return sum(args.values())/len(args)

min_score, max_score = get_min_max_score(korean, english, mathematics, science)
average_score = get_average(korean=korean, english=english, mathematics=mathematics, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))

min_score, max_score = get_min_max_score(english, science)
average_score = get_average(english=english, science=science)
print('낮은 점수: {0:.2f}, 높은 점수: {1:.2f}, 평균 점수: {2:.2f}'.format(min_score, max_score, average_score))
