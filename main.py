import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots


def main():
    df = pd.read_csv('datasets/udemy_courses.csv')
    df['published_timestamp'] = df['published_timestamp'].transform(lambda time: time.split('-')[0])
    df_free, df_paid = [x for _, x in df.groupby(df['is_paid'])]
    # 1
    total_duration_of_content(df_paid)
    # 2
    # total_number_of_lectures_for_every_theme(df_paid)
    # 3
    # price_changes_depending_on_publishdate(df_paid)
    # 4
    # avg_price_every_level(df_paid)
    # 5
    # avg_price_every_subject(df_paid)
    # 6
    # changing_price_depending_on_subscribers(df_paid)
    # 7
    # the_cheapest_courses(df_paid)
    # 8
    # most_popular_courses_by_subscribers(df_paid)
    # 9
    # the_shortest_courses_by_content_duration(df_paid)
    # 10
    # the_shortest_courses_by_num_lectures(df_paid)
    # 11
    # the_most_popular_courses_from_every_theme_by_subscribers(df_paid)
    # 12
    # num_subscribers_for_each_level(df_paid, df_free)


# 1) суммарная продолжительность контента для каждой темы
def total_duration_of_content(df):
    result = df.groupby("subject").agg({'content_duration': 'sum'})
    fig = px.bar(result, labels={'subject': 'Темы', 'value': 'часы', 'variable': 'темы'},
                 title="Cуммарная продолжительность контента для каждой темы")
    fig.show()


# 2) суммарное количество лекций для каждой темы
def total_number_of_lectures_for_every_theme(df):
    result = df.groupby("subject").agg({'num_lectures': 'sum'})
    fig = px.bar(result, labels={'subject': 'Темы', 'value': 'кол-во лекций', 'variable': 'суммарное кол-во лекций'},
                 title="Суммарное количество лекций для каждой темы")
    fig.show()


# 3) изменения цены курсов в зависимости от даты публикации
def price_changes_depending_on_publishdate(df):
    result = df.groupby(['published_timestamp']).agg({'price': 'mean'})
    fig = px.bar(result,
                 labels={'value': 'цены $', 'variable': 'цены', 'published_timestamp': 'годы'},
                 title="Изменения цены курсов в зависимости от даты публикации")
    fig.show()


# 4) сколько в среднем стоят курсы каждого уровня
def avg_price_every_level(df):
    result = df.groupby(['level']).agg({'price': 'mean'})
    fig = px.bar(result,
                 labels={'level': 'уровень', 'value': 'цены', 'variable': 'цены'},
                 title="Cколько в среднем стоят курсы каждого уровня")
    fig.show()


# 5) сколько в среднем стоят курсы по каждой теме
def avg_price_every_subject(df):
    result = df.groupby(['subject']).agg({'price': 'mean'})
    fig = px.bar(result,
                 labels={'subject': 'тема', 'value': 'цены', 'variable': 'цены'},
                 title="Сколько в среднем стоят курсы по каждой теме")
    fig.show()


# 6) как изменяется цена курсов в зависимости от количества подписчиков
def changing_price_depending_on_subscribers(df):
    result = df.groupby(['price']).count()['num_subscribers']
    fig = px.bar(result,
                 labels={'price': 'цена $', 'value': 'кол-во подписчиков', 'variable': 'кол-во подписчиков'},
                 title="Изменнение цены курсов в зависимости от количества подписчиков")
    fig.show()


# 7) самые дешёвые курсы (10-20-30, на выбор);
def the_cheapest_courses(df):
    # result = df.sort_values(by="price").head(10).groupby(['course_title'])
    result = df.groupby(['course_title']).agg({'price': 'min'}).sort_values(by="price").head(10)
    fig = px.bar(result,
                 labels={'value': 'цена $', 'variable': 'цена $', 'course_title': 'название курса'},
                 title="10 самых дешевых курсов")
    fig.show()


# 8) самые популярные (по количеству подписчиков) курсы
def most_popular_courses_by_subscribers(df):
    # result = df.sort_values(by="price").head(10).groupby(['course_title'])
    result = df.groupby(['course_title']).agg({'num_subscribers': 'max'}).sort_values(by="num_subscribers").tail(10)
    fig = px.bar(result,
                 labels={'value': 'кол-во подписчиков', 'variable': 'кол-во подписчиков',
                         'course_title': 'название курса'},
                 title="Самые популярные (по количеству подписчиков) курсы")
    fig.show()


# 9) самые короткие курсы по продолжительности контента;
def the_shortest_courses_by_content_duration(df):
    result = df.groupby(['course_title']).agg({'content_duration': 'min'}).sort_values(by="content_duration").head(10)
    fig = px.bar(result,
                 labels={'value': 'продолжительность часы', 'variable': 'продолжительность часы',
                         'course_title': 'название курса'},
                 title="Самые короткие курсы по продолжительности контента")
    fig.show()


# 10) самые короткие курсы по количеству лекций
def the_shortest_courses_by_num_lectures(df):
    result = df.groupby(['course_title']).agg({'num_lectures': 'min'}).sort_values(by="num_lectures").head(10)
    fig = px.bar(result,
                 labels={'value': 'кол-во лекций', 'variable': 'кол-во лекций',
                         'course_title': 'название курса'},
                 title="Cамые короткие курсы по количеству лекций")
    fig.show()


# 11) самые популярные (по количеству подписчиков) курсы по каждой из тем.
def the_most_popular_courses_from_every_theme_by_subscribers(df):
    business_finances, graphic_design, music_instruments, web_development = [x for x in df.groupby(df['subject'])]
    result_business_finances = business_finances[1].groupby(['course_title']).agg({'num_subscribers': 'max'}).tail(1)
    result_graphic_design = graphic_design[1].groupby(['course_title']).agg({'num_subscribers': 'max'}).tail(1)
    result_music_instruments = music_instruments[1].groupby(['course_title']).agg({'num_subscribers': 'max'}).tail(1)
    result_web_development = web_development[1].groupby(['course_title']).agg({'num_subscribers': 'max'}).tail(1)
    fig = make_subplots(rows=1, cols=4, subplot_titles=(
        "Бизнес и Финансы", "Графика и Дизайн", "Музыкальные инструменты", "Веб разработка"))
    fig.add_trace(px.bar(result_business_finances)['data'][0], row=1, col=1)
    fig.add_trace(px.bar(result_graphic_design)['data'][0], row=1, col=2)
    fig.add_trace(px.bar(result_music_instruments)['data'][0], row=1, col=3)
    fig.add_trace(px.bar(result_web_development)['data'][0], row=1, col=4)
    fig.show()


# 12 (кол-во подписчиков для каждого уровня) (сумма всех ~ 11М)
def num_subscribers_for_each_level(df_paid, df_free):
    num_subscribers_for_each_level_paid = df_paid.groupby(['level']).agg({'num_subscribers': 'sum'})
    num_subscribers_for_each_level_free = df_free.groupby(['level']).agg({'num_subscribers': 'sum'})
    fig = make_subplots(rows=1, cols=2, subplot_titles=("Платные курсы", "Бесплатные курсы"))
    fig.add_trace(px.bar(num_subscribers_for_each_level_paid)['data'][0], row=1, col=1)
    fig.add_trace(px.bar(num_subscribers_for_each_level_free)['data'][0], row=1, col=2)
    fig.show()


if __name__ == '__main__':
    main()
