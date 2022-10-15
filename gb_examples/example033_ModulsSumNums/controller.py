from unittest import result
import model_sum
import model_mult
import view


def button_click_sum():
    value_a = view.get_value()
    value_b = view.get_value()
    model_sum.init(value_a, value_b)
    result = model_sum.do_it()
    view.view_data(result, 'sum')


def button_click_mult():
    value_a = view.get_value()
    value_b = view.get_value()
    model_mult.init(value_a, value_b)
    result = model_mult.do_it()
    view.view_data(result, 'sum')
