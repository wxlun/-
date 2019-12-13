from django.template import Library
from django.utils.safestring import mark_safe
import datetime
register = Library()

@register.simple_tag
def build_filter_ele(filter_column,admin_class):
    column_obj = admin_class.model._meta.get_field(filter_column)
    try:
        filter_ele = "<select name = '%s'>" % filter_column
        for choice in column_obj.get_choices():
            selected = ''
            if filter_column in admin_class.filter_conditions: #当前字段被过滤
                if str(choice[0]) == admin_class.filter_conditions.get(filter_column): #当前值被选中
                    selected = 'selected'
            option = "<option value = '%s' %s>%s</option>" %(choice[0],selected,choice[1])
            filter_ele += option
    except AttributeError as e:
        print("err",e)
        filter_ele = "<select name = '%s__gte'>" % filter_column
        if column_obj.get_internal_type() in ('DateField','DateTimeField'):
            time_obj = datetime.datetime.now()
            time_list = [
                ['','--------'],
                [time_obj,"Today"],
                [time_obj - datetime.timedelta(7),'七天内'],
                [time_obj.replace(day=1),"本月"],
                [time_obj - datetime.timedelta(90),'三个月内'],
                [time_obj.replace(month=1,day=1),'YearToDay(YTD)'],
                ['','ALL'],
            ]
            option = ''
            for i in time_list:
                selected = ''
                time_to_str = ''if not i[0] else "%s-%s-%s" %(i[0].year,i[0].month,i[0].day)
                if "%s__gte"% filter_column in admin_class.filter_conditions:  # 当前字段被过滤
                    if time_to_str == admin_class.filter_conditions.get("%s__gte"% filter_column):  # 当前值被选中
                        selected = 'selected'
                option = "<option value = '%s' %s>%s</option>" %(time_to_str,selected,i[1])
                filter_ele += option
    filter_ele += "</select>"
    return mark_safe(filter_ele)

@register.simple_tag
def build_table_row(obj,admin_class):
    """生成一条记录的html element"""
    ele = ""
    if admin_class.list_display:
        for index,column_name in enumerate(admin_class.list_display):
            column_obj = admin_class.model._meta.get_field(column_name)
            if column_obj.choices:
                column_data = getattr(obj,'get_%s_display' % column_name)()
            else:
                column_data = getattr(obj,column_name)
            td_ele = "<td>%s</td>" % column_data
            if index == 0:
                td_ele = "<td><a href='%s/change/'>%s</a></td>" % (obj.id,column_data)
            # td_ele = "<td>%s</td>"%column_data
            ele += td_ele
    else:
        # td_ele = "<td>%s</td>" % obj  #默认返回obj的__str__方法
        td_ele = "<td><a href='%s/change/'>%s</a></td>" % (obj.id, obj)
        ele += td_ele

    return mark_safe(ele)

@register.simple_tag
def get_model_name(admin_class):
    return admin_class.model._meta.model_name.upper()

@register.simple_tag
def render_filtered_args(admin_class,render_html=True):
    """拼接筛选的字段"""
    if admin_class.filter_conditions:
        ele = ''
        for k,v in admin_class.filter_conditions.items():
            ele += '&%s=%s' %(k,v)
        if render_html:
            return mark_safe(ele)
        else:
            return ele
        return mark_safe(ele)
    else:
        return ''


@register.simple_tag
def render_sorted_arrow(column,sorted_column):
    if column in sorted_column:
        last_sort_index = sorted_column[column]
        if last_sort_index.startswith('-'):
            arrow_direction = 'bottom'
        else:
            arrow_direction = 'top'

        ele = '''<span class="glyphicon glyphicon-triangle-%s" aria-hidden="true"></span>''' % arrow_direction
        return mark_safe(ele)
    return ''


@register.simple_tag
def get_sorted_column(column,sorted_column,forloop):
    if column in sorted_column:
        last_sort_index = sorted_column[column]
        if last_sort_index.startswith('-'):
            this_time_sort_index = last_sort_index.strip('-')
        else:
            this_time_sort_index = '-%s' % last_sort_index
        return this_time_sort_index
    else:
        return forloop

@register.simple_tag
def render_paginator(querysets,admin_class,sorted_column):
    ele = '''
          <ul class="pagination">
    '''
    for i in querysets.paginator.page_range:
        if abs(querysets.number - i) < 3:
            active = ''
            if querysets.number == i:
                active = 'active'
            filter_ele = render_filtered_args(admin_class)

            sorted_ele = ''
            if sorted_column:
                sorted_ele = '&_o=%s' % list(sorted_column.values())[0]

            p_ele = '''<li class="%s"><a href="?_page=%s%s%s">%s</a></li>''' % (active,i,filter_ele,sorted_ele,i)
            ele += p_ele
    ele += "</ul>"

    return mark_safe(ele)


@register.simple_tag
def get_current_sorted_column_index(sorted_column):
    return list(sorted_column.values())[0] if sorted_column else ''