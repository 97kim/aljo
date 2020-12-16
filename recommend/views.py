from django.shortcuts import render
from .models import Recommend
from django.contrib.auth.decorators import login_required
from aljoadmin.models import Aljoadmin
from django.db.models import Q
from django.utils.text import slugify

import pandas as pd
import csv
import surprise
from surprise import Reader, Dataset
import warnings


# Create your views here.

# def bar(request):

@login_required
def recommend_index(request):
    recommends = Recommend.objects
    return render(request, 'menu-recommend.html', {'recommends': recommends})

@login_required
def recommend_result(request):
    test = Recommend()
    ratings={}

    if request.POST.get('q1'):
        test.q1 = request.POST.get('q1')
        ratings['타로 밀크티'] = test.q1
    if request.POST.get('q2'):
        test.q2 = request.POST.get('q2')
        ratings['블랙 밀크티'] = test.q2
    if request.POST.get('q3'):
        test.q3 = request.POST.get('q3')
        ratings['초콜렛 밀크티'] = test.q3
    if request.POST.get('q4'):
        test.q4 = request.POST.get('q4')
        ratings['우롱 밀크티'] = test.q4
    if request.POST.get('q5'):
        test.q5 = request.POST.get('q5')
        ratings['망고 요구르트'] = test.q5
    if request.POST.get('q6'):
        test.q6 = request.POST.get('q6')
        ratings['망고 스무디'] = test.q6
    if request.POST.get('q7'):
        test.q7 = request.POST.get('q7')
        ratings['딸기 쉐이크'] = test.q7
    if request.POST.get('q8'):
        test.q8 = request.POST.get('q8')
        ratings['토피넛 라떼'] = test.q8
    if request.POST.get('q9'):
        test.q9 = request.POST.get('q9')
        ratings['녹차 플랫치노'] = test.q9
    if request.POST.get('q10'):
        test.q10 = request.POST.get('q10')
        ratings['초콜릿칩 플랫치노'] = test.q10
    if request.POST.get('q11'):
        test.q11 = request.POST.get('q11')
        ratings['오리진 쉐이크'] = test.q11
    if request.POST.get('q12'):
        test.q12 = request.POST.get('q12')
        ratings['녹차 라떼'] = test.q12
    if request.POST.get('q13'):
        test.q13 = request.POST.get('q13')
        ratings['아이스티'] = test.q13
    if request.POST.get('q14'):
        test.q14 = request.POST.get('q14')
        ratings['초콜릿크림칩 프라푸치노'] = test.q14
    if request.POST.get('q15'):
        test.q15 = request.POST.get('q15')
        ratings['바닐라크림 프라푸치노'] = test.q15
    if request.POST.get('q16'):
        test.q16 = request.POST.get('q16')
        ratings['말차크림 프라푸치노'] = test.q16
    if request.POST.get('q17'):
        test.q17 = request.POST.get('q17')
        ratings['화이트딸기크림 프라푸치노'] = test.q17
    if request.POST.get('q18'):
        test.q18 = request.POST.get('q18')
        ratings['카라멜 프라푸치노'] = test.q18
    if request.POST.get('q19'):
        test.q19 = request.POST.get('q19')
        ratings['자바칩 프라푸치노'] = test.q19
    if request.POST.get('q20'):
        test.q20 = request.POST.get('q20')
        ratings['아메리카노'] = test.q20
    test.save()
    f = open('menu_rating.csv', 'a', newline='', encoding='utf-8')
    wr = csv.writer(f)
    user_num = pd.read_csv("menu_rating.csv")
    user_num = int(user_num['user'][-1:])
    user_num +=1
    user_num = str(user_num)
    for i in ratings:
        wr.writerow([user_num, i, ratings[i]])
    f.close()
    warnings.filterwarnings('ignore')
    data = pd.read_csv('menu_rating.csv', encoding="utf-8", sep=",", error_bad_lines=False)
    df = data[['user', 'menu', 'rating']]
    # df = df.drop_duplicates(['id', 'menu'], keep="last")

    def recur_dictify(frame):
        if len(frame.columns) == 1:
            if frame.values.size == 1: return frame.values[0][0]
            return frame.values.squeeze()
        grouped = frame.groupby(frame.columns[0])
        d = {k: recur_dictify(g.iloc[:, 1:]) for k, g in grouped}
        return d

    df_to_dict = recur_dictify(df)

    name_list = []
    menu_set = set()

    for user_key in df_to_dict:
        # print(user_key)
        name_list.append(user_key)
        # 현재 사용자가 평점을 매긴 메뉴를 set에 담는다
        for menu_key in df_to_dict[user_key]:
            menu_set.add(menu_key)

    menu_list = list(menu_set)

    # 협업필터링 추천 시스템에 사용할 rating 딕셔너리 만들기(user,menu,rating)
    # 학습할 데이터 준비
    rating_dic = {
        'user': [],
        'menu': [],
        'rating': []
    }

    # 사용자 수 만큼 반복
    for name_key in df_to_dict:
        for menu_key in df_to_dict[name_key]:
            # 사용자 인덱스 번호 추출
            a1 = name_list.index(name_key)
            # 메뉴 인덱스 번호 추출
            a2 = menu_list.index(menu_key)
            # 평점 가져오기
            a3 = df_to_dict[name_key][menu_key]
            # 딕셔너리에 추가하기
            rating_dic['user'].append(a1)
            rating_dic['menu'].append(a2)
            rating_dic['rating'].append(a3)

    df = pd.DataFrame(rating_dic)
    df = df.drop_duplicates(['user', 'menu', 'rating'], keep="last")
    reader = Reader(rating_scale=(1, 5))  # 평점의 범위를 정하기 위해 평점을 포함한 파일을 파싱하는 Reader클래스를 사용합니다.
    # 학습하기 : surprise.KNNBasic
    # surprise에서 사용할 데이터 셋을 구성할 때 필요한 이름들은
    # 데이터가 저장되어 있는 딕셔너리의 컬럼 이름들이다.
    # 첫번째 -> user 두번쨰 -> menu 세번째 ->rating
    # 즉, 컬럼명의 리스트가 필요하다.
    col_list = ['user', 'menu', 'rating']
    data = Dataset.load_from_df(df[col_list], reader)

    trainset = data.build_full_trainset()  # 전체 데이터셋으로부터 fold를 나누지 않고 훈련셋을 리턴한다.
    option = {'name': 'pearson'}
    algo = surprise.KNNBasic(sim_options=option)  # 사용된 머신러닝 알고리즘 : KNNBasic, 유사도 측정방법 : 피어슨 상관계수

    algo.fit(trainset)

    # 예측 :CF추천시스템
    # 사용자의 메뉴 추천받기
    new_user = user_num
    index = name_list.index(new_user)
    result = algo.get_neighbors(index, k=3)

    def localtest():
        recommend_list = []
        results=[]
        for r1 in result:
            max_rating = data.df[data.df['user'] == r1]['rating'].max()  # 대부분 아마 5점일 것이다.
            # print(max_rating)
            menu_id = data.df[(data.df['rating'] == max_rating) & (data.df['user'] == r1)]['menu'].values  # 5점 준 메뉴들을 찾는다.
            # print(r1, menu_id)  # 최근접 이웃 3명의 user인덱스와 그 user들이 최고점을 준 메뉴들을 출력한다.
            for menu_item in menu_id:
                recommend_list.append(menu_list[menu_item])
        #         recommend_set.add(menu_list[menu_item])
        # 원래는 set으로 하려 했으나 1~3위까지의 추천을 위한 중복된 데이터의 개수를 세기 위해 리스트로 구현할 것이다.

        count_menu = list(menu_set)
        # print(recommend_list)
        count_dic = {}
        for i in count_menu:
            count_dic[i] = 0

        for menu in recommend_list:
            count_dic[menu] += 1

        def f1(x):
            return count_dic[x]

        first = max(count_dic.keys(), key=f1)
        # del count_dic[first]
        # second = max(count_dic.keys(), key=f1)
        # del count_dic[second]
        # third = max(count_dic.keys(), key=f1)
        # results.append(second)
        # results.append(third)
        return first

    def pic():
        first=localtest()
        pic = '/static/img/'+first+'.png'
        # pic = '''<img src="{%static 'img/'''+localtest()+'''.png'%}" alt="추천 이미지" />'''
        return pic

    aljorecommend = Aljoadmin.objects.filter(Q(foodname__icontains=localtest()) | Q(recipe__icontains=localtest())).distinct()

    return render(request, 'menu-recommend-result.html', {'localtest':localtest, 'pic':pic, 'aljorecommend':aljorecommend})
